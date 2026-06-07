"""MarketView protocol — causal, point-in-time market access (ADR-0002, ADR-0003, ADR-0006)."""

from __future__ import annotations

from typing import Protocol

from domain.market import Quote
from domain.primitives import Symbol, Timestamp


class MarketView(Protocol):
    """Point-in-time market access for strategies.

  Constraints (binding):
  - Exposes only data with timestamp <= clock.now() (no look-ahead).
  - Does NOT expose future data or arbitrary unbounded history.
  - Strategies depend on this abstraction, never on the engine (ADR-0002).
  - Lookback/rolling computation uses framework-managed estimators (ADR-0006).
  """

    def now(self) -> Timestamp:
        """Current view time (equals clock.now())."""
        ...

    def last(self, symbol: Symbol) -> Quote:
        """Last-known quote for *symbol* at or before now()."""
        ...

    def symbols(self) -> frozenset[Symbol]:
        """Symbols with at least one known quote at or before now()."""
        ...
