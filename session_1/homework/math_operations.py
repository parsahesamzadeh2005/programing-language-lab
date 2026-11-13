num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# تبدیل رشته‌ها به عدد اعشاری
num1 = float(num1_str)
num2 = float(num2_str)

# انجام چهار عمل اصلی
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition:", addition)
print("Type of addition result:", type(addition))

print("Subtraction:", subtraction)
print("Type of subtraction result:", type(subtraction))

print("Multiplication:", multiplication)
print("Type of multiplication result:", type(multiplication))

print("Division:", division)
print("Type of division result:", type(division))