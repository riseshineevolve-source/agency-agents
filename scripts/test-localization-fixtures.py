#!/usr/bin/env python3
import argparse
from localization.fixtures import run

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="build/localization-proof")
    raise SystemExit(run(parser.parse_args().output))
