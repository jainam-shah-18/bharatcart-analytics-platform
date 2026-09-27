import logging
import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path("data/raw")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_PREFIX = os.getenv("S3_PREFIX", "raw")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def validate_configuration():
    if not BUCKET_NAME:
        raise ValueError("S3_BUCKET_NAME is missing from .env")


def find_csv_files():
    files = list(DATA_DIR.glob("*.csv"))

    if not files:
        raise FileNotFoundError(f"No CSV files found in {DATA_DIR.resolve()}")

    return files


def upload_files(files):
    s3 = boto3.client("s3")

    for file_path in files:
        if file_path.stat().st_size == 0:
            raise ValueError(f"Empty file detected: {file_path.name}")

        object_key = f"{S3_PREFIX}/{file_path.name}"

        logging.info("Uploading %s to s3://%s/%s", file_path, BUCKET_NAME, object_key)

        s3.upload_file(
            str(file_path),
            BUCKET_NAME,
            object_key,
        )

    logging.info("Uploaded %d CSV files successfully", len(files))


def main():
    validate_configuration()
    files = find_csv_files()
    upload_files(files)


if __name__ == "__main__":
    main()