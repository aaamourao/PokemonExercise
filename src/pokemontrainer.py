"""
    Exercicio - Pokemon: apanha-los todos
    Premium Minds

    author: Adriano de Araujo Abreu Mourao
    email: mourao [dot] aaa [at] gmail [dot] com
"""


class PokemonTrainer:
    '''A fantastic being, who lives in the amazing PokeWorld.'''

    # Map which shows the relation of each movement command and their meaning
    # in a 2D coordinate system.
    mov_map = {
            'N': {
                'axis': 0,
                'value': 1
            },
            'S': {
                'axis': 0,
                'value': -1
            },
            'E': {
                'axis': 1,
                'value': 1
            },
            'O': {
                'axis': 1,
                'value': -1
            }
    }

    def __init__(self, init_pos=[0, 0]) -> 'PokemonTrainer object':
        '''Creates a Pokemon Trainer object on any position coordinate,
        default (0, 0). '''
        # coordinates of current position
        self.pos = init_pos
        # hash table of visited coordinates
        self.visited = set()
        # mark if pokemon trainer has started his journey
        self.moved = False

    def move(self, cmd: str) -> int:
        '''Move the Pokemon Trainer around the Pokemon World. It returns
        how many Pokemons were captured on this single movement.'''
        captured_now = 0
        # if it's the first movement, they get a pokemon from initial pos
        if not self.moved:
            captured_now += 1
            self.visited.add(str(self.pos))
            self.moved = True
        # move around PokeWorld
        for step in cmd:
            self.pos[PokemonTrainer.mov_map[step.upper()]['axis']] += \
                    PokemonTrainer.mov_map[step.upper()]['value']
            pos_str = str(self.pos)
            if pos_str not in self.visited:
                captured_now += 1
                self.visited.add(pos_str)
        return captured_now

    @property
    def captured(self):
        '''Return the total number of captured pokemons in the Pokemon
        Trainer's life.'''
        return len(self.visited)


