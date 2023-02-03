from unittest import TestCase
import utils


class tests(TestCase):

    def test_id_length(self):
        expected_length = 8
        actual_length = len(utils.generate_id())

        self.assertEqual(actual_length, expected_length)

    def test_config_load(self):
        expected_type = dict

        actual_type = type(utils.load_config("config.json"))

        self.assertEqual(actual_type, expected_type)


test_to_run = tests()
test_to_run.test_id_length()
test_to_run.test_config_load()
