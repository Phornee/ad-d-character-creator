import random

STR = 0
CON = 1
DEX = 2
INT = 3
WIS = 4
CHA = 5

def roll_dice_stats():
    rolls = []
    for i in range(0, 3):
        rolls.append(random.randint(1, 6))
    final_stat = rolls[0] + rolls[1] + rolls[2]
    return final_stat

def roll_dice_stats_cool():
    rolls = []
    for i in range(0, 4):
        rolls.append(random.randint(1, 6))

    rolls.sort()
    final_stat = rolls[1] + rolls[2] + rolls[3]
    return final_stat

def roll_dice_stats_epic():
    rolls = []
    for i in range(0, 6):
        rolls.append(random.randint(1, 6))

    rolls.sort()
    final_stat = rolls[3] + rolls[4] + rolls[5]
    return final_stat

def generate_stats():
    stats = []
    for i in range(0, 6):
        stats.append(roll_dice_stats())
    return stats

def fullfill_req(stats, char_class):
    if char_class == 'war':
        return stats[STR] >= 9
    elif char_class == 'pal':
        return stats[STR] >= 12 and stats[CON] >= 9 and stats[WIS] >= 13 and stats[CHA] >= 17
    elif char_class == 'ran':
        return stats[STR] >= 13 and stats[CON] >= 14 and stats[DEX] >= 13 and stats[WIS] >= 14
    elif char_class == 'mag':
        return stats[INT] >= 9
    elif char_class == 'cle':
        return stats[WIS] >= 9
    elif char_class == 'dru':
        return stats[WIS] >= 12 and stats[CHA] >= 15
    elif char_class == 'thi':
        return stats[DEX] >= 9
    elif char_class == 'bar':
        return stats[DEX] >= 12 and stats[INT] >= 13 and stats[CHA] >= 15
    else:
        raise Exception("Character class {} not supported yet!.".format(char_class))

def apply_race_mods(stats, race):
    if race == 'elf':
        stats[DEX] = stats[DEX] + 1
        stats[CON] = stats[CON] - 1
    elif race == 'dwarf':
        stats[CON] = stats[CON] + 1
        stats[CHA] = stats[CHA] - 1

def create_char(name, char_class, race, level):
    found = False
    stats = []
    while not found:
        stats = generate_stats()
        apply_race_mods(stats, race)
        found = fullfill_req(stats, char_class)

    print('Name: {} | Class: {} | Race: {}'.format(name, char_class, race))
    print('STR: {}'.format(stats[0]))
    print('CON: {}'.format(stats[1]))
    print('DEX: {}'.format(stats[2]))
    print('INT: {}'.format(stats[3]))
    print('WIS: {}'.format(stats[4]))
    print('CHA: {}'.format(stats[5]))

    return stats

