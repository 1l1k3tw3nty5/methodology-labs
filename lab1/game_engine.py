import random
import math

def run_game(game_logic, description):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)
    
    for _ in range(3):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def game_lcm():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = math.lcm(*numbers)
    return question, correct_answer

def game_geometric_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer

if __name__ == "__main__":
    games = {
        "lcm": (game_lcm, "Find the smallest common multiple of given numbers."),
        "progression": (game_geometric_progression, "What number is missing in the progression?")
    }
    
    print("Choose a game: 'lcm' or 'progression'")
    choice = input().strip().lower()
    
    if choice in games:
        run_game(*games[choice])
    else:
        print("Invalid game choice.")
