#!/usr/bin/env python3
"""
Wait for one or more HTTP endpoints to become healthy.

Usage:
  python scripts/wait_for_health.py --url http://127.0.0.1:3000/health
  python scripts/wait_for_health.py \
    --url http://127.0.0.1:3000/health \
    --url http://127.0.0.1:5173/health \
    --timeout 120

Exit codes:
  0 = all endpoints healthy
  1 = timeout / unhealthy
  2 = invalid usage
"""

from __future__ import annotations

import argparse
import sys
import time
import urllib.error
import urllib.request
from typing import Iterable, Tuple


def parse_expected_statuses(values: Iterable[int] | None) -> set[int]:
    if values:
        return set(values)
    return set(range(200, 400))


def probe(url: str, expected_statuses: set[int], expect_text: str | None, request_timeout: float) -> Tuple[bool, str]:
    try:
        with urllib.request.urlopen(url, timeout=request_timeout) as response:
            status = response.status
            body = response.read(4096).decode("utf-8", errors="ignore")
            if status not in expected_statuses:
                return False, f"status {status} not in expected set"
            if expect_text and expect_text not in body:
                return False, f"missing expected text: {expect_text!r}"
            return True, f"healthy (status={status})"
    except urllib.error.HTTPError as exc:
        return False, f"http error {exc.code}"
    except urllib.error.URLError as exc:
        return False, f"url error {exc.reason}"
    except TimeoutError:
        return False, "request timeout"
    except Exception as exc:  # pragma: no cover
        return False, f"unexpected error: {exc}"


def wait_for_url(
    url: str,
    expected_statuses: set[int],
    expect_text: str | None,
    timeout_s: float,
    interval_s: float,
    request_timeout: float,
) -> bool:
    deadline = time.time() + timeout_s
    last_reason = "not checked"

    while time.time() < deadline:
        ok, reason = probe(url, expected_statuses, expect_text, request_timeout)
        if ok:
            print(f"{url}: {reason}")
            return True
        last_reason = reason
        print(f"{url}: waiting ({reason})")
        time.sleep(interval_s)

    print(f"{url}: timeout after {timeout_s:.1f}s ({last_reason})", file=sys.stderr)
    return False


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Wait for health endpoints")
    parser.add_argument(
        "--url",
        action="append",
        required=True,
        help="Health URL to check (repeatable)",
    )
    parser.add_argument(
        "--expect-status",
        action="append",
        type=int,
        help="Allowed status code (repeatable). Default: any 2xx/3xx.",
    )
    parser.add_argument(
        "--expect-text",
        help="Optional response text that must be present",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=90.0,
        help="Per-URL timeout in seconds (default: 90)",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Polling interval in seconds (default: 1)",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=2.0,
        help="Per-request timeout in seconds (default: 2)",
    )
    args = parser.parse_args(argv)

    if args.timeout <= 0 or args.interval <= 0 or args.request_timeout <= 0:
        print("timeout, interval, and request-timeout must be > 0", file=sys.stderr)
        return 2

    expected_statuses = parse_expected_statuses(args.expect_status)

    for url in args.url:
        ok = wait_for_url(
            url=url,
            expected_statuses=expected_statuses,
            expect_text=args.expect_text,
            timeout_s=args.timeout,
            interval_s=args.interval,
            request_timeout=args.request_timeout,
        )
        if not ok:
            return 1

    print("All health checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
