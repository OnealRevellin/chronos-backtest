"""Clock protocol — sole source of time (ADR-0004)."""

from __future__ import annotations

from typing import Iterator, Protocol

from domain.primitives import Timestamp


class Clock(Protocol):
    """Drives simulation time; everything reads 'now' from the clock."""

    def now(self) -> Timestamp:
        """Current simulation time."""
        ...

    def __iter__(self) -> Iterator[Timestamp]:
        """Walk forward through time-ordered timestamps."""
        ...
