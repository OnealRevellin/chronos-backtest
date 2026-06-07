"""Sizer protocol."""

from __future__ import annotations

from typing import Protocol

from domain.trading import Order, PortfolioState, TargetAllocation


class Sizer(Protocol):
    """Translates TargetAllocation into executable orders."""

    def size(self, target: TargetAllocation, state: PortfolioState) -> list[Order]:
        """Produce orders to move from current state toward *target*."""
        ...
