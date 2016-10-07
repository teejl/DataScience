""" Characters 

I plan on building a program that will coordinate to characters in a rpg video game. My goal is for the characters to be able to have defined stats, and if they are to level up there stats will change according to a different set of function of my choosing. 

So far the ideas of stats I have chosen are:
Health
Attack
Stregnth
Speed
Dexterity
Defence
Wisdom
Intelligence
...

So there are many different possibilities. At first I will start off with a single set of stats, and find a way to incorporate different stats.

"""

def char(char_name, level,  health, attack, stregnth, defence, speed):
	# the goal of this function is to define a character and his stats
	# the input is the information the output is the vector

	char_name = [level, health, attack, stregnth, defence, speed]

def char_levelup(char_name):
	# the goal of this function is to adjust character stats based on the stats of the character
	# the input is the character and the out put is the new character with new stats

	for i in char_name:
		i += 1



