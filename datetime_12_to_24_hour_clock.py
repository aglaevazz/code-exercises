# python3
# this programmes converts a 12-hour-clock format into a 24-hour-format
# p.e.: input = "10:10 PM", output "22:10"

import unittest


def convert_12_to_24_hour_format(am_pm_string):
    hour_12_string = am_pm_string[:-2]
    am_pm = am_pm_string[-2:]
    if am_pm == 'AM':
        if hour_12_string[:2] == '12':
            return '00' + hour_12_string[2:]
        return hour_12_string
    if hour_12_string[:2] == '12':
        return hour_12_string
    return str(int(hour_12_string[:2]) + 12) + hour_12_string[2:]


class Unittest(unittest.TestCase):

    def test_convert_12_to_24_hour_format(self):
        am_pm_string = '12:12:12AM'
        hour_12_string = '00:12:12'
        self.assertEqual(convert_12_to_24_hour_format(am_pm_string), hour_12_string)
        am_pm_string = '06:34:41AM'
        hour_12_string = '06:34:41'
        self.assertEqual(convert_12_to_24_hour_format(am_pm_string), hour_12_string)
        am_pm_string = '12:24:50PM'
        hour_12_string = '12:24:50'
        self.assertEqual(convert_12_to_24_hour_format(am_pm_string), hour_12_string)
        am_pm_string = '05:05:07PM'
        hour_12_string = '17:05:07'
        self.assertEqual(convert_12_to_24_hour_format(am_pm_string), hour_12_string)


if __name__ == '__main__':
    unittest.main()
