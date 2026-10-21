n = int(input("Введите количество измерений: "))

if n > 0:
    total_sum = 0.0

    for i in range(1, n + 1):
        value = float(input(f"Введите измерение #{i}: "))
        total_sum += value

    average = total_sum / n

    print("\n--- Результаты анализа ---")
    print(f"Сумма всех измерений: {total_sum}")
    print(f"Среднее арифметическое: {average}")
else:
    print("Количество измерений должно быть больше 0.")