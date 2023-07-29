
def get_player_guess(min_num, max_num):
    while True:
            guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
            if min_num <= guess <= max_num:
                return guess
            else:
                print("Invalid Input data")


def play_game():
    min_num = 1
    max_num = 100
    secret_number = 50
    print("Welcome to game!")
    while True:
        guess = get_player_guess(min_num, max_num)

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correct , you are winner.")
            break
        else:
            print("You lost the game try again")


play_game()
