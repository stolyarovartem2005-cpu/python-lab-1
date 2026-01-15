def read_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Помилка: потрібно ввести ціле число (наприклад: 10). Спробуйте ще раз.")

def read_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("Помилка: потрібно ввести число (наприклад: 2.5). Спробуйте ще раз.")

a = read_int("Введіть ціле число a: ")
b = read_int("Введіть ціле число b: ")
x = read_float("Введіть дробове число x: ")
y = read_float("Введіть дробове число y: ")

print("\nВи ввели:")
print(f"a = {a}, b = {b}, x = {x}, y = {y}")

results = []

results.append(a + b)
results.append(a - b)
results.append(a * b)

if b != 0:
    results.append(a / b)
    results.append(a // b)
    results.append(a % b)
else:
    results.append("Неможливо: ділення на нуль")
    results.append("Неможливо: цілочисленне ділення на 0")
    results.append("Неможливо: остача від ділення на 0")

results.append(a ** b)

print("\nСписок результатів (Завдання 2):")
print(results)

print("\nЗавдання 3:")
print(f"Кількість елементів у списку results: {len(results)}")

print("Парні елементи списку (ті, що є цілими числами і парні):")
for item in results:
    if isinstance(item, int) and item % 2 == 0:
        print(item)

print("\nЗавдання 4:")
if len(results) >= 5:
    results[1], results[4] = results[4], results[1]
    print("Список після заміни 2-го і 5-го елементів:")
    print(results)
else:
    print("Список має менше ніж 5 елементів, заміна неможлива.")

name = input("\nВведіть ваше прізвище та ім’я: ").strip()

print("\nЗавдання 5:")
print("Виконавець лабораторної роботи №1:")
print(name)
print("Висновки:")
print("1) Ознайомився з введенням даних через input та приведенням типів int/float.")
print("2) Виконав базові арифметичні операції та зберіг результати у список.")
print("3) Навчився працювати зі списками: визначати довжину, знаходити парні елементи, міняти елементи місцями.")
