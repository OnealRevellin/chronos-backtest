"""Universe membership."""

from __future__ import annotations

from dataclasses import dataclass

from domain.primitives import Symbol


@dataclass(frozen=True, slots=True)
class Universe:
    """Static point-in-time universe membership (Phase 1).

  Future: as-of membership queries for survivorship-safe backtests.
  """

    symbols: frozenset[Symbol]

    def __post_init__(self) -> None:
        if not self.symbols:
            msg = "universe must contain at least one symbol"
            raise ValueError(msg)
