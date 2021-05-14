import unittest

from detector import Detector
from invader import Invader


class TestDetector(unittest.TestCase):

    def setUp(self):
        self.detector = Detector(chars_difference=2)
        self.invader_template = ['--o-----o--',
                                 '---o---o---',
                                 '--ooooooo--',
                                 '-oo-ooo-oo-',
                                 'ooooooooooo',
                                 'o-ooooooo-o',
                                 'o-o-----o-o',
                                 '---oo-oo---']

    def test_match_detected(self):
        self.assertTrue(self.detector._match_detected('abcd', 'abef'))

    def test_match_not_detected(self):
        self.assertFalse(self.detector._match_detected('abcd', 'agef'))

    def test_invader_detected_difference_less_than_2(self):
        detection_sample = ['--o--------',
                            '--oo---o---',
                            '--ooo-ooo--',
                            '-oo-ooo-oo-',
                            'ooooo-ooooo',
                            'o-ooo-ooo-o',
                            'o-o--o--o-o',
                            '---ooooo---']

        result = self.detector.detect_invader(self.invader_template, detection_sample, 0, 11, 1, 2)
        self.assertEqual(detection_sample, result[0]['invader'])

    def test_invader_not_detected_difference_more_than_2(self):
        detection_sample = ['--o-----o--',
                            '--oo---o---',
                            '--o-o-o-o--',
                            '-oo-o-o-oo-',
                            'oo-oo-oo-oo',
                            'o-ooo-ooo-o',
                            'o-o--o--o-o',
                            '---oo--o---']

        result = self.detector.detect_invader(self.invader_template, detection_sample, 0, 11, 1, 2)
        self.assertEqual(result, [])

    def test_invader_not_detected_not_exact_match(self):
        detector = Detector(chars_difference=0)

        detection_sample = ['--o--------',
                            '---o---o---',
                            '--ooooooo--',
                            '-oo-ooo-oo-',
                            'ooooooooooo',
                            'o-ooooooo-o',
                            'o-o-----o-o',
                            '---oo-oo---']

        result = detector.detect_invader(self.invader_template, detection_sample, 0, 11, 1, 2)
        self.assertEqual(len(result), 0)

    def test_invader_detected_once(self):
        # should be detected just once, since start and end index are passed
        detection_sample = ['--o-----o----o-----o--',
                            '---o---o------o---o---',
                            '--ooooooo----ooooooo--',
                            '-oo-ooo-oo--oo-ooo-oo-',
                            'oooooooooooooooooooooo',
                            'o-ooooooo-oo-ooooooo-o',
                            'o-o-----o-oo-o-----o-o',
                            '---oo-oo------oo-oo---']

        result = self.detector.detect_invader(self.invader_template, detection_sample, 0, 11, 1, 2)
        self.assertEqual(len(result), 1)

    def test_detect_indexes_approximate_match(self):
        radar_sample = '--o-----o----o-----o--'
        invader = Invader(['--o-----o--', '---o---o---'])

        result = {n for n in self.detector.detect_header_indexes(invader.head, radar_sample)}

        self.assertEqual(result, {0, 1, 2, 5, 6, 10})

    def test_detect_indexes_exact_match(self):
        radar_sample = '--o-----o--'
        invader = Invader(['--o-----o--', '---o---o---'])
        detector = Detector(chars_difference=0)

        result = {n for n in detector.detect_header_indexes(invader.head, radar_sample)}

        self.assertEqual(result, {0})

    def test_not_detect_indexes_not_exact_match(self):
        radar_sample = '--o-----o-o'
        invader = Invader(['--o-----o--', '---o---o---'])
        detector = Detector(chars_difference=0)

        result = {n for n in detector.detect_header_indexes(invader.head, radar_sample)}

        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
