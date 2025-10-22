#!/usr/bin/env python3
"""Интеграционные тесты для математических функций"""

import math_operations

def test_complex_calculation():
    """Тестирование комплексных вычислений"""
    print("🔄 Тестируем комплексные вычисления...")
    # (10 + 5) * (8 - 8/4) = 15 * 6 = 90
    result = math_operations.multiply(
        math_operations.add(10, 5),
        math_operations.subtract(8, math_operations.divide(8, 4))
    )
    assert result == 90, f"Ожидалось 90, получено {result}"
    print("✅ Комплексные вычисления работают")

def test_operation_sequence():
    """Тестирование последовательности операций"""
    print("🔄 Тестируем последовательность операций...")
    # ((5 + 3) * 2 - 4) / 3 = 4
    step1 = math_operations.add(5, 3)        # 8
    step2 = math_operations.multiply(step1, 2)  # 16
    step3 = math_operations.subtract(step2, 4)  # 12
    step4 = math_operations.divide(step3, 3)    # 4
    
    assert step4 == 4, f"Ожидалось 4, получено {step4}"
    print("✅ Последовательность операций работает")

def run_integration_tests():
    """Запуск всех интеграционных тестов"""
    print("=== ЗАПУСК ИНТЕГРАЦИОННЫХ ТЕСТОВ ===")
    test_complex_calculation()
    test_operation_sequence()
    print("🎉 ВСЕ ИНТЕГРАЦИОННЫЕ ТЕСТЫ ПРОЙДЕНЫ!")

if __name__ == "__main__":
    run_integration_tests()
