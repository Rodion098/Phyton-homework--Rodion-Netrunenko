# ДЗ 2. Умовні вирази. Вправа №1
# Програма зчитує число, вирішує в які рамки воно підпадає та повідомляє про це користувача. Рамки:
#
#   Число дорівнює або менше ніж -500
#   Дорівнює або менше ніж -100, але більше -500
#   Менше ніж 0, але більше -100
#   Дорівнює або більше ніж 0, але менше 100
#   Дорівнює або більше ніж 100, але менше 500
#   Дорівнює або більше ніж 500

user_number = float(input("Enter your number: "))
if user_number <= -500:
 print("You entered the top 6")
elif user_number <= -100 and user_number > -500:
 print("You entered the top 5")
elif user_number < 0 and user_number > -100:
 print("You entered the top 4")
elif user_number >= 0 and user_number < 100:
 print("You entered the top 3")
elif user_number >= 100 and user_number < 500:
 print("You entered the top 2")
elif user_number >= 500:
 print("You entered the top 1")
else:
 print("You got nowhere")















