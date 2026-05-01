fact =1
for i in range (1,6):
    fact *=i
    print("5!= ", fact)
# print("5!= ", fact)


print("mohammedarif".upper())
print("MOHAMMEDARIF".lower())
print("mohammed arif".title())
print("mohammed arif".capitalize())
print(" hi  ".strip())
print("hi bye!".replace("hi","hello"))
print("a,b,c".split(","))
print ("-".join(["a","b"]))
print("hello".find("e"))
print("hello".index("e"))
print("hello".count("1"))
print("hello".startswith("r"))
print("hello".endswith("o"))
print("13w4".isdigit())
print("qwe".isalpha())
print("1234".isalnum())
print("23".zfill(9))
print("hi".center(10,"-"))
print("hi".encode())

s= "hello world"
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())


q="python is easy to learn"
print(q.title())
print(q.find("to"))
print(q.replace("python", "java"))





csv= "Ravi,Kumar,Priya,Siva,Mala"
names = csv.split(",")
print(names)
print(len(names))
print(" | ".join(names))


a= "Error2Experts"
print(a.center(30,"*"))
print(a.ljust(25,"-"))
print(a.rjust(25,"-"))
print("42".zfill(8))


#Practice
user = (input("Enter your Name"))
print(user.upper())
print(user.title())
print(user.swapcase())



#Practice

user = (input("Enter your Name"))
print(user.count("our"))


#Practice
arun=('arun@gmail.com')
anu=('anu@eurogriptyres.com')

if arun .endswith("@gmail.com"):
    print("Vaild")
if anu .endswith("@eurogriptyres.com"):
    print("Not Valid")
else:
    print("Invaild")


#Practice

print("34" .zfill(8)) , print("34" .isdigit())

































