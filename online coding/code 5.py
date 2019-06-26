a = [1, 2, 3, 4, 5]
b = [1, 2, 6, 7, 8]

while True:
    number = int(input("enter your number here: "))

    if number in a:
        print ("its in a")
    elif number in b:
        print ("its in b")
    elif number not in a or b:
        print ("neither")


