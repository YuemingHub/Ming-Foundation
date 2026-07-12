#!/usr/bin/env python3
"""Shared validation helpers for governed UTF-8 text."""

from __future__ import annotations

from pathlib import Path
import hashlib


def canonical_text_bytes(path: Path) -> bytes:
    """Return UTF-8 text bytes with canonical LF newlines.

    Governed text may appear as LF or CRLF in a local working tree. Validation
    identity follows canonical repository text semantics, not host checkout
    representation.
    """
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    data.decode("utf-8")
    return data


def canonical_text_blob_sha(path: Path) -> str:
    data = canonical_text_bytes(path)
    return hashlib.sha1(
        f"blob {len(data)}\0".encode("ascii") + data
    ).hexdigest()
