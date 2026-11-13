number = int(input("Enter an integer number: "))

# بررسی زوج یا فرد بودن با عملگر باقی‌مانده
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# بررسی مثبت، منفی یا صفر بودن
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")