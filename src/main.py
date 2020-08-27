"""
    Exercicio - Pokemon: apanha-los todos
    Premium Minds

    author: Adriano de Araujo Abreu Mourao
    email: mourao [dot] aaa [at] gmail [dot] com
"""


import argparse
from pokemontrainer import PokemonTrainer


def main():
    parser = argparse.ArgumentParser(description=
            'Pokemon: apanha-los todos by Adriano Mourao')
    parser.add_argument('mov_seq', metavar='MovementSequence', type=str,
            help='string containing a movement sequence: N, S, E and O')
    args = parser.parse_args()
    ash = PokemonTrainer()
    try:
        print(ash.move(args.mov_seq))
    except:
        print(
        'Invalid movement sequence: it should be a sequence of N, S, E and O')


if __name__ == '__main__':
    main()


