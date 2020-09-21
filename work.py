import unittest

print("Введите исходные размеры изображения")
orig_width = int(input())
orig_height = int(input())

def resize():

    width_percent = 100 # Пусть ширина = 100%
    height_percent = orig_height / (orig_width / width_percent)
    print("Изменить по высоте или ширине?h/w")
    check = str(input())

    if check != "h" and check != "w":
        return "Данные введены неверно!"
    elif check == "w":
        print("Введите новую ширину")
        w_width = int(input())
        w_height = w_width / width_percent * height_percent
        return round(w_width) , round(w_height)
    elif check == "h":
        print("Введите новую высоту")
        h_height = int(input())
        h_width = h_height / height_percent * width_percent
        return round(h_width) , round(h_height)
11


print(resize())


class ResizeOrientationTestCase(unittest.TestCase):

    def test_orientation(self):
        self.assertLessEqual(orig_width, orig_height, msg=" горизонтальная картинкаs")

    def test_orientation_horizont(self):
        self.assertGreaterEqual(orig_width, orig_height, msg="вертикальная картинка")


