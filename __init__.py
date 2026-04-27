"""project1 - Base project with no dependencies."""

__version__ = "1.0.0"

from .core import greet, login, register_user

__all__ = ["greet", "login", "register_user"]
