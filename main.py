# Basic Rock Paper Scissors Game
# Name: Anshu Pathak
# Date: 2026-02-13

import random

from rich.console import Console

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

# Create a Console object for rich output
console = Console()

choices = ["rock", "paper", "scissors"]
num_to_choice = {"1": "rock", "2": "paper", "3": "scissors"}


def get_user_choice():
    """Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
    while True:
        console.print("\n[bold cyan]Choose your move:[/bold cyan]")
        console.print("1. Rock")
        console.print("2. Paper")
        console.print("3. Scissors")

        user_input = (
            console.input("[yellow]Enter 1, 2, 3 or the word: [/yellow]")
            .lower()
            .strip()
        )

        # Check if it's a number key
        if user_input in num_to_choice:
            return num_to_choice[user_input]
        # Check if it's the word
        if user_input in choices:
            return user_input

        console.print("[bold red]Invalid choice! Please try again.[/bold red]")


def get_computer_choice():
    """Randomly return 'rock', 'paper', or 'scissors'."""
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """Return 'user', 'computer', or 'tie' based on the choices."""
    if user_choice == computer_choice:
        return "tie"

    # Winning conditions for the user
    win_conditions = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if win_conditions[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"


def print_round_result(user_choice, computer_choice, winner):
    """Print the choices and the winner of the round using rich colors."""
    console.print(f"\n[blue]You chose:[/blue] [bold]{user_choice}[/bold]")
    console.print(f"[magenta]Computer chose:[/magenta] [bold]{computer_choice}[/bold]")

    if winner == "tie":
        console.print("[bold yellow]It's a tie![/bold yellow]")
    elif winner == "user":
        console.print("[bold green]You win this round![/bold green]")
    else:
        console.print("[bold red]Computer wins this round![/bold red]")


def main():
    """Main function to run the game for 3 rounds and print the final result."""
    user_score = 0
    computer_score = 0
    rounds = 3

    console.print(
        "[bold underline reverse]Welcome to Rock, Paper, Scissors![/bold underline reverse]"
    )

    for round_num in range(1, rounds + 1):
        console.print(f"\n--- Round {round_num} ---", style="bold underline")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner(user_choice, computer_choice)
        print_round_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

    # Print final scores and announce the overall winner
    console.print("\n" + "=" * 20)
    console.print(
        f"[bold]Final Score -> You: {user_score} | Computer: {computer_score}[/bold]"
    )

    if user_score > computer_score:
        console.print("[bold green]Congratulations, you win the game![/bold green]")
    elif computer_score > user_score:
        console.print(
            "[bold red]The computer wins the game. Better luck next time![/bold red]"
        )
    else:
        console.print("[bold yellow]The game is a draw![/bold yellow]")


if __name__ == "__main__":
    main()
