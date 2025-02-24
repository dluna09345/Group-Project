def factorial(num):
    finalNum = 1
    for i in range(num, 0, -1):
        finalNum = finalNum * i
    return finalNum

if __name__ == "__main__":
    print(factorial(int(input("Please Enter the Number to be factorial-ed: "))))