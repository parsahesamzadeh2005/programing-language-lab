
price = int(input("Enter product price: "))

rank = input("Enter your rank (gold/silver): ")
d=0

if rank:
    if rank == "gold":
        if price > 10000:
            discount = 30
        else :
            discount = 20

    elif rank == "silver":
        if price > 10000:
            discount = 20
        else :
            discount = 10

elif price > 10000:
    discount = 10
    print("You got Silver tier discount!")


else:
    discount = 0

final_price = price - (price * discount / 100)

print("Discount:", discount, "%")
print("Final price:", final_price)
