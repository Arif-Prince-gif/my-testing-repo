num = -7
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


age = 17
if age >= 18:
    print("You can vote!")
else:
    years = 18 - age
    print("Wait", years, "more year(s)")

workers = 200
if workers >= 188:
    print ("few pepole only leave")
else :
    leave = workers - 20
    print (leave, "nothing else")

   
n = int(input("Enter your age:" ))

if n % 2 == 0:
    print(n, "is Even")
else:
    print(n, "is odd")

a, b, c = map(int, input("Enter 3 numbers:" ).split ())
print ("number:" , a, b, c)
print("sum:" ,a+b+c)
