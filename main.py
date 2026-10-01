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
