# Multi Dice Probability Calculator

This Python program calculates the probability of achieving a specified number of successes using custom colored dice (blue, red, and green) with different success thresholds. It also recommends how many six-sided dice to roll to achieve the same probability of success, where success is defined as rolling a 4 or higher.

## Table of Contents
- [Overview](#overview)
- [Methodology](#methodology)
- [How the Program Works](#how-the-program-works)
  - [Input](#input)
  - [Output](#output)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Overview

This program calculates the probability of getting a specific number of successes when rolling custom colored dice. Each color of die has a different threshold for success, and the program supports rolling a mix of blue, red, and green dice.

Additionally, the program can recommend how many standard six-sided dice (where a success is defined as rolling 4+) you would need to roll in order to achieve the same success probability.

## Methodology

This program calculates the probability of achieving a given number of successes using multiple types of dice (blue, red, and green), each with a different probability of success. It also recommends how many standard six-sided dice to roll in order to achieve a similar probability of success. 

### Success Probability for Colored Dice

Each colored die has a different threshold for success:

| Die Color | Success Condition    | Success Probability |
|-----------|----------------------|---------------------|
| Blue      | Rolls 6 or higher     | 0.5 (50%)           |
| Red       | Rolls 4 or higher     | 0.7 (70%)           |
| Green     | Rolls 8 or higher     | 0.3 (30%)           |

The challenge is to calculate the probability of achieving **at least** a certain number of successes when rolling a specified number of these dice, given that each die has a different success probability.

#### Key Concepts:

1. **Combination of Probabilities**: For each die, the outcome of success or failure is independent of the other dice. Therefore, for a given number of successes across multiple dice, we need to consider **all possible combinations** of successes and failures for the dice.

2. **Binomial Distribution**: 
   The probability of getting exactly \( k \) successes out of \( n \) trials, where each trial has a success probability \( p \), is modeled by the binomial distribution. The binomial probability mass function is given by:
   
   **P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)**

   Where:
   - \( P(X = k) \) is the probability of getting exactly \( k \) successes.
   - \( C(n, k) \) is the binomial coefficient, which gives the number of ways to choose \( k \) successes from \( n \) trials.
   - \( p \) is the probability of success on a single trial.
   - \( n \) is the number of trials (in our case, the number of dice rolled).


3. **Sum of Probabilities for Multiple Dice**: Since each type of die (blue, red, green) has a different probability of success, we can’t directly use the binomial distribution formula. Instead, we calculate the success and failure probabilities for each possible combination of dice results (using **all combinations of successes and failures**) and sum them to find the overall probability of achieving at least the target number of successes.

### Implementation

1. **Success Probability Calculation**:
   - The code calculates the probability of achieving at least the target number of successes by iterating over **all possible success/failure combinations** of the dice. For each combination, it multiplies the probabilities of success or failure for the individual dice and sums up the probabilities of the combinations where the total number of successes matches or exceeds the target.
   
   For example:
   - If you roll 1 blue die, 2 red dice, and 1 green die, and you want to know the probability of achieving at least 2 successes, the program computes the probabilities for every combination of success and failure for these dice and sums the relevant probabilities.

2. **Recommendation for Six-Sided Dice**:
   - To recommend the number of six-sided dice that should be rolled to achieve the same probability of success, the program assumes a **50% success rate** for each die (since success on a six-sided die is defined as rolling a 4 or higher).
   - It then calculates the number of dice needed to achieve the same overall probability of hitting at least the target number of successes using six-sided dice.
   - This part of the program uses an iterative method to find the smallest number of six-sided dice required to match or exceed the target success probability by summing the probabilities for different numbers of successes using the binomial distribution.

## How the Program Works

### Input

The program prompts the user for the following inputs:

1. **Number of Blue Dice**: The number of blue dice to roll.
2. **Number of Red Dice**: The number of red dice to roll.
3. **Number of Green Dice**: The number of green dice to roll.
4. **Target Number of Successes**: The minimum number of successes you want to achieve.

### Output

The program will output the following:

1. The probability of achieving at least the target number of successes with the specified dice.
2. A recommendation of how many six-sided dice you should roll to achieve a similar probability of success, where a success on a six-sided die is defined as rolling a 4 or higher.

## Installation

To use the program, follow these steps:

1. Install Python 3.6+.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the provided Python file.

## Usage

Run the program in a terminal or command prompt using the following command:

```bash
python mdp.py
``` 

## Example
```
Enter the number of blue, red, and green dice you will roll:
Number of blue dice: 1
Number of red dice: 2
Number of green dice: 1
Enter the target number of successes: 2

The probability of getting at least 2 successes with the colored dice is: 0.6964

To achieve a similar probability with 6-sided dice (rolling 4+), you should roll approximately 4 dice.
```
