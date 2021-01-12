# python 3
# this program rounds grades

import unittest


def round_grades(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38 and grade != 100:
            if str(grade)[1] in ['3', '4']:
                grade = int(str(grade)[0] + '5')
            elif str(grade)[1] in ['8', '9']:
                grade = int(str(grade)[0] + '0') + 10
        rounded_grades.append(grade)
    return rounded_grades


class TestRoundGrades(unittest.TestCase):

    def test_round_grades(self):
        grades = [0, 12, 37, 38, 39, 50, 72, 91, 87, 100]
        rounded_grades = [0, 12, 37, 40, 40, 50, 72, 91, 87, 100]
        self.assertEqual(round_grades(grades), rounded_grades)


if __name__ == '__main__':
    unittest.main()
