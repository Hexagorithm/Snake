import settings as st
from game import Game

def main():
    game = Game(st.screen_size,)
    game.run()

if __name__ == "__main__":
    main()