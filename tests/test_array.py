# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Array test."""
from src.numpy_ollama_toolkit_tayra.tools import add, add_matrix, ShapeMismatchError
import pytest


def test_add_lists():
    result = add(
        [1., 2.],
        [3., 6.]
    )
    assert result == [4., 8.]


def test_add_lists_of_lists():
    a = [[1., 2.], [3., 4.]]
    b = [[2., 3.,], [4., 5.,]]
    result = add_matrix(a, b)
    assert result == [[3., 5.,], [7., 9.,]]


def test_must_fail():
    with pytest.raises(ShapeMismatchError):
        a = [[1., 2.]]
        b = [[1., 2., 3.,]]
        add_matrix(a, b)
