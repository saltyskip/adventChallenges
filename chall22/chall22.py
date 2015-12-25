from copy import deepcopy

MANA_C = 0
I_DAMAGE = 1
D_DAMAGE = 2
T_EFFECT = 3
B_ARMOR = 4
B_MANA = 5
I_HEAL = 6

C_MANA = 500
C_HP = 50
B_HP = 51
B_DAMAGE = 9

EFFECTS = 3
ARMOR = 2
MANA = 1

spells = {
	'missle':(53,0,4,0,0,0,0),
	'drain':(73,0,2,0,0,0,2),
	'shield':(113,0,0,6,7,0,0),
	'poison': (173,0,3,6,0,0,0),
	'recharge': (229,0,0,5,0,101,0)
}

character = [C_HP, C_MANA, 0, []]
boss = [B_HP, B_DAMAGE]
mana_used = []
min_mana = 1000000
global_seq = []

def simulateTurn(myHealth, bossHealth, effects, myMana, manaCost, myTurn, seq):
	myArmor = 0
	newEffects = []
	#apply all effects and update
	global global_seq 
	for effect in effects:
		if effect[T_EFFECT] >= 0:
			myArmor += effect[B_ARMOR]
			myMana += effect[B_MANA]
			myHealth += effect[I_HEAL]
			bossHealth -= effect[D_DAMAGE]
		newEffect = (effect[0], effect[1], effect[2], effect[3], effect[4], effect[5], effect[6])
		if newEffect[T_EFFECT] > 0: newEffects.append(newEffect)
	
	if bossHealth <= 0: 
		global min_mana
		if manaCost < min_mana:
			min_mana = manaCost
			global_seq = seq
			return 	

	if manaCost >= min_mana:
		return

	if myTurn:
		for spell in spells:
			alreadyUsing = False
			for effect in newEffects:
				if spells[spell][MANA_C] == effect[MANA_C]:
					alreadyUsing = True
			if not alreadyUsing and spells[spell][MANA_C] < myMana:
				
				simulateTurn(myHealth, bossHealth, newEffects + [spells[spell]], myMana - spells[spell][MANA_C], manaCost+spells[spell][MANA_C], False, seq + [spell])
	else:
		myHealth -= max(B_DAMAGE - myArmor, 1)
		if myHealth > 0:
			simulateTurn(myHealth, bossHealth, newEffects, myMana, manaCost, True, seq)
simulateTurn(C_HP, B_HP, [], 500, 0, True, [])
print min_mana
print global_seq

