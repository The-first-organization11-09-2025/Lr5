from ЛР3 import bubble_sort, selections_sort, insertion_sort

def test_bubble_sort():
    a = [1,4,3,6,2]
    b = [1,2,3,4,6]
    assert bubble_sort(a) == b


def test_selections_sort():
    a = [1,2,4,3,5]
    b = [1,2,3,4,5]
    assert selections_sort(a) == b


def test_insert_sort():
    a = [3,2,6,4,8]
    b = [2,3,4,6,8]
    assert insertion_sort(a) == b


# Перевод числа в двоичную систему
def numbber_conversion(digit):
    print(digit)
    rest = ''
    while digit > 0:
        rest = str(digit % 2) + rest
        digit = digit // 2
    return int(rest)

print(numbber_conversion(8))


def test_number_conversion():
    assert numbber_conversion(8) == 1000


# Определение вида треугольника, зная его стороны
def triangle(a,b,c):
    number = [a,b,c]
    m = max(number)
    number.remove(m)
    if m < number[0] + number[1]:
        if m ** 2 == number[0] ** 2 + number[1] ** 2:
            ans = "Прямоуголный треугольник"
        elif m ** 2 < number[0] ** 2 + number[1] ** 2:
            ans = "Остроугольный треугольник"
        else:
            ans = "Тупоугольный треугольник"
    else:
        ans = "Треугольника не существует"
    return ans


def test_triangle():
    assert triangle(1,2,10) == "Треугольника не существует"
    assert triangle(3,4,5) ==  "Прямоуголный треугольник"
    assert triangle(7,8,9) == "Остроугольный треугольник"
    assert triangle(3,4,6) == "Тупоугольный треугольник"
    assert triangle(10,1,2) == "Треугольника не существует"


# Имеет ли квадратное уравнение решение, зная коэф.
def decision(a,b,c):
    if (b ** 2) - (4*a*c) >= 0:
        answ = "Корни есть"
    else:
        answ = "Корней нет"
    return answ


def test_decision():
    assert decision(1,0,3) == "Корней нет"
    assert decision(1,-4,4) == "Корни есть"


# Факториал числа
def factorial(a):
    answer = 1
    i = 1
    while i <= a:
        answer *= i
        i += 1
    return answer


def test_factorial():
    factorial(4) == 24


# Количество буквы а в предложении
def count_a(sentence):
    count = 0
    for char in sentence.lower():
        if char == 'а':
            count += 1
    return count


def test_count_a():
    count_a("Аккомпанемент — это музыкальное сопровождение к сольной партии голоса или инструмента, а также к основной теме, мелодии музыкального произведения") == 9