import random

class RPS:
    def __init__(self, rounds):
        self.rounds = rounds
        self.round = 0
        self.userwins = 0
        self.compwins = 0
        self.choices = ["rock", "paper", "scissors"]

    def comp_pick(self):
        return random.choice(self.choices)

    def check_winner(self, user, comp):
        if user == comp:
            return "draw"
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            self.userwins += 1
            return "user"
        else:
            self.compwins += 1
            return "comp"

    def play(self):
        print(f"Game Start! {self.rounds} rounds.")
        while self.round < self.rounds:
            user = input("Rock, Paper, Scissors? ").lower()
            if user not in self.choices:
                print("Invalid! Try again.")
                continue

            comp = self.comp_pick()
            print(f"Computer: {comp}")
            result = self.check_winner(user, comp)

            if result == "user":
                print("You win!")
            elif result == "comp":
                print("Computer wins!")
            else:
                print("Draw!")

            self.round += 1

        self.show_result()

    def show_result(self):
        print("\nFinal Score:")
        print(f"You: {self.userwins} | Computer: {self.compwins}")

        if self.userwins > self.compwins:
            print("You win the game!")
        elif self.compwins > self.userwins:
            print("Computer wins the game!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    r = int(input("Enter rounds: "))
    game = RPS(r)
    game.play()