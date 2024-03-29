from astronaut import Astronaut
from board import Board
from creature import Creature

import configparser


class GameManager:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('game_config.ini')

        self.max_rounds = int(config['DEFAULT']['GameRounds'])
        start_will_count = int(config['DEFAULT']['StartWillCount'])
        self.current_phase = 1

        self.board = Board()
        self.astro = Astronaut(start_will_count)
        self.creature = Creature()
        self.current_hero = None


    def get_phase_description(self, phase_number):
        if phase_number == 1:
            print(f'\n***** Exploration *****')
            print(f'Available locations for Astronaut: {self.astro.get_available_locations()}')
            print(f'Astronaut will count - {self.astro.get_available_will()}')
            print(f'\nChoose your action from:')
            print(f'Select location number from {self.astro.get_available_locations()}')
            if len(self.astro.get_discard_pile()) >= 1 and self.astro.get_available_will() >= 1:
                print(f'or \'R\' - Resist')
            print(f'or \'G\' - Give Up')
        elif phase_number == 2:
            print(f'\n***** Hunting *****')
            print(f'\nThe Creature going to hunt on the planet locations - {self.board.get_opened_location()}')
        elif phase_number == 3:
            print(f'\n***** Reckoning *****')
        elif phase_number == 4:
            print(f'\n***** End of Turn *****')

        else:
            print(f'Unknown phase')


    def get_current_phase(self):
        return self.current_phase

    def get_player_input(self):
        player_action = input(f'Your choice: ')

        if player_action == 'x':
            print(f'END')
            exit(0)
        if player_action == 'h':
            print(self.astro)

        return player_action

    def action(self):
        self.get_phase_description(self.get_current_phase())
        if self.get_current_phase() == 1:
            self.operate_phase_one(self.get_player_input())
            return True
        if self.get_current_phase() == 2:
            self.operate_phase_two()
            return True
        if self.get_current_phase() == 3:
            self.operate_phase_three()
            return True
        if self.get_current_phase() == 4:
            self.operate_phase_four()
            return True
        return True

    def operate_phase_one(self, res):
        if res == 'R':
            will_count = int(input(f'Enter will count, 1 or 2: '))
            if will_count <= self.astro.get_available_will():
                counter = 0
                self.astro.remove_will(will_count)
                while len(self.astro.get_discard_pile()) > 0:
                    self.current_hero.add_card_from_discard_pile()
                    counter = counter + 1
                    if will_count == 1 and counter == 2:
                        break
                    if will_count == 2 and counter == 4:
                        break

                if self.astro.get_available_will() <= 0:
                    self.astro_give_up_action()
                return
            else:
                print(f'Can\'t perform action. Not enough resources')
                return
        elif res == 'G':
            self.astro_give_up_action()
            return
        elif int(res) in self.astro.get_available_locations():
            self.astro.set_location(int(res))
            self.current_phase = 2
            return
        else:
            print(f'Incorrect action, please try again')
            return

    def astro_give_up_action(self):
        self.astro.give_up(self.astro.clear_discard_pile())
        self.creature.increase_score()
        print(f'\nCurrent score: Creature - Astronaut')
        print(f'{self.creature.get_score()} - {self.astro.get_score()}')

    def operate_phase_two(self):
        self.creature.set_targets(self.board.get_opened_location(), self.astro.get_discard_pile())
        print(f'Creature start hunting at locations: {self.creature.creature_location}')
        self.current_phase = 3

    def operate_phase_three(self):
        if self.astro.selected_location == self.creature.creature_location:
            print(f'You have been captured by Creature')
            self.astro.remove_will()
            self.creature.increase_score()
        else:
            print(f'You are lucky')
            self.astro.increase_score()

        if self.astro.get_score() >= self.max_rounds:
            print(f'Astronaut WON')
            exit(0)
        if self.creature.get_score() >= self.max_rounds:
            print(f'Creature WON')
            exit(0)

        self.current_phase = 4

    def operate_phase_four(self):
        print(f'Points to WIN - {self.max_rounds}')
        print(f'Current score: Creature - Astronaut')
        print(f'{self.creature.get_score()} - {self.astro.get_score()}')
        self.astro.end_of_phase()
        self.current_phase = 1

    def choose_player(self):
        print(f'Please choose your side:')
        print(f'0 - Creature')
        print(f'1 - Astronaut')
        player_choice = input('Your choice: ')
        if player_choice == '0':
            print(f'\nNow you are playing as Creature')
            self.current_hero = self.creature
            print(f'NOT REALIZED YET')
            exit(1)
        elif player_choice == '1':
            print(f'\nNow you are playing as Astronaut')
            self.current_hero = self.astro
