import unittest
import work
from work import width
from work import height

class ResizeOrientationTestCase(unittest.TestCase):

    def test_orientation_vertical(self):
        self.assertLess(work.orig_width, work.orig_height , msg="Это горизонтальная картинка")

    def test_orientation_horizont(self):
        self.assertGreater(work.orig_width , work.orig_height , msg="Это вертикальная картинка")

if __name__ == '__main__':
    unittest.main()
