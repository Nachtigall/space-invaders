import unittest
from unittest.mock import Mock, call

from invader import Invader
from scanner import Scanner


class TestScanner(unittest.TestCase):

    def setUp(self):
        self.detector = Mock()
        self.detector.detections = ['a']

        def indexes():
            yield 1

        self.detector.detect_header_indexes.return_value = indexes()

        self.data = ['--o-----o--',
                     '---o---o---',
                     '--ooooooo--',
                     'o-o-----o-o',
                     '---oo-oo---']

        self.scanner = Scanner(self.detector, self.data)

    def test_scan_for_invader(self):
        invader_data = ['0-o--o--o-0']
        invader = Invader(invader_data)

        expected_calls = [call('0-o--o--o-0', '--o-----o--'),
                          call('0-o--o--o-0', '---o---o---'),
                          call('0-o--o--o-0', '--ooooooo--'),
                          call('0-o--o--o-0', 'o-o-----o-o'),
                          call('0-o--o--o-0', '---oo-oo---')]

        self.scanner.scan_for_invader(invader)

        self.detector.detect_header_indexes.assert_has_calls(expected_calls)
        self.detector.detect_invader.assert_called_with(invader_data, ['--o-----o--'], len(invader_data),
                                                        1 + len(invader_data[0]), 0, len(invader_data))

