#!/usr/bin/env python3
"""Unit-тесты для математических функций"""

import math_operations

def test_add():
    """Тестирование функции сложения"""
    print("Тестируем сложение...")
    assert math_operations.add(2, 3) == 5, "2 + 3 должно быть 5"
    assert math_operations.add(-1, 1) == 0, "-1 + 1 должно быть 0"
    assert math_operations.add(0, 0) == 0, "0 + 0 должно быть 0"
    print("Сложение работает корректно")

def test_subtract():
    """Тестирование функции вычитания"""
    print("Тестируем вычитание...")
    assert math_operations.subtract(5, 3) == 2, "5 - 3 должно быть 2"
    assert math_operations.subtract(10, 10) == 0, "10 - 10 должно быть 0"
    assert math_operations.subtract(0, 5) == -5, "0 - 5 должно быть -5"
    print("Вычитание работает корректно")

def test_multiply():
    """Тестирование функции умножения"""
    print("Тестируем умножение...")
    assert math_operations.multiply(2, 4) == 8, "2 * 4 должно быть 8"
    assert math_operations.multiply(0, 100) == 0, "0 * 100 должно быть 0"
    assert math_operations.multiply(-2, 3) == -6, "-2 * 3 должно быть -6"
    print("Умножение работает корректно")

def test_divide():
    """Тестирование функции деления"""
    print("Тестируем деление...")
    assert math_operations.divide(10, 2) == 5, "10 / 2 должно быть 5"
    assert math_operations.divide(9, 3) == 3, "9 / 3 должно быть 3"
    
    # Тестируем деление на ноль
    try:
        math_operations.divide(5, 0)
        assert False, "Делитель 0 должен вызывать ошибку"
    except ValueError as e:
        assert str(e) == "Деление на ноль невозможно", "Неверное сообщение об ошибке"
    print("Деление работает корректно")

def test_power():
    """Тестирование функции возведения в степень"""
    print("Тестируем возведение в степень...")
    assert math_operations.power(2, 3) == 8, "2^3 должно быть 8"
    assert math_operations.power(5, 0) == 1, "5^0 должно быть 1"
    assert math_operations.power(3, 2) == 9, "3^2 должно быть 9"
    print("Возведение в степень работает корректно")

def run_unit_tests():
    """Запуск всех unit-тестов"""
    print("=== ЗАПУСК UNIT-ТЕСТОВ ===")
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_power()
    print("ВСЕ UNIT-ТЕСТЫ ПРОЙДЕНЫ!")

if __name__ == "__main__":
    run_unit_tests()
