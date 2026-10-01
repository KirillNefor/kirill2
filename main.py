# main.py - Простой калькулятор
def main():
    print("Калькулятор запущен")

if __name__ == "__main__":
    main()
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
def menu():
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    return input("Выберите операцию: ")
def main():
    print("=== Калькулятор ===")
    choice = menu()
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    
    if choice == '1':
        print(f"Результат: {add(a, b)}")
    elif choice == '2':
        print(f"Результат: {subtract(a, b)}")
    elif choice == '3':
        print(f"Результат: {multiply(a, b)}")
    elif choice == '4':
        print(f"Результат: {divide(a, b)}")
    else:
        print("Неверный выбор")
