import sys

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3
    except:
        print("AssertionError")
        print("Usage: program [number_width]x[number_height] [w|h]:[new_value]")
        sys.exit()

param_origwh = sys.argv[1].split('x', 2)
param_check_value = sys.argv[2].split(':', 2)

width = int(param_origwh[0])
height = int(param_origwh[1])
check = param_check_value[0]
value = int(param_check_value[1])

def resize(width, height, check, value):
    width = int(param_origwh[0])
    height = int(param_origwh[1])
    check = param_check_value[0]
    value = int(param_check_value[1])

    width_percent = 100  # Пусть ширина = 100%
    height_percent = height / (width / width_percent)

    if check == "w":
        new_height = value / width_percent * height_percent
        return round(value), round(new_height)
    elif param_check_value[0] == "h":
        new_width = value / height_percent * width_percent
        return round(new_width), round(value)


def parse_args():
    try:
        assert int(param_origwh[0]) > 0
        assert int(param_origwh[1]) > 0
        assert param_check_value[0] == 'w' or 'h'
        assert int(param_check_value[1]) > 0
        assert len(sys.argv) == 3
    except:
        return print("AssertionError" , "\nUsage: program [number_width]x[number_height] [w|h]:[new_value]")
    else:
        return resize(width, height, check, value)

if __name__ == '__main__':
    print(parse_args())


