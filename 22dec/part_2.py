

class Player:
    def __init__(self, id, deck):
        self.id, self.deck = (id, deck)

    def won(self, num):
        self.deck = self.deck[1:] + [self.deck[0], num]

    def lost(self):
        self.deck = self.deck[1:]

    def __repr__(self):
        return f"<Player {self.id} -> {', '.join([str(i) for i in self.deck])}>"
    
    @property
    def score(self):
        tot = 0
        for idx, card in enumerate(reversed(self.deck)):
            tot += card * (idx + 1)
        return tot


puzzle_input = [player for player in open('puzzle_input.txt').read().split("\n\n")]

players = []
for p in puzzle_input:
    p = p.split("\n")
    players.append(
        Player(
            int(p[0].replace("Player ", "").replace(":", "")),
            [int(i) for i in p[1:]]
        )
    )


class Game:
    def __init__(self, players, depth=0):
        self.players = players
        self.depth = depth

    def start(self):
        self.rounds = 0
        self.known_decks = []
        self.round()

    def round(self):
        while True:
            self.rounds += 1

            # print(f"\n-- round {self.rounds} --")
            # for player in self.players:
            #     print(f"Player {player.id}'s deck: {', '.join([str(i) for i in player.deck])}")


            start_sub_game = True
            for player in self.players:
                # print(f"Player {player.id} plays: {player.deck[0]}")
                if player.deck[0] > len(player.deck) - 1:
                    start_sub_game = False

            if start_sub_game:
                print(" "*4*self.depth, "... entering a sub game")
                new_players = []
                for player in self.players:
                    new_players.append(
                        Player(
                            player.id,
                            player.deck[1:][:player.deck[0]]
                        )
                    )
                sub_game = Game(new_players, depth=self.depth+1)
                sub_game.start()
                if sub_game.winner.id == 1:
                    self.players[0].won(self.players[1].deck[0])
                    self.players[1].lost()
                else:
                    self.players[1].won(self.players[0].deck[0])
                    self.players[0].lost()
            else:
                if self.players[0].deck[0] > self.players[1].deck[0]:
                    self.players[0].won(self.players[1].deck[0])
                    self.players[1].lost()
                else:
                    self.players[1].won(self.players[0].deck[0])
                    self.players[0].lost()
            
            for player in self.players:
                if len(player.deck) == 0:
                    self.players.remove(player)
            
            if len(self.players) == 1:
                self.winner = self.players[0]
                break

            new_deck = [self.players[0].deck, self.players[1].deck]
            if new_deck not in self.known_decks:
                self.known_decks.append(new_deck)
            else:
                self.winner = self.players[0]
                break


def main():
    game = Game(players)
    game.start()

    print(game.winner)
    print(game.winner.score)

if __name__ == "__main__":
    main()
