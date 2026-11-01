def minimax(coins, i, j):
    if i > j:
        return 0

    if i == j:
        return coins[i]

    left = coins[i] + min(
        minimax(coins, i + 2, j),
        minimax(coins, i + 1, j - 1)
    )

    right = coins[j] + min(
        minimax(coins, i, j - 2),
        minimax(coins, i + 1, j - 1)
    )

    return max(left, right)


def ai_move(coins):
    n = len(coins)

    if n == 1:
        return 0

    left_score = coins[0] + min(
        minimax(coins, 2, n - 1),
        minimax(coins, 1, n - 2)
    )

    right_score = coins[-1] + min(
        minimax(coins, 0, n - 3),
        minimax(coins, 1, n - 2)
    )

    if left_score >= right_score:
        return 0
    else:
        return n - 1


# Main program

coins = [5, 3, 7, 10]

human_score = 0
ai_score = 0

print("==== COIN GAME ====")
print("You can take only the LEFT or RIGHT coin.")
print("You are HUMAN.")
print("AI uses MINIMAX.\n")

while len(coins) > 0:

    print("\nCoins:", coins)

    choice = input("Your choice (L/R): ").upper()

    while choice not in ["L", "R"]:
        choice = input("Enter L for Left or R for Right: ").upper()

    if choice == "L":
        coin = coins.pop(0)
    else:
        coin = coins.pop()

    human_score += coin

    print("You took:", coin)
    print("Your score:", human_score)

    if len(coins) == 0:
        break

    position = ai_move(coins)

    if position == 0:
        coin = coins.pop(0)
        print("AI chooses LEFT")
    else:
        coin = coins.pop()
        print("AI chooses RIGHT")

    ai_score += coin

    print("AI took:", coin)
    print("AI score:", ai_score)


# Display final results

print("\n=================")
print("GAME OVER")
print("=================")

print("Human Score:", human_score)
print("AI Score:", ai_score)

if human_score > ai_score:
    print("You WIN!")
elif ai_score > human_score:
    print("AI WINS!")
else:
    print("DRAW!")
