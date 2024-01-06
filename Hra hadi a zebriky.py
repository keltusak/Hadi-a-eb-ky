import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self, dice_roll):
        new_position = self.position + dice_roll
        print(f'Hráč {self.name} hodil {dice_roll} a posunul se na pole {new_position}')
        return new_position

    def win(self):
        print(f'Hráč {self.name} vyhrál!')

class SnakeAndLadderGame:
    def __init__(self, num_players):
        self.players = [Player(chr(65 + i)) for i in range(num_players)]
        self.snakes_and_ladders = {2: 38, 7: 14, 8: 31, 15: 26, 16: 6, 21: 42, 36: 44, 46: 25, 49: 11, 51: 67, 62: 19, 64: 60, 71: 91, 74: 53, 78: 98, 87: 94, 92: 88, 95: 75, 99: 80}

    def snake_or_ladder(self, position):
        if position in self.snakes_and_ladders:
            new_position = self.snakes_and_ladders[position]
            if new_position > position:
                print(f'Žebřík! {position} -> {new_position}')
            else:
                print(f'Had! {position} -> {new_position}')
            return new_position
        return position

    def play(self):
        while True:
            for player in self.players:
                input(f'Je na tahu hráč {player.name}. Stiskněte Enter pro hod kostkou...')
                
                while True:
                    dice_roll = random.randint(1, 6)

                    if dice_roll == 6:
                        print(f'Gratulujeme! Hráč {player.name} hodil 6 a bude házet znovu.')
                        continue  # Hráč hází znovu

                    break

                new_position = player.move(dice_roll)
                new_position = self.snake_or_ladder(new_position)
                # Kontrola, zda hráč dosáhl nebo přesáhl pole 100
                if new_position == 100:
                    player.win()
                    return

                # Kontrola kolize s ostatními hráči
                for other_player in self.players:
                    if other_player != player and other_player.position == new_position:
                        print(f'Kolize! Hráč {other_player.name} posunut o jedno pole zpět.')
                        other_player.position -= 1

                player.position = new_position
                print('\nStav hry:')
                self.print_board()

    def print_board(self):
        for player in self.players:
            print(f'Hráč {player.name} je na poli {player.position}')

if __name__ == "__main__":
    num_players = int(input("Zadejte počet hráčů: "))
    game = SnakeAndLadderGame(num_players)
    game.play()