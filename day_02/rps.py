import random

def quit_game():
    print("Thanks for playing! Goodbye!")
    exit()

def game(user, computer):
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    result = determine_winner(user, computer)
    print(result)
    restart = input("Do you want to play again? (yes/no): ")
    if restart.lower() == 'yes':
        main()
    elif restart.lower() == 'no':
        quit_game()
    else:
        print("Invalid input, quitting the game.")
        quit_game()

def test(user):
        while user != 'quit':
            if user not in ['rock', 'paper', 'scissors']:
                print("Invalid choice, please try again.")
                user = input("Enter your choice (rock, paper, scissors or quit): ")
                continue
            if user in ['rock', 'paper', 'scissors']:
                break
        if user == 'quit':
            quit_game()

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"
def main():
    user= input("Enter your choice (rock, paper, scissors or quit): ")
    test(user)
    computer= random.choice(['rock', 'paper', 'scissors'])
    game(user, computer)

main()