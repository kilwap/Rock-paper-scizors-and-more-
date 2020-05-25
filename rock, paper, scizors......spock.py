import random
if __name__ == '__main__':
    while True:
        human = input("rock, paper, scissors, lizard or spock? Choose: ")
        l = ["rock", "paper", "scissors", "spock"]
        computer = (random.choice(l))
#rock
        if human == "rock" and computer == "paper":
            print("Loser! Paper covers rock.")
            print("Try again")
        elif human == "rock" and computer == "spock":
            print("Loser! Spock vaporizes rock.")
            print("Try again")
        elif human == "rock" and computer == "lizard":
            print("Winner! Rock crushes lizard.")
            print("Try again")
        elif human == "rock" and computer == "scissors":
            print("Winner! Rock crushes scissors.")
            print("Try again")
        elif human == "rock" and computer == "rock":
            print("Double rocks. It's a tie!")
            print("Try again")
#paper
        elif human == "paper" and computer == "paper":
            print("Double papers. It's a tie!")
            print("Try again")
        elif human == "paper" and computer == "spock":
            print("Winner! Paper dissproves rock.")
            print("Try again")
        elif human == "paper" and computer == "lizard":
            print("Loser! Lizard eats paper.")
            print("Try again")
        elif human == "paper" and computer == "scissors":
            print("Loser! Scissors cuts paper.")
            print("Try again")
        elif human == "paper" and computer == "rock":
            print("Winner! paper covers rock")
            print("Try again")
#scissors
        elif human == "scissors" and computer == "paper":
            print("Winner! Scissors cuts paper")
            print("Try again")
        elif human == "scissors" and computer == "spock":
            print("Loser! Spock smashes scissors.")
            print("Try again")
        elif human == "scissors" and computer == "lizard":
            print("Winner! Scissors decapitates lizard.")
            print("Try again")
        elif human == "scissors" and computer == "scissors":
            print("Double scissors. It's a tie!")
            print("Try again")
        elif human == "scissors" and computer == "rock":
            print("Loser! Rock crashes scissors")
            print("Try again")
#lizard
        elif human == "lizard" and computer == "paper":
            print("Winner! Lizard eats paper")
            print("Try again")
        elif human == "lizard" and computer == "spock":
            print("Winner! Lizard poisons spock.")
            print("Try again")
        elif human == "lizard" and computer == "lizard":
            print("Double lizard. It's a tie!")
            print("Try again")
        elif human == "lizard" and computer == "scissors":
            print("Loser! Scissors decapitates lizard")
            print("Try again")
        elif human == "lizard" and computer == "rock":
            print("Loser! Rock crashes lizard")
            print("Try again")
        # lizard
#spock
        elif human == "spock" and computer == "paper":
            print("Loser! Paper disproves spock.")
            print("Try again")
        elif human == "spock" and computer == "spock":
            print("Double spocks. It's a tie!")
            print("Try again")
        elif human == "spock" and computer == "lizard":
            print("Loser! Lizard poisones spock")
            print("Try again")
        elif human == "spock" and computer == "scissors":
            print("Winner! Spock smashes scissors")
            print("Try again")
        elif human == "spock" and computer == "rock":
            print("Winner! Spock vaporizes rock")
            print("Try again")
        else:
            print ("BAZINGA! You didn't choose the right option. Choose wisely next time.")
