from invader import Invader
from detector import Detector


class Scanner:
    def __init__(self, detector: Detector, content: list):
        self.detector = detector
        self.scanner_content = content

    def scan_for_invader(self, invader: Invader) -> list:
        """
        Scans radar content. If possible indexes are detected - starts detection process.
        :param invader: instance of invader
        :return: returns list of detections
        """
        for i, line in enumerate(self.scanner_content):
            detected_indexes = {n for n in self.detector.detect_header_indexes(invader.head, line)}

            for index in detected_indexes:
                starting_index = index
                ending_index = starting_index + invader.width

                starting_line = i
                ending_line = i + invader.height

                detection_part = self.scanner_content[starting_line:ending_line]

                self.detector.detect_invader(invader.data, detection_part, starting_index, ending_index,
                                             starting_line, ending_line)
            else:
                continue

        return self.detector.detections
