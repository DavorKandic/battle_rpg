from classes.game import Person, bcolors


magic = [{'name': 'Fire', 'cost': 10, 'dmg': 60},
         {'name': 'Thunder', 'cost': 10, 'dmg': 80},
         {'name': 'Blizzard', 'cost': 10, 'dmg': 60}]
player = Person(460, 65, 60, 34, magic)

# Testing our player object
print('PHYSICAL ATTACK TEST')
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
print('MAGIC ATTACK TEST')
print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
print('TAKING DAMAGE TEST')
print(f'Current HP is: {player.hp}')
dmg1 = player.generate_damage()
dmg2 = player.generate_damage()
dmg3 = player.generate_damage()
player.take_damage(dmg1)
print(f'After taking damage of {dmg1} HP is {player.hp}')
player.take_damage(dmg2)
print(f'After taking damage of {dmg2} HP is {player.hp}')
player.take_damage(dmg3)
print(f'After taking damage of {dmg3} HP is {player.hp}')
      



