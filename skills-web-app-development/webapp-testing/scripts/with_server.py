#!/usr/bin/env python3
"""
Start one or more servers, wait for readiness, run a command, then clean up.

Usage:
  # Single server and port check
  python scripts/with_server.py --server "npm run dev" --port 5173 -- npm test

  # Multiple servers
  python scripts/with_server.py \
    --server "npm run api" --port 3000 \
    --server "npm run web" --port 5173 \
    -- npm run test:e2e

  # Optional HTTP health checks (repeatable)
  python scripts/with_server.py \
    --server "npm run web" --port 5173 \
    --url "http://127.0.0.1:5173/healthz" \
    -- npm test
"""

from __future__ import annotations

import argparse
import os
import signal
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from typing import List


def wait_for_port(host: str, port: int, timeout_s: int) -> None:
    start = time.time()
    while time.time() - start < timeout_s:
        try:
            with socket.create_connection((host, port), timeout=1):
                return
        except OSError:
            time.sleep(0.25)
    raise RuntimeError(f"Port not ready: {host}:{port} within {timeout_s}s")


def wait_for_url(url: str, timeout_s: int) -> None:
    start = time.time()
    while time.time() - start < timeout_s:
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                if 200 <= response.status < 400:
                    return
        except urllib.error.URLError:
            pass
        except TimeoutError:
            pass
        time.sleep(0.25)
    raise RuntimeError(f"URL not ready: {url} within {timeout_s}s")


def terminate_process_tree(proc: subprocess.Popen[bytes], grace_s: int) -> None:
    if proc.poll() is not None:
        return

    try:
        if os.name != "nt":
            os.killpg(proc.pid, signal.SIGTERM)
        else:
            proc.terminate()
    except Exception:
        proc.terminate()

    try:
        proc.wait(timeout=grace_s)
        return
    except subprocess.TimeoutExpired:
        pass

    try:
        if os.name != "nt":
            os.killpg(proc.pid, signal.SIGKILL)
        else:
            proc.kill()
    except Exception:
        proc.kill()
    proc.wait()


def parse_command(args: argparse.Namespace) -> List[str]:
    command = args.command
    if command and command[0] == "--":
        command = command[1:]
    return command


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Run a command with one or more servers")
    parser.add_argument(
        "--server",
        action="append",
        dest="servers",
        required=True,
        help="Server command (repeatable)",
    )
    parser.add_argument(
        "--port",
        action="append",
        dest="ports",
        type=int,
        required=True,
        help="Port for each server (must match --server count)",
    )
    parser.add_argument(
        "--url",
        action="append",
        dest="urls",
        default=[],
        help="Optional health URL to poll after ports are ready (repeatable)",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host for port polling (default: 127.0.0.1)")
    parser.add_argument("--timeout", type=int, default=45, help="Timeout seconds per check (default: 45)")
    parser.add_argument("--grace", type=int, default=5, help="Grace seconds before force kill (default: 5)")
    parser.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="Command to run after readiness checks (prefix with -- to separate)",
    )

    args = parser.parse_args(argv)
    command = parse_command(args)

    if not command:
        print("Error: missing command to run. Use -- before the command.", file=sys.stderr)
        return 2

    if len(args.servers) != len(args.ports):
        print("Error: --server and --port counts must match.", file=sys.stderr)
        return 2

    procs: List[subprocess.Popen[bytes]] = []

    try:
        for idx, (server_cmd, port) in enumerate(zip(args.servers, args.ports), start=1):
            print(f"Starting server {idx}/{len(args.servers)}: {server_cmd}")
            proc = subprocess.Popen(
                server_cmd,
                shell=True,
                start_new_session=(os.name != "nt"),
            )
            procs.append(proc)
            print(f"Waiting for port {args.host}:{port} ...")
            wait_for_port(args.host, port, timeout_s=args.timeout)
            print(f"Ready: {args.host}:{port}")

        for url in args.urls:
            print(f"Waiting for URL {url} ...")
            wait_for_url(url, timeout_s=args.timeout)
            print(f"Ready: {url}")

        print(f"\nAll readiness checks passed")
        print(f"Running command: {' '.join(command)}\n")
        result = subprocess.run(command)
        return result.returncode
    finally:
        if procs:
            print(f"\nStopping {len(procs)} server(s)...")
        for idx, proc in enumerate(procs, start=1):
            try:
                terminate_process_tree(proc, grace_s=args.grace)
                print(f"Stopped server {idx}")
            except Exception as exc:
                print(f"Failed to stop server {idx}: {exc}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
