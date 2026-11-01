low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:
    guess = (low + high) // 2

    print("My guess is:", guess)
    feedback = input("Enter higher, lower, or correct: ").lower()

    if feedback == "correct":
        print("I guessed the number!")
        break

    elif feedback == "higher":
        low = guess + 1

    elif feedback == "lower":
        high = guess - 1

    else:
        print("Invalid feedback. Try again.")

if low > high:
    print("The feedback was inconsistent or the number is outside the range.")