import Levenshtein
from typing import Generator


class Detector:
    def __init__(self, chars_difference):
        self.chars_difference = chars_difference
        self.detections = []

    def detect_header_indexes(self, invader_head: str, radar_line: str) -> Generator[int, None, None]:
        """
        Detects all possible indexes for header pattern within radar line.
        :param invader_head: invader header line
        :param radar_line: line from radar data
        :return: returns generator
        """
        for i in range(len(radar_line)):
            try_pattern = radar_line[i:i + len(invader_head)]

            if self._match_detected(invader_head, try_pattern):
                pattern_index = radar_line.find(try_pattern)
                yield pattern_index
            else:
                i += 1
                continue

    def detect_invader(self, invader: list, part_to_detect: list, starting_index: int,
                       ending_index: int, starting_line: int, ending_line: int) -> list:
        """
        Detects matches in provided invader data and pre-selected part of radar data.
        :param invader: invader full data
        :param part_to_detect: selected part of radar data
        :param starting_index: starting index line from which begins possible invader match
        :param ending_index: ending index line where ends possible invader match
        :param starting_line: starting line in radar data where possible invader begins
        :param ending_line: ending line in radar data where possible invader ends
        :return: List of detections
        """
        detection = []
        invader_footprint = []

        for invader_line, radar_line in zip(invader, part_to_detect):
            radar_line = radar_line[starting_index:ending_index]

            if self._match_detected(invader_line, radar_line):
                detection.append(True)
                invader_footprint.append(radar_line)
            else:
                detection.append(False)

        if detection and all(detection):
            self._create_detection_results(invader_footprint, starting_line, ending_line, starting_index, ending_index)

        return self.detections

    def _create_detection_results(self, invader_footprint: list, starting_line: int, ending_line: int,
                                  starting_index: int, ending_index: int) -> None:
        """
        Creates detection results.
        :param invader_footprint: list if invader detected data.
        :param starting_line: line from which invader was detected
        :param ending_line: line where invader body ended
        :param starting_index: index of radar line where invader was detected
        :param ending_index: index of radar line where invader ended
        :return: None
        """
        self.detections.append({'invader': invader_footprint, 'starting_line': starting_line, 'ending_line': ending_line,
                               'starting_index': starting_index, 'ending_index': ending_index})

    def _match_detected(self, invader_line: str, radar_line: str) -> bool:
        """
        Compares two strings of provided data.
        :param invader_line: invader line to compare
        :param radar_line: radar line to compare
        :return: True if distance for two strings are <= than defined chars difference number, else return False
        """
        if Levenshtein.distance(invader_line, radar_line) <= self.chars_difference:
            return True
        return False
