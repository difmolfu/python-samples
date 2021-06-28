num1 = int(input("type first number: "))
num2 = int(input("type second number: "))
num3 = int(input("type third number: "))

do = input("what action do you want to perform? +, -, *, / ? ")

# работаем с переменной и проверяем её значения (do)
if do == "+":
    print (num1 + num2 + num3)
elif do == "-":
    print (-num1 - num2 - num3)
elif do == "*":
     print (num1 * num2 * num3)
elif do == "/":
    print (num1 / num2 / num3)
else:
    print("Что-то введено неправильно")
  
