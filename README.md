# Multi Dice Probability Calculator

This Python program calculates the probability of achieving a specified number of successes using custom colored dice (blue, red, and green) with different success thresholds. It also recommends how many six-sided dice to roll to achieve the same probability of success, where success is defined as rolling a 4 or higher.

## Table of Contents
- [Overview](#overview)
- [Dice Success Conditions](#dice-success-conditions)
- [How the Program Works](#how-the-program-works)
  - [Input](#input)
  - [Output](#output)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Overview

This program calculates the probability of getting a specific number of successes when rolling custom colored dice. Each color of die has a different threshold for success, and the program supports rolling a mix of blue, red, and green dice.

Additionally, the program can recommend how many standard six-sided dice (where a success is defined as rolling 4+) you would need to roll in order to achieve the same success probability.

## Dice Success Conditions

The following table describes the success conditions for each die type:

| Die Color | Success Condition    | Success Probability |
|-----------|----------------------|---------------------|
| Blue      | Rolls 5 or higher     | 0.6 (60%)           |
| Red       | Rolls 7 or higher     | 0.4 (40%)           |
| Green     | Rolls 3 or higher     | 0.8 (80%)           |

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
