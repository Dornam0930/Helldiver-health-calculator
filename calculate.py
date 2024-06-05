# placeholder till math functions are coded
from math import floor
hitboxes = ["Overall", "Explosion", "Fortified", "Head", "Chest", "Arm", "Leg"]
max_hp = 125

def func2():
    pass

def calc_all_damage(damage, explosive_damage, armor_values, armor):
    damage_list = []
    damage_listv = []
    remaining_hp = []
    remaining_hpv = []

    if explosive_damage == None:
        for hitbox in hitboxes:
            if hitbox == hitboxes[1] or hitbox == hitboxes[2]:
                damage_list.append("N/A")
                remaining_hp.append("N/A")
            else:
                damage_after_armor = floor(armor_values[armor][hitbox] * damage)
                remainder = max_hp - damage_after_armor
                damage_list.append(damage_after_armor)
                remaining_hp.append(remainder)

        for hitbox in hitboxes:
            if hitbox == hitboxes[1] or hitbox == hitboxes[2]:
                damage_listv.append("N/A")
                remaining_hpv.append("N/A")
            else:
                damage_after_armor = floor(armor_values[f"{armor}V"][hitbox] * damage)
                remainder = max_hp - damage_after_armor
                damage_listv.append(damage_after_armor)
                remaining_hpv.append(remainder)
    else:
        for hitbox in hitboxes:
            if hitbox == hitboxes[1] or hitbox == hitboxes[2]:
                damage_after_armor = floor(armor_values[armor][hitbox] * explosive_damage)
                remainder = max_hp - damage_after_armor
                damage_list.append(damage_after_armor)
                remaining_hp.append(remainder)
            else:
                damage_after_armor = floor(armor_values[armor][hitbox] * damage)
                remainder = max_hp - damage_after_armor
                damage_list.append(damage_after_armor)
                remaining_hp.append(remainder)

        for hitbox in hitboxes:
            if hitbox == hitboxes[1] or hitbox == hitboxes[2]:
                damage_after_armor = floor(armor_values[f"{armor}V"][hitbox] * explosive_damage)
                remainder = max_hp - damage_after_armor
                damage_listv.append(damage_after_armor)
                remaining_hpv.append(remainder)
            else:
                damage_after_armor = floor(armor_values[f"{armor}V"][hitbox] * damage)
                remainder = max_hp - damage_after_armor
                damage_listv.append(damage_after_armor)
                remaining_hpv.append(remainder)

    return damage_list, damage_listv, remaining_hp, remaining_hpv
