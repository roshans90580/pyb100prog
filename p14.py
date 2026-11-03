a = int(input("enter first no"))
b = int(input("enter sec no"))
c = int(input("enter third no"))
if a<b and a<c :
    print(f"{a} is smallest")
elif b<a and b<c :
    print(f"{b} is smallest")
else :
    print(f"{c} is smallest")