import random
import math

def game_lcm():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = math.lcm(*numbers)
    return question, correct_answer
