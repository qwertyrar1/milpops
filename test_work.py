import unittest


def width():
    width = int(input())
    return width
#width == orig_width

def height():
    height = int(input())
    return height
#height == orig_height

class ResizeOrientationTestCase(unittest.TestCase):

    def test_orientation_vertical(self):
        self.assertLess(width(), height() , msg="Вериткальная картинка")

    def test_orientation_horizont(self):
        self.assertGreater(width() , height() , msg="Горизонтальная картинка")

if __name__ == '__main__':
    unittest.main()
