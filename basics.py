
# Online Python - IDE, Editor, Compiler, Interpreter
'''
a = "My name is Sharon"
b = 123
print(a.upper())
print(a.replace("S", "J"))

if 2 > b:
     print("Y")
elif 1234 == b:
     print("N")
else:
    print("idk")
    
    
for x in a:
    print(x)

    
num = 20
while num > 10:
    print(num)
    if num == 16:
        break
    num-=1
else:
    print("Done")


for num in range((16, 9, -1)):
    print(num)
'''
print("Enter a no")
num = input()
if float(num) < 1:
    print(f"{num} is Less")
elif float(num) == 1:
    print(f"{num} is same as 1")
else:
    print(f"{num} is Great")