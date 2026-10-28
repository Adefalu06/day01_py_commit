import sys
import random
from enum import Enum


# game_count =0
def rps(name="PlayerOne"):
    game_count=0
    player_wins =0
    python_wins =0

    def play_game():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        playerChoice = input(
            f"\n {name} please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerChoice  not in ["1","2","3"]:
            print(f"{name} please enter 1, 2, or 3.")
            return play_game()

    
        player =int(playerChoice)

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print(f"\n{name} you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )
        
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name
            if player == 1 and computer == 3:
                player_wins +=1
                return(f"🎉 {name}, you win!")
            elif player == 2 and computer == 1:
                player_wins +=1
                return(f"🎉 {name}, you win!")
            elif player == 3 and computer == 2:
                player_wins +=1
                return(f"🎉 {name}, you win!")
            elif player == computer:
                return("😲 Tie game!")
            else:
                python_wins +=1
                return(f"🐍 Python wins! sorry\n {name} 😲...")
            
        game_result=decide_winner(player,computer)
        print(game_result)

        nonlocal game_count 
        
        game_count +=1

        print(f"\n Game Count: {game_count}")
        print(f"\n {name}'s Wins: { player_wins}")
        print(f"\n Python Wins: { python_wins}")

        print(f"\nPlay again? ")

        while True:
            playAgain = input("\nY for Yes or \nQ to Quit \n\n")
            if playAgain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playAgain.lower() == "y":
            return play_game()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
        sys.exit(f"Bye! {name} 👋")

    return play_game


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description= "Provide personalized"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing te game."
    )
   

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
