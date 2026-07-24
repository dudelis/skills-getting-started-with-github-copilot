"""Shared pytest fixtures for backend API tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """FastAPI test client."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated by restoring the in-memory activities data."""
    # Arrange
    original_activities = deepcopy(activities)

    yield

    # Assert/cleanup
    activities.clear()
    activities.update(original_activities)
