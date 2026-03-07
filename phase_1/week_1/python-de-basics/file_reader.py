from pipeline_logger import get_logger
import os
# file_reader.py | Example file name
logger = get_logger("file_reader")

def read_csv_safe(filepath: str) -> list[dict]:
    logger.info(f"Attempting to read file: {filepath}")
    
    if not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        raise FileNotFoundError(f"No file at {filepath}")
    
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
        logger.info(f"Successfully read {len(lines)} lines from {filepath}")
        return lines
    except Exception as e:
        logger.exception(f"Unexpected error reading file: {e}")
        raise

if __name__ == "__main__":
    read_csv_safe("ghost.csv")