"""Uses MCTS to interpret a chemprop model."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from chemprop.interpret import chemprop_interpret

if __name__ == '__main__':
    chemprop_interpret()
