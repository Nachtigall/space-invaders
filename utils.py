import sys

import logger

logger = logger.get_logger(__name__)


def read_invader_file(filename: str, start_end_symbol: str) -> list:
    data = []
    invaders_data = []

    try:
        with open(filename, 'r') as f:
            started_reading = False

            for line in f:
                line = line.strip('\n')
                if not started_reading:
                    if line == start_end_symbol:
                        started_reading = True
                elif line == start_end_symbol:
                    started_reading = False
                    invaders_data.append(data)
                    data = []
                else:
                    data.append(line)

        return invaders_data
    except FileNotFoundError:
        logger.error("File with invader templates is not found! Exiting.")
        sys.exit(1)


def read_radar_file(filename) -> list:
    try:
        with open(filename, 'r') as radar_data:
            content = radar_data.read().splitlines()

        return content
    except FileNotFoundError:
        logger.error("File with radar data is not found! Exiting.")
        sys.exit(1)


def present_results(detection: dict) -> None:
    # added +1 to match actual file line numbers, since iteration is starting from 0, not 1
    logger.info("Invader detected!")
    logger.info(f"starting_line: {detection['starting_line'] + 1}, ending_line: {detection['ending_line'] + 1}. "
                f"starting_index {detection['starting_index']}, ending_index: {detection['ending_index']}")
    present_invader(detection['invader'])


def present_invader(invader_data: list, warning_level: str = "info") -> None:
    for data in invader_data:
        if warning_level == 'warn':
            logger.warning(data)
        else:
            logger.info(data)
