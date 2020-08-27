"""
    Exercicio - Pokemon: apanha-los todos
    Premium Minds

    author: Adriano de Araujo Abreu Mourao
    email: mourao [dot] aaa [at] gmail [dot] com
"""


import pytest
from ..pokemontrainer import PokemonTrainer


class TestPokemonTrainer:
    '''Unit tests for PokemonTrainer'''

    def test_example(self):
        '''Example described at the PDF.'''
        ash = PokemonTrainer()
        assert ash.move('E') == 2
        misty = PokemonTrainer()
        assert misty.move('NESO') == 4
        brock = PokemonTrainer()
        assert brock.move('NSNSNSNSNS') == 2

    def test_move_short(self):
        '''Test sequence of moves in the pokemon world with same object.'''
        ash = PokemonTrainer()
        assert ash.move('E') == 2
        assert ash.move('O') == 0
        assert ash.move('N') == 1
        assert ash.move('S') == 0
        assert ash.move('S') == 1
        assert ash.move('N') == 0
        assert ash.move('N') == 0
        assert ash.move('N') == 1


    def test_move_long(self):
        ash = PokemonTrainer()
        assert ash.move('NESO') == 4
        assert ash.move('SONE') == 3
        assert ash.move('NOSE') == 1
        assert ash.move('SENO') == 1
        misty = PokemonTrainer()
        assert misty.move('NESOSONENOSESENO') == 9

    def test_captured(self):
        ash = PokemonTrainer()
        ash.move('NESO')
        ash.move('SONE')
        ash.move('NOSE')
        ash.move('SENO')
        assert ash.captured == 9
        misty = PokemonTrainer()
        misty.move('NESOSONENOSESENO')
        assert misty.captured == 9



