# if elif else statement
age = int(input("Enter your age: "))
if age <= 16:
    print("you are child")
elif 17 <= age <= 21:
    print("you are adult")
else:
    print("you are seniour")
# for loops
flowers=("Rose","Lotus","water-lily")
for x in flowers:
    print(x)

#  break statement
for i in range(10):
    if i==5:
        break
    print(i)
# continue statement
for i in range(20):
    if i%2==0:
        continue
    print(i)
# pass statement
for i in range(10):
    if i == 5:
        pass 
    else:
     print(i)