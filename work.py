def resize(orig_width, orig_height, check, value):
    width_percent = 100 # Пусть ширина = 100%
    height_percent = orig_height / (orig_width / width_percent)
    if check == "w":
        height = value / width_percent * height_percent
        return round(value) , round(height)
    elif check == "h":
        width = value / height_percent * width_percent
        return round(width) , round(value)


if __name__ == '__main__':
    print(resize(1920, 1080, "h", 540))

