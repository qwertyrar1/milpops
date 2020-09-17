print("Исходнй размер изображения 1024x600")
print("Введите то что хотите найти,h-высоту,w-ширину")
check = str(input())
if check != "h" and check != "w":
    print("Данные введены неверно!")
elif check == "h":
    print("Введите новую ширину")
    h_width = int(input())
    h_height = h_width / 100 * 58.6
    print("Высота:")
    print(round(h_height))
elif check == "w":
    print("Введите новую высоту")
    w_height = int(input())
    w_width = w_height / 58.6 * 100
    print("Ширина:")
    print(round(w_width))


