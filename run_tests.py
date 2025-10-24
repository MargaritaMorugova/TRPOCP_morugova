#!/usr/bin/env python3
"""Главный скрипт для запуска всех тестов"""

import sys
import test_unit
import test_integration

def main():
    """Запуск всех тестов"""
    print("ЗАПУСК ВСЕХ ТЕСТОВ")
    print("=" * 50)
    
    try:
        # Запускаем unit-тесты
        test_unit.run_unit_tests()
        print()
        
        # Запускаем интеграционные тесты
        test_integration.run_integration_tests()
        print()
        
        # Финальное сообщение
        print("=" * 50)
        print("ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
        print("Unit-тесты: пройдены")
        print("Интеграционные тесты: пройдены")
        print("Проект готов к использованию!")
        print("=" * 50)
        
    except Exception as e:
        print(f" ТЕСТИРОВАНИЕ ПРОВАЛЕНО: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
