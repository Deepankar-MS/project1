"""Core functionality for project1."""

import hashlib
import hmac
import os

# In-memory user store: {username: (salt_hex, dk_hex)}
_users: dict = {}

_PBKDF2_ITERATIONS = 600_000
_PBKDF2_HASH = "sha256"
_DK_LEN = 32  # bytes


def _hash_password(password: str, salt: bytes) -> str:
    """Return the PBKDF2-HMAC-SHA256 hex digest for *password* + *salt*."""
    dk = hashlib.pbkdf2_hmac(
        _PBKDF2_HASH,
        password.encode("utf-8"),
        salt,
        _PBKDF2_ITERATIONS,
        dklen=_DK_LEN,
    )
    return dk.hex()


def register_user(username: str, password: str) -> bool:
    """Register a new user with the given username and password.

    Returns True on success, False if the username is already taken.
    """
    if not username or not password:
        raise ValueError("Username and password must not be empty.")
    if username in _users:
        return False
    salt = os.urandom(16)
    _users[username] = (salt.hex(), _hash_password(password, salt))
    return True


def login(username: str, password: str) -> bool:
    """Validate credentials and return True if the login is successful.

    Returns False when the username does not exist or the password is wrong.
    Uses a constant-time comparison to avoid timing attacks.
    """
    if not username or not password:
        return False
    entry = _users.get(username)
    if entry is None:
        return False
    salt_hex, stored_dk = entry
    candidate_dk = _hash_password(password, bytes.fromhex(salt_hex))
    return hmac.compare_digest(stored_dk, candidate_dk)


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello from project1, my name is agent, hello from Agent {name}!"
