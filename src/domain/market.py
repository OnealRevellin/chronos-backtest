"""Market data value objects."""

from __future__ import annotations

from dataclasses import dataclass

from domain.primitives import Granularity, Symbol, Timestamp


@dataclass(frozen=True, slots=True)
class Quote:
    """Point-in-time market snapshot exposed to strategies via MarketView.

  Represents the last-known OHLCV for a symbol at or before clock.now().
  """

    symbol: Symbol
    timestamp: Timestamp
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass(frozen=True, slots=True)
class MarketEvent:
    """Transport unit emitted by DataSource.stream().

    Carries granularity metadata; the engine ingests events to update causal state.
    """

    symbol: Symbol
    timestamp: Timestamp
    open: float
    high: float
    low: float
    close: float
    volume: float
    granularity: Granularity

    def to_quote(self) -> Quote:
        """Convert this event to a strategy-facing Quote."""
        return Quote(
            symbol=self.symbol,
            timestamp=self.timestamp,
            open=self.open,
            high=self.high,
            low=self.low,
            close=self.close,
            volume=self.volume,
        )
