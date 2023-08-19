try:
    a=10
    print(a)
except NameError:
    print("error") 
else:
    print("nothing happened") 
finally:
    print("hai")          