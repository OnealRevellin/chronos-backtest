"""DataSource protocol."""

from __future__ import annotations

from typing import Iterator, Protocol

from domain.market import MarketEvent
from domain.primitives import Timestamp
from domain.universe import Universe


class DataSource(Protocol):
    """Streams market events in timestamp order for a universe and date range."""

    def stream(
        self,
        universe: Universe,
        start: Timestamp,
        end: Timestamp,
    ) -> Iterator[MarketEvent]:
        """Yield MarketEvents in strict timestamp order."""
        ...
