import random
import sys

startGame = input("Do you want to play the game of BlackJack? Type 'y' or 'n': ").lower()
if startGame == 'y':
    print("""
          .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
              |  \/ K|                            _/ |                
              '------'                           |__/
          """)
else:
    print('')

