# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Exceptions."""
__all__ = ['ShapeMismatchError']


class ShapeMismatchError(Exception):
    """The array shape is not valid.
    
    Parameters
    ----------
    *args : Any
        The arguments.
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
