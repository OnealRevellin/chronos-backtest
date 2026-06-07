"""Strategy protocol."""

from __future__ import annotations

from typing import Protocol

from domain.trading import TargetAllocation
from protocols.market_view import MarketView


class Strategy(Protocol):
    """Pure alpha logic; signal computation lives inside on_data (ADR-0005)."""

    def on_data(self, view: MarketView) -> TargetAllocation | None:
        """Return a target allocation or None to hold current positions."""
        ...
