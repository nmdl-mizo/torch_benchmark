import os
import pathlib
import logging
import time
import argparse
import subprocess


BANNER = r"""
 _____              _       ____                  _
|_   _|__  _ __ ___| |__   | __ )  ___ _ __   ___| |__
  | |/ _ \| '__/ __| '_ \  |  _ \ / _ \ '_ \ / __| '_ \
  | | (_) | | | (__| | | | | |_) |  __/ | | | (__| | | |
  |_|\___/|_|  \___|_| |_| |____/ \___|_| |_|\___|_| |_| v0.0.1
"""
SEP = "-" * 80


def main(args: argparse.Namespace):
    # get args
    save_name = args.save_name
    cwd = pathlib.Path(os.getcwd())
    codes_path = cwd / "codes"
    save_pth = cwd / save_name

    # set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(save_pth)
    logger.addHandler(fh)

    # print banner
    logger.info(BANNER)

    for i, code in enumerate(codes_path.glob("*.py")):
        logger.info(SEP)
        logger.info(f"[START CODE_{i+1}] Running {code.name}")

        # run code
        start = time.time()
        res = subprocess.run(["python3", f"{code}"], cwd=str(codes_path), capture_output=True, text=True)
        end = time.time()

        logger.info(f"\t{res.stdout}")
        logger.info(f"[FINISH CODE_{i+1}] Time taken: {end - start:.2f} [s]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--save_name",
        type=str,
        default="torch_benchmark.log",
        help="name of log file, default: torch_benchmark.log",
    )
    args = parser.parse_args()
    main(args)
