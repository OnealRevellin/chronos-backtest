"""Reproducibility primitives."""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class SeededRNG:
    """Single injection point for stochastic components."""

    def __init__(self, seed: int) -> None:
        self._seed = seed
        self._stdlib = random.Random(seed)
        self._numpy: np.random.Generator | None = None

    @property
    def seed(self) -> int:
        return self._seed

    @property
    def stdlib(self) -> random.Random:
        """Stdlib RNG (always available, no numpy dependency)."""
        return self._stdlib

    @property
    def numpy(self) -> np.random.Generator:
        """NumPy Generator; lazy-imported for optional numpy-backed components."""
        if self._numpy is None:
            import numpy as np

            self._numpy = np.random.default_rng(self._seed)
        return self._numpy
