import random
import string
print("Welcome to our Random Passward Genertor")
def main():

    length=int(input("Enter the lenght of passward you want:"))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine=lowerD+upperD+digitD+symbolsD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()
