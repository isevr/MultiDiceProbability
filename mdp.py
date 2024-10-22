from itertools import product
from math import comb
import math
from scipy.stats import binom

def get_success_probability(num_blue, num_red, num_green, target_successes):
    p_blue_success = 0.6  # Blue succeeds on 5+
    p_red_success = 0.4   # Red succeeds on 7+
    p_green_success = 0.8 # Green succeeds on 3+

    total_dice = num_blue + num_red + num_green
    
    success_probabilities = [p_blue_success] * num_blue + [p_red_success] * num_red + [p_green_success] * num_green
    
    total_prob = 0
    
    for success_count in range(target_successes, total_dice + 1):
        prob = 0
        for combination in product([0, 1], repeat=total_dice):
            if sum(combination) == success_count:
                combination_prob = 1
                for i in range(total_dice):
                    if combination[i] == 1:  # Success
                        combination_prob *= success_probabilities[i]
                    else:  # Failure
                        combination_prob *= (1 - success_probabilities[i])
                prob += combination_prob
        total_prob += prob

    return total_prob

def dice_recommendation(success_prob, target_successes):
    p_single_die_success = 0.5

    def calc_required_dice(p_die_success, target_prob):
        return math.ceil(math.log(1 - target_prob) / math.log(1 - p_die_success))

    recommended_dice = 0
    total_prob = 0
    while total_prob < success_prob:
        recommended_dice += 1
        total_prob = sum(binom.pmf(k, recommended_dice, p_single_die_success) for k in range(target_successes, recommended_dice + 1))

    return recommended_dice

def main():
    while True:
        print("Enter the number of blue, red, and green dice you will roll:")
        num_blue = int(input("Number of blue dice: "))
        num_red = int(input("Number of red dice: "))
        num_green = int(input("Number of green dice: "))

        target_successes = int(input("Enter the target number of successes: "))

        total_dice = num_blue + num_red + num_green
        if target_successes > total_dice:
            print(f"\nIt is impossible to achieve {target_successes} successes with only {total_dice} dice.")
            choice = str(input('Type "a" to run another calculation or "q"to quit: '))

            if choice == 'q':
                break
            elif choice == 'a':
                continue
            else:
                choice = str(input('Type "a" to run another calculation or "q"to quit: '))

        success_prob = get_success_probability(num_blue, num_red, num_green, target_successes)
        
        print(f"\nThe probability of getting at least {target_successes} successes with the colored dice is: {success_prob:.4f}")

        recommended_dice = dice_recommendation(success_prob, target_successes)
        print(f"\nTo achieve a similar probability with 6-sided dice (rolling 4+), you should roll approximately {recommended_dice} dice.")
        choice = str(input('Type "a" to run another calculation or "q"to quit: '))

        if choice == 'q':
            break
        elif choice == 'a':
            continue
        else:
            choice = str(input('Type "a" to run another calculation or "q"to quit: '))

if __name__ == "__main__":
    main()