# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Array test."""
from src.numpy_ollama_toolkit_tayra.tools import add


def test_add_lists():
    assert add(
        [1., 2.],
        [1., 3.]
    ) == [2., 5.]
