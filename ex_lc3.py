number = int(input("Number: "))


def reverse_number_minus(number: int) -> int:
    """
    Функция возвращает перевернутое число, как с минусом, так и без него
    """
    if number < 0:
        number_str = str(number)
        new_number_str = ''
        for item in range(len(number_str)-1, -1, -1):
            new_number_str += number_str[item]
        new_number_str = new_number_str[0:len(new_number_str)-1]
        new_number_int = int(new_number_str)
        new_number_int *= -1
        return new_number_int
    else:
        number_str = str(number)
        new_number_str = ''
        for item in range(len(number_str) - 1, -1, -1):
            new_number_str += number_str[item]
        new_number_int = int(new_number_str)
        return new_number_int


print(reverse_number_minus(number))