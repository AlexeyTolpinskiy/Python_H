def pow(x, y):
    y_1 = abs(y)
    while y_1 != 0:
        if y_1 == 1:
            print(1 / x)
            break
        else:
            x_1 = x * x
            y_1 -= 1
        print(1 / x_1)

pow(10, -2)