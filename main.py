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
    outcome += 1 if max_atk_roll > max_def_roll else -1
    outcome += 1 if other_atk_roll > other_def_roll else -1
    outcome = int(outcome / 2)

    return outcome


if __name__ == '__main__':
    num_atk_dice = 3
    num_def_dice = 2
    num_runs = 5000000

    outcome_avg = 0

    for i in range(num_runs):
        # For memory efficiency, we don't store each set of dice roll outcomes.
        outcome_avg += simulation(num_atk_dice, num_def_dice) / num_runs

    print(f'Avg outcome: {outcome_avg:6f}')
    print(f"""
    An outcome of 1 means attacker won and the defender lost two men.
    An outcome of -1 means the defender won and the attacker lost two men.
    An outcome of 0 means both sides lost one each.
    
    If the Avg Outcome value is multiplied by the defender count, the fight should always be a close match.
    Alternatively: With equal men, for roughly every 1000 men the defender kills, the attacker kills {1000 + int(outcome_avg * 1000)}.)
    This represents a "win" {((1 + outcome_avg) / 2) * 100}% of the time for the attacker, discounting draws.""")
