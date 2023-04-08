"""Trains a chemprop model on a dataset."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from chemprop.train import chemprop_train


if __name__ == '__main__':
    chemprop_train()
