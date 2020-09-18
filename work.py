print("Введите исходные размеры изображения")
width = int(input())
height = int(input())
width_percent = 100 # Пусть ширина = 100%
height_percent = height / (width / width_percent)
print("Введите то что хотите найти,h-высоту,w-ширину")
check = str(input())
if check != "h" and check != "w":
    print("Данные введены неверно!")
elif check == "h":
    print("Введите новую ширину")
    h_width = int(input())
    h_height = h_width / width_percent * height_percent
    print("Высота:")
    print(round(h_height))
elif check == "w":
    print("Введите новую высоту")
    w_height = int(input())
    w_width = w_height / height_percent * width_percent
    print("Ширина:")
    print(round(w_width))


