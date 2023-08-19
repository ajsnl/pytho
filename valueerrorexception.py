try:
    num=int(input("enter a number"))
    deno=int(input("enter a number"))
    res=num/deno
    print(res)
except ValueError:
    print("error:not valid integer")
        