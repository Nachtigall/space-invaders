import sys

import logger
import utils
from detector import Detector
from invader import Invader
from scanner import Scanner

START_END_SYMBOLS = '~~~~'
INVADER_TEMPLATES_FILENAME = 'invader_samples/default_invaders.txt'
RADAR_DATA_FILENAME = 'radar_sample/sample.txt'
CHARS_DIFFERENCE = 2

logger = logger.get_logger(__name__)


def main():
    logger.info("Hello! We are starting.\n"
                "Set parameters:\n"
                f"Start and end file symbols: {START_END_SYMBOLS}\n"
                f"Invader templates filename: {INVADER_TEMPLATES_FILENAME}\n"
                f"Radar data filename: {RADAR_DATA_FILENAME}\n"
                f"Allowed char difference: {CHARS_DIFFERENCE}\n")

    invaders_data = utils.read_invader_file(INVADER_TEMPLATES_FILENAME, START_END_SYMBOLS)

    if not invaders_data:
        logger.error("No correct invader data is found. Exiting.")
        sys.exit(1)

    radar_content = utils.read_radar_file(RADAR_DATA_FILENAME)

    detector = Detector(chars_difference=CHARS_DIFFERENCE)
    invaders = [Invader(data) for data in invaders_data]

    results = []

    for invader in invaders:
        if not invader.is_valid():
            logger.warning('Not valid invader template detected. This invader will be skipped:')
            utils.present_invader(invader.data, 'warn')
            continue

        scanner = Scanner(detector, radar_content)
        results = scanner.scan_for_invader(invader)

    if results:
        for detection in results:
            utils.present_results(detection)

    else:
        logger.info("No invaders detected. Yay!")


if __name__ == '__main__':
    main()
