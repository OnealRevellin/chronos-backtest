"""ExecutionModel protocol."""

from __future__ import annotations

from typing import Protocol

from domain.trading import Fill, Order
from protocols.market_view import MarketView


class ExecutionModel(Protocol):
    """Simulates order execution (fills, costs, latency)."""

    def execute(self, order: Order, view: MarketView) -> Fill:
        """Simulate execution of *order* against the causal market view."""
        ...
