def ft_rev_num(a_):
    if a_ >= 0:
        n1 = a_ // 100
        n2 = a_ // 10 % 10
        n3 = a_ % 10
        return n3 * 100 + n2 * 10 + n1
    else:
        res_ = a_ * -1
        n_1 = res_ // 100
        n_2 = res_ // 10 % 10
        n_3 = res_ % 10
        res__ = (n_3 * 100 + n_2 * 10 + n_1) * -1
        return res__
