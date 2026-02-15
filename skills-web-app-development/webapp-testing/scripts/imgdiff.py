#!/usr/bin/env python3
"""
Minimal image diff utility for visual regression workflows.

Usage:
  python scripts/imgdiff.py baseline.png current.png --out diff.png

Exit codes:
  0 = within thresholds
  1 = different beyond thresholds
  2 = error
"""

from __future__ import annotations

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline")
    parser.add_argument("current")
    parser.add_argument("--out", default="diff.png")
    parser.add_argument("--max-rms", type=float, default=0.0, help="Allowable RMS threshold")
    parser.add_argument(
        "--max-different-pixels",
        type=int,
        default=0,
        help="Allowable number of changed pixels (RGBA-wise)",
    )
    args = parser.parse_args()

    try:
        from PIL import Image, ImageChops  # type: ignore
        from PIL.ImageStat import Stat  # type: ignore
    except Exception:
        print("Pillow is required. Install with: pip install pillow", file=sys.stderr)
        return 2

    try:
        baseline = Image.open(args.baseline).convert("RGBA")
        current = Image.open(args.current).convert("RGBA")
    except Exception as exc:
        print(f"Failed to read images: {exc}", file=sys.stderr)
        return 2

    if baseline.size != current.size:
        print(f"Different sizes: {baseline.size} vs {current.size}", file=sys.stderr)
        return 1

    diff = ImageChops.difference(baseline, current)
    stat = Stat(diff)

    # Overall RMS across RGBA channels.
    rms_channels = stat.rms
    rms = (sum(v * v for v in rms_channels) / len(rms_channels)) ** 0.5

    # Count pixels where any channel differs.
    diff_data = diff.getdata()
    different_pixels = sum(1 for px in diff_data if px != (0, 0, 0, 0))

    if different_pixels > 0:
        diff.save(args.out)

    within_rms = rms <= args.max_rms
    within_pixels = different_pixels <= args.max_different_pixels

    if within_rms and within_pixels:
        print(
            f"Images within thresholds (RMS={rms:.4f}, changed_pixels={different_pixels})."
        )
        return 0

    print(
        "Images differ "
        f"(RMS={rms:.4f}, threshold={args.max_rms:.4f}; "
        f"changed_pixels={different_pixels}, threshold={args.max_different_pixels}). "
        f"Wrote {args.out}"
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
