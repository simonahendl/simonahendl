import base64
import random


def part1(num):
    number = input("Enter a number:")
    for num in number:
        if float(num) % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")

def part2():
    rand_number = random.randint(1,9)
    guess = 0

    while guess != rand_number and guess != "exit":
        guess = input("Please guess a number: ")

        if guess == "exit":
            break
        if int(guess) < rand_number:
            print("Too low.")
        elif int(guess) > rand_number:
            print("Too high.")
        else:
            print("Correct guess!")


def part3(string):
    if string[::-1] == string[0:]:
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome.")


def part4a(filename, username, password):
    encryptU = base64.b64encode(username.encode())
    encryptP = base64.b64encode(password.encode())
    f = open(filename, "w")
    f.write(str(encryptU.decode())+'\n')
    f.write(str(encryptP.decode()))
    f.close()

def part4b(filename, password=None):
    f = open(filename, "r")
    userAndPass = f.readlines()
    for line in userAndPass:
        print(base64.b64decode(line).decode())
    f.close()

    if password != None:
        f = open(filename, "w")
        userAndPass[1] = str(base64.b64encode(password.encode()).decode())
        f.writelines(userAndPass)
        f.close()

if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
