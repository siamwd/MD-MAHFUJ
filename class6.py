# # set
# thisset={"apple","banana","cherry"}

# print(thisset)
# # for loop
# thisset={"apple","banana","cherry"}
# for x in thisset:
#     print(x)

# # true false
# thisset={"apple","banana","cherry"}
# print("banana" in thisset)
# print("banana" not in thisset)
# add
# thisset={"apple","banana","cherry"} 
# thisset .add("orange")
# print(thisset)
# append
thisset={"apple","banana","cherry"}
mylist=["kiwi","orange"]
thisset.update(mylist)
print(thisset)
# remove
# thisset={"apple","banana","cherry"}
# thisset.remove("banana")
# print(thisset)
# # pop
# thisset={"apple","banana","cherry"}
# thisset.pop()
# print(thisset)
# # clear
# thisset={"apple","banana","cherry"}
# thisset.clear()
# print(thisset)
# # delete
# thisset={"apple","banana","cherry"}
# thisset.delete()
# print(thisset)
# union
x={"apple","banana","cherry"}
y={"banana","orange"}
z=x|y
print(z)
# difference
x={"apple","banana","cherry"}
y={"banana","orange"}
myset=x-y
print(myset)