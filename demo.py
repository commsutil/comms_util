# demo.py - Test comms_util
# Explanation: CLI for GrokCall; runs a mock voice call.
# Notes: python demo.py --dest alice --mode voice

import argparse
import asyncio
from comms.grokcall import GrokCall

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dest", default="testuser")
    parser.add_argument("--mode", default="voice")
    args = parser.parse_args()
    asyncio.run(GrokCall(args.dest, args.mode))
    print("Call initiated—check IPFS/Twitter!")
