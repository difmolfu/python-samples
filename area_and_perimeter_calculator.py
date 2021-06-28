p=int(input ("type length  "))
s=int(input ("type width  "))
do=input ("do you want to calculate the area or perimeter?  ")

if do == "area":
    print (p * s)
elif do == "perimeter":
    print ((p + s) * 2)

k=input("press close to exit") 