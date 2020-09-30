import unittest
import work

class Resize(unittest.TestCase):

    def test_resize(self):
        [w , h] = work.resize(1024 , 786 , "w" , 300)
        self.assertEqual(w , 300)
        self.assertEqual(h , 230)

    def test_resize_2(self):
        [w, h] = work.resize(1920, 1080, "h", 540)
        self.assertEqual(w, 960)
        self.assertEqual(h, 540)

if __name__ == '__main__':
    unittest.main()
