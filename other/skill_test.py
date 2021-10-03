def right(int_list):
    return [i % 10 for i in int_list]


def addstar(str_list):
    return [i + '*' for i in str_list]


def multi_lower(str_list):
    return [i.lower() for i in str_list]


def multiply(str_list):
    return [i*3 for i in str_list]


if __name__ == '__main__':
    print(right([1, 22, 94]))
    print(right([10, 0]))

    print(addstar(["a", "hello", "hai", "*"]))

    print(multi_lower(["Choc"]))

    print(multiply(["a", "bb"]))
