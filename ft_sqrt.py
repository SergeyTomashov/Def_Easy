def ft_sqrt(number):
    if number < 0:
        return -1
    elif number == 0:
        return 0
    for i in range(number):
        if i * i == number:
            return i
    return -1
