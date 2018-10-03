from tensorflow import keras
from tensorflow.nn import relu, softmax
import numpy as np
from connect4 import Connect4Game
from random import randrange
from time import sleep

def build_model():
    md = keras.models.Sequential()
    md.add(keras.layers.Dense(16,activation=relu))
    md.add(keras.layers.Dense(16,activation=relu))
    md.add(keras.layers.Dense(7,activation=softmax))
    md.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'],
            )
    return md

def play_self(md=None):
    """
    returns ([winning moves], [losing moves])
    """
    game = Connect4Game()
    winner = None
    moves = {p:[] for p in range(1, game.n_players+1)}
    while winner == None:
        for player in range(1, game.n_players+1):
            if game.is_full():
                return None, moves, game
            x = prep_board(game, player)
            y = np.argmax(md.predict(x.reshape((1, -1)))) if md else randrange(0, game.width)
            while len(game.board[y]) >= game.height:
                y = randrange(0, game.width)
            game.move(player, y)
            moves[player].append((x, y))
            winner = game.checkwin()
    return winner, moves, game

def prep_board(game, player):
    # pad board
    board = [col + [-1]*(game.height-len(col)) for col in game.board]
    # onehot encode
    features = np.array(board).flatten()
    features = np.concatenate([
        np.array([int(x == player), int(x not in [player, -1])])
        for x in features
        ])
    return features

if __name__ == '__main__':
    md = build_model()
    playargs = []
    randcounter = 100
    traincounter = 1000
    while traincounter > 0:
        print('new game')
        winner, moves, game = play_self(md) if randcounter == 0 else play_self()
        if winner == None:
            continue
        xs = np.stack([x for x, y in moves[winner]])
        ys = np.array([y for x, y in moves[winner]])
        md.fit(xs, ys)
        if randcounter > 0:
            randcounter -= 1
        else:
            game.print_board()
            traincounter -= 1
