from game_manager import GameManager

if __name__ == "__main__":
    print(f'START')

    gm = GameManager()
    gm.init_player()
    stop = True
    while stop:
        stop = gm.action()

    print(f'END')