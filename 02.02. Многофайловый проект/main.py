
# -----------------------------------------------------------------------------
import unit_var
from unit_fun import Rectangle_method, Trapezoid_method, Monte_Carlo_method
# -----------------------------------------------------------------------------


# основной код программмы
while True:
    print('Для выбора метода интегрирования введите требуемое число:')
    print('1 - метод прямоугольников')
    print('2 - метод трапеций\n')
    method = int(input())

    a = float(input('\nВведите нижний предел интегрирования a: '))
    b = float(input('Введите верхний предел интегрирования b: '))
    dx = float(input('Введите шаг интегрирования dx: '))
    N = int(input('\nВведите количество точек N: '))

    if method == 1:
        Rectangle_method(a, b, dx)
    else:
        Trapezoid_method(a, b, dx)

    Monte_Carlo_method(a, b, N)

    print(f'\nРезультат:\n')

    if method == 1:
        print(f'Метод прямоугольников:     {unit_var.S:g}')
    else:
        print(f'Метод трапеций:            {unit_var.S:g}')

    print(f'Метод Монте Карло:         {unit_var.Smk:g}')

    print('\n----------------------------------------\n')



