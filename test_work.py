import unittest
import work
import sys

param_origwh = sys.argv[1].split('x', 2)
param_check_value = sys.argv[2].split(':', 2)

width = int(param_origwh[0])
height = int(param_origwh[1])
check = param_check_value[0]
value = int(param_check_value[1])

class Resize(unittest.TestCase):
    if check == "w":
        def test_resize(self):
            [w , h] = work.resize(width, height, check, value) # 1024 , 786 , "w" , 300
            self.assertEqual(w , 300)
            self.assertEqual(h , 230)

    elif check == "h":
        def test_resize_2(self):
            [w, h] = work.resize(width, height, check, value) # 1920, 1080, "h", 540
            self.assertEqual(w, 960)
            self.assertEqual(h, 540)

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
