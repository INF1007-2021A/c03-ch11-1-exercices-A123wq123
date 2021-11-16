"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	def __init__(self, __name, power, min_lvl):
		self.__name = __name
		self.power = power
		self.min_lvl = min_lvl

	def make_unarmed(self):
		self.Weapon = ("Unarmed", 20, 0)

	UNARMED_POWER = 20


class Character:

	def __init__(self, __name, max_hp, attack, defense, level, weapon, hp):
		self.__name = __name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = Weapon
		self.hp = hp
		if self.weapon == None:
			self.weapon = Weapon.make_unarmed(self)

	def compute_damage(a, d):
		chance = random.randint(0, 400)
		if chance <= 25:
			crit = 2
		else:
			crit = 1
		((2 * a.level()/5 + 2) * a.weapon.power * (a.attack/d.defense)/50 + 2) * modifier



	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""



def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués
