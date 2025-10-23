"""Математические функции для тестирования"""

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def power(base, exponent):
    """Возведение в степень"""
    return base ** exponent
def calculate_circle_area(radius):
    """Вычисление площади круга"""
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 3.14159 * radius ** 2

def calculate_triangle_area(base, height):
    """Вычисление площади треугольника"""
    if base < 0 or height < 0:
        raise ValueError("Основание и высота не могут быть отрицательными")
    return 0.5 * base * height

def is_prime(number):
    """Проверка числа на простоту"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
