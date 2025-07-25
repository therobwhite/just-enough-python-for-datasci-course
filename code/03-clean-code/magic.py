import random


def play_round() -> bool:
    player_boost = 2
    dice_sides = 12

    player = random.randint(1, dice_sides) * player_boost
    opponent = random.randint(1, dice_sides)

    player_wins = player > opponent
    return player_wins

print(play_round())
