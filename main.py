from classes.game import Person, tcols
import os
import time

os.system('color')

magic = [{'name': 'Fire', 'cost': 10, 'dmg': 100},
         {'name': 'Thunder', 'cost': 12, 'dmg': 120},
         {'name': 'Blizzard', 'cost': 8, 'dmg': 100}]
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)
"""
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
"""
running = True
i = 0
print(tcols.blue('You are walking through misty old forest.\nFull moon shines in cold night... '))
print(tcols.red('ENEMY ATTACKS!'))
i += 1

while running:
    print('=============================')
    player.choose_action()
    choice = input('Choose action: ')
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked for',dmg,'points of damage. Enemy HP: ',enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = input('Choose magic: ')
        index = int(magic_choice) - 1
        print(tcols.yellow(f'You have chosen {magic[index]["name"].upper()}!'))
        magic_dmg = player.generate_spell_damage(index)
        enemy.take_damage(magic_dmg)
        print('You attacked for',magic_dmg,'points of damage. Enemy HP: ',enemy.get_hp())
   
    if enemy.get_hp() == 0:
        print(tcols.green('You win!'))
        break

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print('Enemy attacked for', enemy_dmg, 'points of damage. Player HP:', player.get_hp())
    if player.get_hp() == 0:
        print(tcols.red('Your enemy has defeated you!'))
        break
    """
    player.choose_magic()
    choice = input('Choose magic: ')
    index = int(choice) - 1
    print('You chose', player.get_spell_name(index))
    """
time.sleep(0.5)
print(tcols.yellow('GAME OVER'))

    



