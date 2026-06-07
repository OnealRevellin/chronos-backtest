"""Portfolio protocol."""

from __future__ import annotations

from typing import Protocol

from domain.trading import Fill, PortfolioState


class Portfolio(Protocol):
    """Authoritative ledger; must conserve value."""

    def apply(self, fill: Fill) -> None:
        """Apply a fill to the ledger."""
        ...

    def state(self) -> PortfolioState:
        """Current portfolio snapshot."""
        ...
