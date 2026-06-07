"""Primitive types and enums for the Chronos domain."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

UTC = timezone.utc
from enum import Enum
from typing import NewType

Timestamp = datetime
Symbol = NewType("Symbol", str)


class Granularity(Enum):
    """Descriptive metadata on market events; not a code-path discriminator (ADR-0003)."""

    DAILY = "daily"
    HOURLY = "hourly"
    MINUTE = "minute"
    TICK = "tick"


class Side(Enum):
    BUY = "buy"
    SELL = "sell"


class OrderType(Enum):
    MARKET = "market"


def utc_timestamp(dt: datetime) -> Timestamp:
    """Return a timezone-aware UTC timestamp.

    Raises:
        ValueError: If *dt* is naive or not in UTC.
    """
    if dt.tzinfo is None:
        msg = "timestamp must be timezone-aware"
        raise ValueError(msg)
    if dt.utcoffset() != timedelta(0):
        msg = "timestamp must be in UTC"
        raise ValueError(msg)
    return dt


def symbol(value: str) -> Symbol:
    """Construct a validated symbol identifier."""
    stripped = value.strip()
    if not stripped:
        msg = "symbol must be non-empty"
        raise ValueError(msg)
    return Symbol(stripped)
