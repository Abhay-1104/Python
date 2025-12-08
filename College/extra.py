# a=8
# b=9.5
# c=4+2j
# d=True
# e="Abhay"

# print(a+b,c)
# print(type(a),type(b),type(c),type(d),type(e),sep=" | ")
# print(id(a))
# for i in range(0,6,2):
#     print(i)
#=============================

# n1=4
# n2=3
# print(n1+n2,abs(n2-n1),n1*n2,n1/n2,n1//n2,n1**n2,n1^n2,n1>>n2,n1<<n2,sep=" | ")
# print("Sum id %d",n1+n2)

#==============================
# for ch in "python":
#     print(ch,end=" ")

#==============================

# f=open("file.txt","w")
# s="Today is Python lab exam"
# f.write(s)
# f.close()

# f=open("file.txt","r")
# content=f.read()
# print(content)
# f.close()

# f1 = open("file.txt", "r")
# data = f1.read()
# f1.close()

# f2 = open("file2.txt", "w")
# f2.write(data)
# f2.close()

# f3 = open("file.txt", "r")
# s = f3.read()
# print(s)
# f1.close()


# l1=list("Hello")
# print(l1)

# squares = [i*i for i in range(1, 6)]
# print(squares)    

# evens = [x for x in range(0, 9) if x % 2 == 0]
# print(evens)      

#========================
d = {"name": "Abhay", "branch": "IoT", "sem": 2}

print(dict(d))           # creates another dict
print(len(d))            # number of key-value pairs

print(d.get("name"))     # Abhay (safe, no error)
print(d.get("xyz"))      # None

removed = d.pop("sem")   # removes 'sem'
print(removed)
print(d)

d.clear()                # empty dictionary
print(d)                 # {}
