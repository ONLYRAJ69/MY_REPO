x=float(input("enter ur first number"))
print("x=",x)
y=float(input("enterur second number"))
print("y=",y)
print('''choice 1=addition/n
      choice 2=substraction/n
      choice 3=multipication/n
      choice 4=division''')
z=input("enter ur choice")
print("z=",z)

if(z=='1'):
    print("The addition is",x+y)
elif(z=='2'):
    print("The substraction is",x-y)
elif(z=='3'):
    print("The multipication is",x*y)
elif(z<='4'):
    print("The division is",x/y)

else:
    print("Wrong choice entered")



