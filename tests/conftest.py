"""Shared fixtures."""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True, scope="session")
def spanish_interface():
    """The tests read the interface in Spanish, as hamrlog's do."""
    from hamrpkt import i18n

    i18n.set_language("es")
