def ft_str(number1, number2, number3):
    if number1 <= 0 or number2 <= 0 or number3 <= 0 or \
            number1 >= number2 + number3 or \
            number2 >= number1 + number3 or \
            number3 >= number1 + number2:
        return -1
    p = (number1 + number2 + number3) / 2
    res = (p * (p - number1) * (p - number2) * (p - number3)) ** 0.5
    return res
