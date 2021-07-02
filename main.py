import random

MONEY = 100
choice = ''

def row_to_numbers(row):
	new_list = []
	new_list.append((1 + 3 * (row - 1)))
	new_list.append((2 + 3 * (row - 1)))
	new_list.append((3 + 3 * (row - 1)))
	return new_list

def check_list_contains_number(lst, num):
	for index in range(-1, len(lst)):
		if num == lst[index]:
			return True
		else:
			return False

def coin_flip(bet, choice):
	heads_or_tails = random.randint(0, 1)
	if  heads_or_tails == 0:
		outcome = 'Heads'
	elif heads_or_tails == 1:
		outcome = 'Tails'

	earnings = bet
	losses = -1 * bet

	if outcome == choice:
		print('Nice, the coin flipped with ' + choice + ' on top!')
		return earnings
	else:
		print('Unfortunately, the coin flipped with ' + choice + ' on top.')
		return losses

def cho_han(bet, choice):
	outcome_dice1 = random.randint(1, 6)
	outcome_dice2 = random.randint(1, 6)
	sum = outcome_dice1 + outcome_dice2

	print('The first dice rolled with ', outcome_dice1, ' on top.')
	print('The second dice rolled with ', outcome_dice2, ' on top.')
	print('So the sum of the 2 dices is ', sum, '.')

	if sum % 2 == 0:
		outcome = 'Even'
	else:
		outcome = 'Odd'

	if choice == outcome:
		print('Congratulations, the sum of the 2 dices was indeed ', choice, '!' )	
	else:
		print('Too bad, the sum of the 2 dices was ', outcome, ' and not ', choice, '.')

def pick_a_card(bet):
	card_1 = random.randint(2, 13)
	card_2 = random.randint(2, 13)
	name_card_1 = ''
	name_card_2 = ''


	if card_1 <= 10 and card_1 > 1:
		name_card_1 = str(card_1)
	elif card_1 == 11:
		name_card_1 = 'Jack'
	elif card_1 == 12:
		name_card_1 = 'King'
	elif card_1 == 13:
		name_card_1 = 'Queen'
	elif card_1 == 1:
		name_card_1 = 'Ace'
	print('The card you picked was a ' + name_card_1 + '.')

	if card_2 <= 10 and card_2 > 1:
		name_card_2 = str(card_2)
	elif card_2 == 11:
		name_card_2 = 'Jack'
	elif card_2 == 12:
		name_card_2 = 'King'
	elif card_2 == 13:
		name_card_2 = 'Queen'
	elif card_2 == 1:
		name_card_2 = 'Ace'
	print('The card the other player picked was a ' + name_card_2 + '.')

	if card_1 > card_2:
		print('Nice! You chose the higher card.')
		return bet
	elif card_1 < card_2:
		print('Too bad, your opponent chose a higher card then you.')
		return (-1 * bet)
	else:
		print('You and the other player picked a card with the same value, the game ends in a draw')

#straight needs a number, split needs a list with 2 numbers, street needs a rownumber, six_line needs a list with 2 rownumbers
def roulette(bet, straight, split, street, six_line, corner, trio, basket):
	number = random.randint(1, 36)
	if straight != False:
		bet_straight = straight
		if bet_straight == number:
			straight_won = True
		else:
			straight_won = False
	if split != False:
		bet_split = split
		if bet_split == split[0] or bet_split == split[1]:
			split_won = True
		else:
			split_won = False
	if street != False:
		bet_street_row = street
		bet_street_list = row_to_numbers(bet_street_row)

		street_won = check_list_contains_number(bet_street_list, number)

	if six_line != False:
		bet_six_line_row_1 = six_line[0]
		bet_six_line_row_2 = six_line[1]
		bet_six_line_list = row_to_numbers(bet_six_line_row_1) + row_to_numbers(bet_six_line_row_2)

		six_line_won = check_list_contains_number(bet_six_line_list, number)



coin_flip(10, 'Heads')
print('')
cho_han(10, 'Even')
print('')
pick_a_card(10)