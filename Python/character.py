ch=input("Enter the character:")
if(ch.isalpha()):
    print(f"{ch} is a Character")
elif(ch.isnumeric()):
    print('{} is a Numeric'.format(ch))
elif(ch.isspace()):
    print("Space")
