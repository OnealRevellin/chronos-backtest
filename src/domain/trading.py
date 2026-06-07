"""Strategy and portfolio value objects."""

from __future__ import annotations

from dataclasses import dataclass

from domain.constants import WEIGHT_SUM_TOLERANCE
from domain.primitives import OrderType, Side, Symbol, Timestamp


@dataclass(frozen=True, slots=True)
class TargetAllocation:
    """Portfolio weights per symbol. Weights must be >= 0 and sum to 1."""

    weights: tuple[tuple[Symbol, float], ...]

    @classmethod
    def from_weights(cls, weights: dict[Symbol, float] | list[tuple[Symbol, float]]) -> TargetAllocation:
        """Build a validated TargetAllocation from a mapping or sequence."""
        if isinstance(weights, dict):
            items = tuple(weights.items())
        else:
            items = tuple(weights)

        if not items:
            msg = "target allocation must contain at least one weight"
            raise ValueError(msg)

        frozen_items: list[tuple[Symbol, float]] = []
        total = 0.0
        for sym, weight in items:
            if weight < 0.0:
                msg = f"weight for {sym!s} must be >= 0, got {weight}"
                raise ValueError(msg)
            frozen_items.append((sym, weight))
            total += weight

        if abs(total - 1.0) > WEIGHT_SUM_TOLERANCE:
            msg = f"weights must sum to 1, got {total}"
            raise ValueError(msg)

        return cls(weights=tuple(frozen_items))

    def as_dict(self) -> dict[Symbol, float]:
        """Return weights as a dict (for convenience in sizers)."""
        return dict(self.weights)


@dataclass(frozen=True, slots=True)
class Position:
    """Open position using average-cost accounting (Phase 1, long-only)."""

    symbol: Symbol
    quantity: float
    avg_cost: float


@dataclass(frozen=True, slots=True)
class Order:
    """Order intent produced by the sizer."""

    symbol: Symbol
    side: Side
    quantity: float
    order_type: OrderType
    timestamp: Timestamp


@dataclass(frozen=True, slots=True)
class Fill:
    """Execution result for an order."""

    order: Order
    fill_price: float
    fill_quantity: float
    commission: float
    timestamp: Timestamp


@dataclass(frozen=True, slots=True)
class PortfolioState:
    """Snapshot of portfolio at a point in time."""

    timestamp: Timestamp
    cash: float
    positions: tuple[Position, ...]
    equity: float
