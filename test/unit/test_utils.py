import tempfile
import unittest
from unittest.mock import call
from unittest.mock import patch

import utils


class TestUtils(unittest.TestCase):

    @patch('utils.logger')
    def test_invalid_radar_filename(self, mock_logger):

        with self.assertRaises(SystemExit) as sys_exit:
            utils.read_radar_file('')
            mock_logger.error.assert_called_with('File with radar data is not found! Exiting.')

            self.assertEqual(sys_exit.exception.code, 1)

    @patch('utils.logger')
    def test_invalid_invader_filename(self, mock_logger):

        with self.assertRaises(SystemExit) as sys_exit:
            utils.read_radar_file('')
            mock_logger.error.assert_called_with('File with invader templates is not found! Exiting.')

            self.assertEqual(sys_exit.exception.code, 1)

    def test_read_invader_file_with_wrong_separator(self):
        data = ['+++++', '----ooo-oo--oo', 'oo-oooo-o', '++++']

        tmp = tempfile.NamedTemporaryFile()

        with open(tmp.name, 'w') as f:
            for line in data:
                f.write(line)
                f.seek(0)

            result = utils.read_invader_file(tmp.name, '~~~~')

            self.assertEqual(result, [])

    def test_read_invader_file_with_correct_separator(self):
        data = ['++++++', 'oo-oooo--', 'oo-oooo-o', '++++++']

        tmp = tempfile.NamedTemporaryFile()

        with open(tmp.name, 'w') as f:
            for line in data:
                f.write(f'{line}\n')
                f.flush()

            result = utils.read_invader_file(tmp.name, '++++++')

            self.assertEqual(result, [['oo-oooo--', 'oo-oooo-o']])

    @patch('utils.logger')
    def test_present_invader_defined_logger_lever(self, mock_logger):
        utils.present_invader([''], 'warn')

        mock_logger.warning.assert_called()

    @patch('utils.logger')
    @patch('utils.present_invader')
    def test_present_result(self, mock_present_invader, mock_logger):
        expected_calls = [call('Invader detected!'),
                          call('starting_line: 2, ending_line: 3. starting_index 25, ending_index: 34')]

        utils.present_results({'invader': ['invader data'], 'starting_line': 1, 'ending_line': 2, 'starting_index': 25,
                               'ending_index': 34})

        mock_logger.info.assert_has_calls(expected_calls)
        mock_present_invader.asser_called_with(['invader data'])


if __name__ == '__main__':
    unittest.main()
