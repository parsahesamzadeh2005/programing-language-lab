age = int(input("Enter your age: "))

# تعیین قیمت بلیط بر اساس سن
if age < 5:
    print("Free")
elif age < 18:
    print("50000 Toman")
elif age < 60:
    print("100000 Toman")
else:
    print("70000 Toman")