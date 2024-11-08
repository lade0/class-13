# calculator using function
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
print("please select the operation")
print("please enter a for addition,b for subtraction,c for multiplication and d for division")
choice=input("please enter your choice:")
num1=int(input("please enter the first number:"))
num2=int(input("please enter the second number:"))
if choice=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",mult(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("your input was not valid ")