"""End-to-end tests for story-07-01-01: greet functionality."""

import project1
from project1 import greet


def test_greet_returns_string():
    """greet should return a string."""
    result = greet("Alice")
    assert isinstance(result, str)


def test_greet_contains_name():
    """greet should include the provided name in the response."""
    result = greet("Alice")
    assert "Alice" in result


def test_greet_default_message():
    """greet should return the expected greeting message."""
    result = greet("Alice")
    assert result == "Hello from project1, my name is agent, hello from Agent Alice!"


def test_greet_different_names():
    """greet should work with different names."""
    for name in ["Bob", "Charlie", "World"]:
        result = greet(name)
        assert name in result
        assert result == f"Hello from project1, my name is agent, hello from Agent {name}!"


def test_module_version():
    """project1 package should expose a version."""
    assert hasattr(project1, "__version__")
    assert project1.__version__ == "1.0.0"


def test_greet_exported():
    """greet should be exported from the project1 package."""
    assert "greet" in project1.__all__
