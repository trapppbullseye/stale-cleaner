#!/usr/bin/env python3
"""Close stale issues and PRs automatically"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Close stale issues and PRs automatically")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("stale-cleaner v0.1.0");return
 print(f"[13:11] stale-cleaner ready")
if __name__=="__main__":main()
