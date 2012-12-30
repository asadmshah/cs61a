"""The Game of Hog"""

from dice import four_sided_dice, six_sided_dice, make_test_dice
from ucb import main, trace, log_current_line, interact

goal = 100			# The goal of Hog is to score 100 points.
commentary = False	# Whether to display commentary for every roll.

# Taking turns

def roll_dice(num_rolls, dice=six_sided_dice, who='Boss Hogg'):
	"""
	Calculate WHO's turn score after rolling DICE for NUM_ROLLS times.

	num_rolls:	The number of dice rolls that will be made; at least 1.
	dice:		A function of no args and returns an integer outcome.
	who:		Name of the current player, for commentary.
	"""
	assert type(num_rolls) == int, "num_rolls must be an integer."
	assert num_rolls > 0, "Must roll at least once."
	total = 0
	for i in range(num_rolls):
		this_roll = dice()
		if commentary:
			announce(this_roll, who)
		if this_roll == 1:
			total = this_roll
			break
		total += this_roll
	return total

def take_turn(num_rolls, opponent_score, dice=six_sided_dice, who='Boss Hogg'):
	"""
	Simulate a turn in which WHO chooses to roll NUM_ROLLS, perhaps 0.

	num_rolls:		The number of dice rolls that will be made.
	opponent_score:	The total score of the opponent.
	dice:			A function of no args and returns an integer outcome.
	who:			A function of no args and returns an integer outcome.
	"""
	assert type(num_rolls) == int, "num_rolls must be an integer."
	assert num_rolls >= 0, "Cannot roll a negative number of dice."
	if commentary:
		print(who, "is going to roll", num_rolls, "dice")
	if num_rolls == 0:
		return (opponent_score // 10) + 1
	return roll_dice(num_rolls, dice=dice, who=who)


def take_turn_test():
	"""Test the roll_dice and take_turn functions using test dice."""
	print('-- Testing roll_dice with deterministic test dice --')
	dice = make_test_dice(4, 6, 1)
	assert roll_dice(2, dice) == 10, 'First two rolls total 10'

	dice = make_test_dice(4, 6, 1)
	assert roll_dice(3, dice) == 1, 'Third roll is a 1'

	dice = make_test_dice(1, 2, 3)
	assert roll_dice(3, dice) == 1, 'First roll is a 1'

	print('-- Testing take_turn --')
	dice = make_test_dice(4, 6, 1)
	assert take_turn(2, 0, dice) == 10, 'First two rolls total 10'

	dice = make_test_dice(4, 6, 1)
	assert take_turn(3, 20, dice) == 1, 'Third roll is a 1'

	assert take_turn(0, 34) == 4, 'Opponent score 10s digit is 3'
	assert take_turn(0, 71) == 8, 'Opponent score 10s digit is 7'
	assert take_turn(0,  7) == 1, 'Opponont score 10s digit is 0'

	'*** You may add more tests here if you wish ***'

	print('Tests for roll_dice and take_turn passed.')


# Commentator

def announce(outcome, who):
    """Print a description of WHO rolling OUTCOME."""
    print(who, 'rolled a', outcome)
    print(draw_number(outcome))

def draw_number(n, dot='*'):
	"""Return a text representation of rolling the number N.
	If a number has multiple possible representations (such as 2 and 3), any
	valid representation is acceptable.

	>>> print(draw_number(5))
	 -------
	| *   * |
	|   *   |
	| *   * |
	 -------

	>>> print(draw_number(6, '$'))
	 -------
	| $   $ |
	| $   $ |
	| $   $ |
	 -------
	"""
	assert len(dot) == 1, "Dot must be a single symbol."
	two = "| {0}   {1} |\n".format(dot, dot)
	one = "| {0}     |\n".format(dot)
	nil = "|       |\n"
	mid = "|   {0}   |\n".format(dot)
	border = ' -------'
	design = ''
	template = "{0}{1}{2}"

	if n == 1:
		design = template.format(nil,mid,nil)
	elif n == 2:
		design = template.format(two,nil,nil)
	elif n == 3:
		design = template.format(two,one,nil)
	elif n == 4:
		design = template.format(two,two,nil)
	elif n == 5:
		design = template.format(two,mid,two)
	else:
		design = template.format(two,two,two)
	return border + "\n" + design + border

def draw_dice(c, f, b, s, dot):
    """Return an ASCII art representation of a die roll.

    c, f, b, & s are boolean arguments. This function returns a multi-line
    string of the following form, where the letters in the diagram are either
    filled if the corresponding argument is true, or empty if it is false.

     -------
    | b   f |
    | s c s |
    | f   b |
     -------

    The sides with 2 and 3 dots have 2 possible depictions due to rotation.
    Either representation is acceptable.

    This function uses Python syntax not yet covered in the course.

    c, f, b, s -- booleans; whether to place dots in corresponding positions.
    dot        -- A length-one string to use for a dot.
    """
    assert len(dot) == 1, 'Dot must be a single symbol'
    border = ' -------'
    def draw(b):
        return dot if b else ' '
    c, f, b, s = map(draw, [c, f, b, s])
    top = ' '.join(['|', b, ' ', f, '|'])
    middle = ' '.join(['|', s, c, s, '|'])
    bottom = ' '.join(['|', f, ' ', b, '|'])
    return '\n'.join([border, top, middle, bottom, border])


# Game simulator

def num_allowed_dice(score, opponent_score):
	"""Return the maximum number of dice allowed this turn. The maximum
	number of dice allowed is 10 unless the sum of SCORE and
	OPPONENT_SCORE has a 7 as its ones digit.

	>>> num_allowed_dice(1, 0)
	10
	>>> num_allowed_dice(5, 7)
	10
	>>> num_allowed_dice(7, 10)
	1
	>>> num_allowed_dice(3, 24)
	1
	"""
	if (score + opponent_score) % 10 == 7:
		return 1
	else:
		return 10


def select_dice(score, opponent_score):
	"""Select 6-sided dice unless the sum of scores is a multiple of 7.

	>>> select_dice(4, 24) == four_sided_dice
	True
	>>> select_dice(16, 64) == six_sided_dice
	True
	"""
	if (score + opponent_score) % 7 == 0:
		return four_sided_dice
	else:
		return six_sided_dice

def other(who):
    """Return the other player, for players numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return (who + 1) % 2

def name(who):
    """Return the name of player WHO, for player numbered 0 or 1."""
    if who == 0:
        return 'Player 0'
    elif who == 1:
        return 'Player 1'
    else:
        return 'An unknown player'

def play(strategy0, strategy1):
	"""Simulate a game and return 0 if the first player wins and 1 otherwise.

	A strategy function takes two scores for the current and opposing players.
	It returns the number of dice that the current player will roll this turn.

	If a strategy returns more than the maximum allowed dice for a turn, then
	the maximum allowed is rolled instead.

	strategy0:  The strategy function for player 0, who plays first.
	strategy1:  The strategy function for player 1, who plays second.
	"""
	who = 1
	strats = (strategy0, strategy1)
	score1, score2 = 0, 0

	global name
	global num_allowed_dice
	global select_dice
	global take_turn

	while score1 <= 100 or score2 <= 100:

		if who == 0:
			who = 1
			player_score = score1
			opponent_score = score2
		else:
			who = 0
			player_score = score2
			opponent_score = score1

		this_name = name(who)
		this_strategy = strats[who]

		this_wanted_roll = this_strategy(player_score, opponent_score)
		this_allowed_roll = num_allowed_dice(player_score, opponent_score)
		this_dice = select_dice(player_score, opponent_score)
		
		this_roll = min(this_wanted_roll, this_allowed_roll)
		this_score = take_turn(this_roll, opponent_score, dice=this_dice, who=this_name)

		if who == 0:
			score1 += this_score
		else:
			score2 += this_score

	return who


# Basic Strategy

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two game scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice to roll.

    If a strategy returns more than the maximum allowed dice for a turn, then
    the maximum allowed is rolled instead.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


# Experiments (Phase 2)

def make_average(fn, num_samples=100):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> avg_dice = make_average(dice)
    >>> avg_dice()
    3.75
    >>> avg_score = make_average(roll_dice)
    >>> avg_score(2, dice, False)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    "*** YOUR CODE HERE ***"

def compare_strategies(strategy, baseline=always_roll(5)):
    """Return the average win rate (out of 1) of STRATEGY against BASELINE."""
    as_first = 1 - make_average(play)(strategy, baseline)
    as_second = make_average(play)(baseline, strategy)
    return (as_first + as_second) / 2  # Average the two results

def eval_strategy_range(make_strategy, lower_bound, upper_bound):
    """Return the best integer argument value for MAKE_STRATEGY to use against
    the always-roll-5 baseline, between LOWER_BOUND and UPPER_BOUND (inclusive).

    make_strategy -- A one-argument function that returns a strategy.
    lower_bound -- lower bound of the evaluation range.
    upper_bound -- upper bound of the evaluation range.
    """
    best_value, best_win_rate = 0, 0
    value = lower_bound
    while value <= upper_bound:
        strategy = make_strategy(value)
        win_rate = compare_strategies(strategy)
        print('Win rate against the baseline using', value, 'value:', win_rate)
        if win_rate > best_win_rate:
            best_win_rate, best_value = win_rate, value
        value += 1
    return best_value

def run_experiments():
    """Run a series of strategy experiments and report results."""
    result = eval_strategy_range(always_roll, 1, 10)
    print('Best always_roll strategy:', result)

    if False: # Change to True when ready to test make_comeback_strategy
        result = eval_strategy_range(make_comeback_strategy, 5, 15)
        print('Best comeback strategy:', result)

    if False: # Change to True when ready to test make_mean_strategy
        result = eval_strategy_range(make_mean_strategy, 1, 10)
        print('Best mean strategy:', result)

    "*** You may add additional experiments here if you wish ***"


# Strategies

def make_comeback_strategy(margin, num_rolls=5):
    """Return a strategy that rolls one extra time when losing by MARGIN."""
    "*** YOUR CODE HERE ***"
    return always_roll(num_rolls)

def make_mean_strategy(min_points, num_rolls=5):
    """Return a strategy that attempts to give the opponent problems."""
    "*** YOUR CODE HERE ***"
    return always_roll(num_rolls)

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    "*** YOUR CODE HERE ***"

def final_strategy_test():
    """Compares final strategy to the baseline strategy."""
    print('-- Testing final_strategy --')
    print('Win rate:', compare_strategies(final_strategy))



# Interaction.  You don't need to read this section of the program.

def interactive_strategy(score, opponent_score):
    """Prints total game scores and returns an interactive tactic.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    print('Current score:', score, 'to', opponent_score)
    while True:
        response = input('How many dice will you roll? ')
        try:
            result = int(response)
        except ValueError:
            print('Please enter a positive number')
            continue
        if result < 0:
            print('Please enter a non-negative number')
        else:
            return result

def play_interactively():
    """Play one interactive game."""
    global commentary
    commentary = True
    print("Shall we play a game?")
    winner = play(interactive_strategy, always_roll(5))
    if winner == 0:
        print("You win!")
    else:
        print("The computer won.")

def play_basic():
    """Play one game in which two basic strategies compete."""
    global commentary
    commentary = True
    winner = play(always_roll(5), always_roll(6))
    if winner == 0:
        print("Player 0, who always wants to roll 5, won.")
    else:
        print("Player 1, who always wants to roll 6, won.")

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--take_turn_test', '-t', action='store_true')
    parser.add_argument('--play_interactively', '-p', action='store_true')
    parser.add_argument('--play_basic', '-b', action='store_true')
    parser.add_argument('--run_experiments', '-r', action='store_true')
    parser.add_argument('--final_strategy_test', '-f', action='store_true')
    args = parser.parse_args()
    for name, execute in args.__dict__.items():
        if execute:
            globals()[name]()

