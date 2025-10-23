# TRPOCP_morugova
Технология разработки программного обеспечения цифровых продуктов Моругова МВ
## Новые функции в v1.1.0

### Геометрические функции
- `calculate_circle_area(radius)` - площадь круга
- `calculate_triangle_area(base, height)` - площадь треугольника

### Математические функции  
- `is_prime(number)` - проверка числа на простоту
- `is_even(number)` - проверка четности
- `factorial(n)` - факториал числа

## Использование

```python
from math_operations import *

# Базовые операции
result = add(5, 3)  # 8

# Геометрические функции
area = calculate_circle_area(5)  # ~78.54

# Математические функции
is_prime = is_prime(17)  # True
