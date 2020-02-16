a = input("")

if a.islower() == True:
    print(a +" "+ "Hi I am lowercase.......")
elif a.isupper() == True:
    print(a +" "+ "Hi I am Uppercase........")
elif a.istitle() == True:
    print(a +" "+ "Hi I am Title........")
else:
    print(a +" "+ "Unknown type>>>>>>>>>")


print("\n")