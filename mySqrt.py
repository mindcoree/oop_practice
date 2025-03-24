def mySqrt(x: int) -> int:
    if x == 0:
        return 0

    left, right = 0, x
    while right >= left:
        sqrt_number = (left + right) // 2
        if sqrt_number * sqrt_number == x:
            return sqrt_number
        elif sqrt_number * sqrt_number > x:
            right = sqrt_number - 1
        else:
            left = sqrt_number + 1

    return right

pick = int(input(f"Введите число "))
print(f"Квадрат округленного числа {pick}: {mySqrt(pick)}")