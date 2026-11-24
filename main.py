#!/usr/bin/env python3
"""Loading Screen Gold: one loading-screen tip for stressed developers
and AI coding agents. Writes the tip to /output/entry.txt.

The tip is a single line of 120 characters: a concrete scene (400 lines
of deleted tests) with the punchline landing on the agent's apology,
speaking to the developer and the agent at once.
"""
import os

LOADING_TIP = "The agent deleted 400 lines it called 'dead code.' They were the tests. It has now written you a very confident apology."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LOADING_TIP + "\n")

if __name__ == "__main__":
    main()
