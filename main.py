#!/usr/bin/env python3
"""Museum of the Year 3000 — one-line museum label (make.fun text entry)."""
import os

LINE = "Plastic Fork (c. 2025). Ceremonial trident of the Takeaway Feast. Believed to snap after exactly three bites."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
