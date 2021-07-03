from board import Board
from creature import Creature
from player import Player


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
    player = Player()
    creature = Creature()
    board = Board()
    game_phase = 0
    while 1:
        if game_phase == 0:
            print(f'Phase Ia')
            print(f'0 - Resist')
            print(f'1 - Give Up')
            print(f'2 - Skip')
            res = int(input('Your choice: '))
            if res == 0:
                player.resist()
                game_phase = 1
                continue
            elif res == 1:
                player.give_up()
                game_phase = 1
                continue
            elif res == 2:
                game_phase = 1
                continue
            else:
                print(f'Unknown action')
                break

        if game_phase == 1:
            print(f'Phase Ib')
            print(f'Available location(s): {player.get_available_locations()}')
            res = int(input(f'Please enter location: '))
            player.set_location(res)
            game_phase = 2
            continue

        if game_phase == 2:
            creature.set_targets(board.opened_locations, board.discard_pile)
            game_phase = 3
            continue

        if game_phase == 3:
            if player.selected_location == creature.creature_location:
                print(f'You have been captured')
            else:
                print(f'You are lucky')

            game_phase = 4
            continue

        if game_phase == 4:
            score = 1
            board.dicard_card(player.selected_location)
            game_phase = 0
            continue

        continue


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