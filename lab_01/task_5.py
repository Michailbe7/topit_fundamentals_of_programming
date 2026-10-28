researcher = input("Имя исследователя: ")
experiment = input("Название эксперимента: ")
runs = int(input("Количество запусков: "))
run_duration = float(input("Длительность одного запуска (с): "))
real_part = float(input("Действительная часть коэффициента: "))
imag_part = float(input("Мнимая часть коэффициента: "))

total_seconds = runs * run_duration
total_minutes = total_seconds / 60
coefficient = complex(real_part, imag_part)
squared_modulus = real_part**2 + imag_part**2
has_runs = bool(runs)

border = "=" * 40
print(border)
print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {researcher}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {squared_modulus:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print(border)

print(
    "Типы введённых значений:",
    type(researcher),
    type(experiment),
    type(runs),
    type(run_duration),
    type(real_part),
    type(imag_part),
)