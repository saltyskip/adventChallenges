import math

COST = 0
DAMAGE = 1
ARMOR = 2

BOSS_HP = 103
BOSS_DAMAGE = 9
BOSS_ARMOR =  2

PLAYER_HP = 100


weapons = {
	'Dagger': (8,4,0),
	'Shortsword': (10,5,0),
	'Warhammer': (25,6,0),
	'Longsword': (40,7,0),
	'Greataxe': (74,8,0)
}
armor = {
	'Leather': (13,0,1),
	'Chainmail': (31,0,2),
	'Splintmail': (53,0,3),
	'Bandedmail': (75,0,4),
	'Platemail':(102,0,5),
	'noArmor':(0,0,0),
}

rings = {
	'noRing1': (0,0,0),
	'noRing2': (0,0,0),
	'damage1': (25,1,0),
	'damage2': (50,2,0),
	'damage3': (100,3,0),
	'defense1': (20,0,1),
	'defense2': (40,0,2),
	'defense3': (80,0,3)
}

def defeatedBoss(equipment):
	totalDefense = sum(elem[ARMOR] for elem in equipment)
	totalAttack = sum(elem[DAMAGE] for elem in equipment)
	damagePerTurn = max(1, totalAttack - BOSS_ARMOR)
	turnsToDefeat = math.ceil(float(BOSS_HP)/damagePerTurn)
	if PLAYER_HP - (turnsToDefeat - 1) * max(1, BOSS_DAMAGE - totalDefense) > 0:
		return True
	return False

def findCheapestEquipment():
	currMin = 100000
	currEquip = None
	for wep in weapons.keys():
		for arm in armor.keys():
			for ring1 in rings.keys():
				for ring2 in rings.keys():
					if ring1 == ring2: continue
					equipment = [weapons[wep],armor[arm],rings[ring1], rings[ring2]]
					cost = sum(elem[COST] for elem in equipment)
					if defeatedBoss(equipment) and cost < currMin:
						currMin = cost
						currEquip = equipment
	print currMin
	print currEquip

def findExpensiveLoss():
	currMax = 0
	currEquip = None
	for wep in weapons.keys():
		for arm in armor.keys():
			for ring1 in rings.keys():
				for ring2 in rings.keys():
					if ring1 == ring2: continue
					equipment = [weapons[wep],armor[arm],rings[ring1], rings[ring2]]
					cost = sum(elem[COST] for elem in equipment)
					if not defeatedBoss(equipment) and cost > currMax:
						currMax = cost
						currEquip = equipment
	print currMax
	print currEquip


#findCheapestEquipment()
findExpensiveLoss()




