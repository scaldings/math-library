import string
import random
pi = 22/7


def degrees_to_radians(degrees: int):
    return pi * degrees / 180


def radians_to_degrees(radians: int):
    return radians * 180 / (22 / 7)


def trapezoid_area(base1: float, base2: float, height: float):
    return (base1 + base2) * height / 2


def parallelogram_area(base: float, height: float):
    return base * height


def cylinder_surface_area(radius: float, height: float):
    return pi * pwr(radius, 2) + 2 * pi * radius * height


def cylinder_volume(radius: float, height: float):
    return pi * pwr(radius, 2) * height


def sphere_surface_area(radius: float):
    return 4 * pi * radius


def sphere_volume(radius: float):
    return 4 / 3 * pi * pwr(radius, 3)


def arc_length(radius: float, degrees: int):
    return 2 * pi * radius / 360 * degrees


def sector_area(radius: float, degrees: int):
    return pi * pwr(radius, 2) / 360 * degrees


def discriminant(a: float, b: float, c: float):
    return pwr(b, 2) - 4 * a * c


def discriminant_solutions(a: float, b: float, c: float):
    discriminant1, result = discriminant(a, b, c), 0
    if discriminant1 > 0:
        result = 2
    if discriminant1 == 0:
        result = 1
    if discriminant1 < 0:
        result = 0
    return result


def proper_divisors(n: int):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def proper_divisor_sum(n: int):
    divisor_sum = 0
    for i in proper_divisors(n):
        divisor_sum += i
    return divisor_sum


def is_abundant(n: int):
    factor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            factor_sum += i
    return factor_sum > n


def are_amicable(a: int, b: int):
    return proper_divisor_sum(a) == proper_divisor_sum(b)


def is_prime(n: int):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return len(divisors) == 2


def in_fibonacci_sequence(n: int):
    fibonacci_sequence_array = [0, 1]
    a, x = 0, 1
    for y in range(0, n):
        fibonacci_sequence_array.append(a + x)
        a, x = x, fibonacci_sequence_array[len(fibonacci_sequence_array) - 1]
    if n in fibonacci_sequence_array:
        return True
    else:
        return False


def pwr(a: float, b: float):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return a ** b


def root(a: int, b: float):
    divisors = proper_divisors(a)
    for x in divisors:
        if pwr(x, b) == a:
            return x


def possible_powers(a: int):
    possible_pwrs = [[a, 1]]
    for x in range(a):
        for y in range(a):
            if pwr(x, y) == a:
                possible_pwrs.append([x, y])
    return possible_pwrs


def generate_password(length: int):
    characters, password = list(string.ascii_letters + '0123456789'), ''
    for i in range(length):
        random_int = random.randint(0, len(characters) - 1)
        password += characters[random_int]
    return password
