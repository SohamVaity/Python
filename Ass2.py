# arithmetic operator
a=10
b=5
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Mod: ",a%b)
print("Floor Division: ",a//b)
print("Exponentation: ",a**b)

# assignment operator
a=10
a+=2
print("+=",a)
a=10 ; 
a-=2
print("-=",a)
a=10
a*=2
print("*=",a)
a=10
a/=2
print("/=",a)
a=10
a//=2
print("//=",a)
a=10
a%=2
print("%=",a)
a=10
a**=2
print("**=",a)

# comparision operator
a=10
b=5
print("10>=5",a>=b)
print("10<=5",a<=b)
print("10==5",a==b)
print("10!=5",a!=b)
print("10<5",a<b)
print("10>5",a>b)

# logical operator
a=True
b=False
print("and",a and b)
print("or",a or b)
print("not",not b)


# bitwise operator
a=10
b=5
print("bitwise &",a&b)
print("bitwise |",a|b)
print("bitwise ^",a^b)
print("bitwise >>",a>>2)
print("bitwise <<",a<<2)

#identity operator
a=10
b=10.0
print("is",a is b)
print("is not",a is not b)

# membership operators
a="Soham"
print("in","s" in a)
print("not in","S" not in a)


# char to ASCII ord()
a="A"
val=ord(a)
print(val)

# ASCII to char chr()
print(chr(5))

#string formatting
a=10
b=20
sum=a+b
print("The addition of ",a," and ",b," is : ",sum)
print("The addition of {} and {} is {}".format(a,b,sum))
print(f"The addition of {a} and {b} is {sum}")
print("The addition of %d and %d is %d"%(a,b,sum))

#if..else.. positive negative num.
a=int(input("Enter a value: "))
if a>0:
    print("+ve")
elif a<0:
    print("-ve")
else:
    print("0")


#Soham Vaity batch 3