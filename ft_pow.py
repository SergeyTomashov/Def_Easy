def ft_pow(number, pow_):
    res = 1
    if pow_ > 0:
        for i in range(pow_):
            res = res * number
        return res
    elif pow_ == 0:
        return 1
    elif pow_ < 0:
        for i in range(pow_ * -1):
            res = res * number
        return 1 / res
