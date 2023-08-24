# ТЕМА: Робота зі строками та тип даних integer(ціле число)

# Робота із цілими числами.

# Сумування чисел
# # "+" це оператор для сумування чисел;
# print(100 + 200)
# # "-" це оператор для віднімання чисел;
# print(500 - 400)
# # "*" це оператор для множення чисел;
# print(25 * 5)
# # "/" це оператор для ділення чисел;
# print(100 / 5)

# Зберігання чисел в змінних
# number1 = 100
# number2 = 150
# print(number1 + number2)
# result = number1 + number2
# print(result)

# Піднесення до степені, використовуємо "**"
# result = 5 ** 2
# print(result)

# Робота зі дробними числами
# Приклад: 0.5, 100.50, 5.125, 3.2
# Взаємодія з дробними числами проходить так само як із цілими числами
# print(0.5 + 2.6)
# Будь-яка взаємодія дробного та цілого числа виводить дробне число
# print(2.5 - 0.5)
# Дробні числа в Python називаються float
# float - це числовий тип даних в Python

# Робота зі строками
# age = 19
# text = "I am " + str(age) + " years old."
# print(text)
# str() - команда для перетворення даних в строку

# Форматування строк
# Варіант 1 (f строка)
# name = "John"
# text = f"My name is {name}"
# print(text)
# age = 25
# text2 = f"I am {age} years old"
# print(text2)

# Варіант 2 (метод formating)
# age = 30
# text = "i am {} years old".format(age)
# print(text)
# name = "Askar"
# text2 = "i am {}. I am {} years old".format(name, age)
# print(text2)

# Зріз строк
# Строки мають індекс. Позитивні та від'ємні
# product = "Apple"
# print(product[0])
# print(product[-1])
# print(product[4])

# Pineapple
# product = "Pineapple"
# print(product[0]+product[3]+product[2])
# print(product[4:9])

# Завдання 1
# Отримати через input ім'я користувача та прізвище користувача.
# Вивести на екран привітання з першою літерою прізвища та ім'я повністю.

# last_name = input("Введіть Ваше імя: ")
# first_name = input("Введіть Ваше прізвище: ")
# full_name = f"Вітаю {first_name[0]}. {last_name}"
# print(full_name)

# Завдання 2
# Існує змінна із хаотичними словами. Із допомогою зрізу скласти із них речення.
text = "like I football play"
print(text[5]+text[0:3]+text[7:14]+text[16:20])






















