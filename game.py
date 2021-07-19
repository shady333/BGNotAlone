import random

from board import Board
from creature import Creature
from astronaut import Astronaut


def main_function():

    print(f'Please choose your side:')
    print(f'0 - Creature')
    print(f'1 - Astronaut')

    player_choice = input('Your choice: ')
    if player_choice == '0':
        print(f'Now you are playing as Creature')
        return 0
    elif player_choice == '1':
        print(f'Now you are playing as Astronaut')
        return 1
    elif player_choice == 'x':
        print(f'See you next time')
        return -1
    else:
        print(f'Please make your choice again')
        print(f'x - for Exit')


def player_actions():
    print(f'Player')
    astronaut = Astronaut()
    creature = Creature()
    board = Board()
    game_phase = 0
    while 1:



        if game_phase == 0:
            print(f'Phase Ia')
            print(f'Available location(s): {astronaut.get_available_locations()}')
            if len(astronaut.get_discard_pile()) >= 1 and astronaut.get_available_will() >= 1:
                print(f'0 - Resist')
            print(f'1 - Give Up')
            print(f'2 - Skip')
            print(f'\n')
            print(astronaut)
            res = int(input('Your choice: '))
            if res == 0:
                will_count = int(input(f'Enter will count, 1 or 2: '))
                if will_count < astronaut.get_available_will() and will_count in range(1, 2) \
                        and len(astronaut.get_discard_pile()) >= 2:
                    if will_count == 1:
                        add_card_from_discard_to_astronaut(astronaut, board)
                        add_card_from_discard_to_astronaut(astronaut, board)
                        astronaut.resist(will_count)
                    if will_count == 2:
                        add_card_from_discard_to_astronaut(astronaut, board)
                        add_card_from_discard_to_astronaut(astronaut, board)
                        add_card_from_discard_to_astronaut(astronaut, board)
                        add_card_from_discard_to_astronaut(astronaut, board)
                        astronaut.resist(will_count)
                else:
                    print(f'Can\'t perform action. Not enough resources')
                    continue
                game_phase = 1
                continue
            elif res == 1:
                astronaut.give_up(astronaut.clear_discard_pile())
                creature.increase_score()
                game_phase = 1
                print(f'Current score: Creature - Astronaut')
                print(f'{creature.get_score()} - {astronaut.get_score()}')
                continue
            elif res == 2:
                game_phase = 1
                continue
            else:
                print(f'Unknown action')
                continue

        if game_phase == 1:
            print(f'Phase Ib')
            print(f'Available location(s): {astronaut.get_available_locations()}')
            res = int(input(f'Please enter location: '))
            if res not in astronaut.get_available_locations():
                print(f'Location {res} is not available.')
                print(f'Please choose different location')
                continue
            astronaut.set_location(res)
            game_phase = 2
            continue

        if game_phase == 2:
            creature.set_targets(board.get_opened_location(), astronaut.get_discard_pile())
            game_phase = 3
            continue

        if game_phase == 3:
            if astronaut.selected_location == creature.creature_location:
                print(f'You have been captured')
                astronaut.remove_will()
                creature.increase_score()
            else:
                print(f'You are lucky')
                astronaut.increase_score()

            print(f'Current score: Creature - Astronaut')
            print(f'{creature.get_score()} - {astronaut.get_score()}')

            if astronaut.get_score() >= 5:
                print(f'Astronaut WIN')
                exit(0)
            if creature.get_score() >= 5:
                print(f'Creature WIN')
                exit(0)

            game_phase = 4
            continue

        if game_phase == 4:
            score = 1
            astronaut.add_card_to_discard_pile(astronaut.selected_location)
            game_phase = 0
            continue

        continue


def add_card_from_discard_to_astronaut(astronaut):
    card_number = random.choice(tuple(astronaut.get_discard_pile()))
    astronaut.remove_card_from_discard_pile(card_number)
    astronaut.add_location(card_number)


def creature_actions():
    print(f'Creature')


if __name__ == "__main__":
    print(f'Welcome to the game')
    res = 111
    while True:
        res = main_function()
        if res in (-1, 0, 1):
            break

    if res == 0:
        creature_actions()
    elif res == 1:
        player_actions()
    else:
        exit(0)