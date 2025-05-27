"""
run_eda.py

Basic exploratory summary of outputs for each bill in the 'output/' folder.
"""

import csv
import io
import pathlib
import pandas as pd
from utils_logger import logger

# ROOT FOLDERS

DIR_SCRIPTS = pathlib.Path(__file__).resolve().parent
DIR_ROOT = DIR_SCRIPTS.parent
DIR_DATA = DIR_ROOT / "data"
DIR_OUTPUT = DIR_ROOT / "output"

logger.info(f"{DIR_ROOT=}")
logger.info(f"{DIR_SCRIPTS=}")
logger.info(f"{DIR_DATA=}")
logger.info(f"{DIR_OUTPUT=}")

# FILENAMES

FILE_AMENDMENTS = "amendments.csv"
FILE_HEADINGS = "headings.txt"
FILE_KEYWORDS = "keyword_hits.txt"
FILE_MONEY = "money_lines.csv"


# RELATIVE OUTPUT PATH FUNCTIONS


def PATH_KEYWORDS(bill_output):
    return bill_output / FILE_KEYWORDS


def PATH_HEADINGS(bill_output):
    return bill_output / FILE_HEADINGS


def PATH_MONEY(bill_output):
    return bill_output / FILE_MONEY


def PATH_AMENDMENTS(bill_data):
    return bill_data / FILE_AMENDMENTS


# HELPER FUNCTIONS


def list_bill_folders(output_root):
    return [p.name for p in output_root.iterdir() if p.is_dir()]


def summarize_text_file(path: pathlib.Path):
    try:
        with path.open(encoding="utf-8") as f:
            lines = f.readlines()
        logger.info(f"{path.name} - {len(lines)} lines")
    except FileNotFoundError:
        logger.error(f" Missing: {path}")
    except Exception as e:
        logger.error(f" Error reading {path}: {e}")


def summarize_csv_file(path: pathlib.Path):
    try:
        if not path.exists():
            logger.error(f" Missing: {path}")
            return

        # Read manually and filter good rows
        good_lines = []
        bad_line_count = 0

        with path.open(encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)  # assume first line is header
            num_cols = len(headers)
            good_lines.append(",".join(headers))

            for line in f:
                if len(line.strip()) == 0:
                    continue
                field_count = len(next(csv.reader([line])))
                if field_count == num_cols:
                    good_lines.append(line.strip())
                else:
                    bad_line_count += 1

        # Parse cleaned content with pandas
        csv_cleaned = "\n".join(good_lines)
        df = pd.read_csv(io.StringIO(csv_cleaned))

        logger.info(f" {path.name} - {len(df)} rows, {len(df.columns)} columns")
        if bad_line_count > 0:
            logger.warning(f" {path.name} - Skipped {bad_line_count} malformed line(s)")
    except Exception as e:
        logger.error(f" Error reading {path}: {e}")


# MAIN FUNCTION


def run_eda():
    if not DIR_OUTPUT.exists():
        logger.error(f"No output folder found: {DIR_OUTPUT}")
        return

    bill_folders = list_bill_folders(DIR_OUTPUT)
    if not bill_folders:
        logger.error("No processed bills found in output/")
        return

    for bill in bill_folders:
        logger.info(f"\n📄 Summary for bill: {bill}")
        bill_output = DIR_OUTPUT / bill
        bill_data = DIR_DATA / bill

        logger.info("Source Data:")
        summarize_csv_file(PATH_AMENDMENTS(bill_data))

        logger.info("Generated Output:")
        summarize_text_file(PATH_KEYWORDS(bill_output))
        summarize_text_file(PATH_HEADINGS(bill_output))
        summarize_csv_file(PATH_MONEY(bill_output))

        logger.info("-" * 40)


if __name__ == "__main__":
    run_eda()
