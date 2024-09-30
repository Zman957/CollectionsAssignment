
inputOne = input("Please enter the student's name: ")

inputTwo = int(input("Now write your five grades below:\n "))
inputThree = int(input(" "))
inputFour = int(input(" "))
inputFive = int(input(" "))
inputSix = int(input(" "))

allAdded = [inputTwo, inputThree, inputFour, inputFive, inputSix]

average = sum(allAdded) / len(allAdded)

print ("Average:", average)

if(average >= 90):
    print("Letter grade: A")
elif(average >= 80):
    print("Letter grade: B")
elif(average >= 70):
    print("Letter grade: C")
elif(average >= 60):
    print("Letter grade: D")
elif(average >= 50):
    print("Letter grade: F")
else:
    print("Halo 5 will forever be the best game")