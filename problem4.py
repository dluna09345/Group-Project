def problem4(n):
    finalList = []
    for i in range(n):
        i += 1
        if (i % 3 == 0 and i % 5 == 0):
            finalList.append("FizzBuzz")
        elif (i % 3 == 0):
            finalList.append("Fizz")
        elif (i % 5 == 0):
            finalList.append("Buzz")
        else:
            finalList.append(i)
    return finalList

if __name__ == "__main__":
    print(problem4(int(input("Please Enter a Number: "))))