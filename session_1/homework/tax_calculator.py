salary = float(input("Enter your monthly salary: "))

# محاسبه مالیات ثابت ۱۰ درصد
tax = salary * 0.10

# محاسبه حقوق خالص بعد از کسر مالیات
net_salary = salary - tax

print("Tax amount:", tax)

print("Net salary:", net_salary)