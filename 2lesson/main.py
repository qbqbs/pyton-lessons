def get_imt(weight, height):
    weight = 80
    height = 1.9

    imt = 80 / (height * height)

    print(imt)

    if  imt < 19:
        print("у вас недовес")
    elif imt > 25:
        print("у вас перевес")
    else:
        print("ваш вес в норме")

get_imt(100, 1.8)