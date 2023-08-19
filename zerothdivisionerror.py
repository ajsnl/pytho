try:
    num=int(input("enter a number"))
    deno=int(input("enter a number"))
    res=num/deno
    print(res)
except ZeroDivisionError:
    print("error:division by zero is not possible")
    
        