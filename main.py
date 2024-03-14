from random import randint as ri


def make_dice_rolls(dice_count):
    dice_list = list()
    for i in range(dice_count):
        dice_list.append(ri(1, 6))
    dice_list.sort(reverse=True)
    return dice_list


def second_roll_value(roll_list):
    if len(roll_list) > 1:
        return roll_list[1]


def simulation(num_atk_dice, num_def_dice):
    # Randomise the rolls
    atk_rolls = make_dice_rolls(num_atk_dice)
    def_rolls = make_dice_rolls(num_def_dice)

    # Take the max roll values
    max_atk_roll = atk_rolls[0]
    max_def_roll = def_rolls[0]

    # Take the second highest roll values, if they exist
    other_atk_roll = second_roll_value(atk_rolls)
    other_def_roll = second_roll_value(def_rolls)

    outcome = 0
    outcome += 0.5 if max_atk_roll > max_def_roll else -0.5
    outcome += 0.5 if other_atk_roll > other_def_roll else -0.5

    return outcome


if __name__ == '__main__':
    num_atk_dice = 3
    num_def_dice = 2
    num_runs = 500000

    run_outcome = 0
    def_wins = 0
    atk_wins = 0
    draws = 0
    for i in range(num_runs):
        # For memory efficiency, we don't store each set of dice roll outcomes.
        run_outcome = simulation(num_atk_dice, num_def_dice)
        if run_outcome == 1:
            atk_wins += 1
        elif run_outcome == -1:
            def_wins += 1
        else:
            draws += 1

    print(f"""
    There were:
        {num_runs} simulated fights of {num_atk_dice} attackers vs {num_def_dice} defenders.
        {atk_wins} attacker wins.
        {def_wins} defender wins.
        
        {draws} draws ({num_runs - draws} non-draws).
    
    Alternatively: With equal men, for roughly every 1000 times the defender wins, the attacker wins {int((atk_wins / def_wins) * 1000)}.)
    This represents a "win" {((atk_wins / (num_runs - draws))*100)}% of the time for the attacker, discounting draws.""")
