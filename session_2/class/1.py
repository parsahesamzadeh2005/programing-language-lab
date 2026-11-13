score = float(input("what is your sccore? "))
if score>=0 and score<=20:
    if score >= 18 :
        print('well done nimboos!')
    elif score >= 15 :
        print('your sccore is around B')
    elif score >= 10 :
        print ("نیاز به تلاش بیشتر")
    else :
        print (f"please enseraf da!  {score}")
else:
    print("its not in range")