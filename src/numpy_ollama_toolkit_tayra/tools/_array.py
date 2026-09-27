# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Array implementations for Ollama."""
import numpy as np

__all__ = [
    'add',
]


def add[T: (float, list[float])](
    first: T,
    second: T
) -> T:
    """Adds the two numbers or arrays.

    Parameters
    ----------
    first : T@add
        The first number or array.
    second : T@add
        The second number or array.

    Returns
    -------
    result : T@add
        The sum.

    Notes
    -----
    The arrays must have a same shape
    when you use this function with list of numbers.
    Moreover, the parameters must have the same type.

    Examples
    --------
    The addition of arrays:

    >>> from numpy_ollama_toolkit_tayra.tools import add
    >>> a = [1., 2., 3.]
    >>> b = [4., 5., 6.]
    >>> add(a, b)
    [5., 7., 9.]
    """
    if isinstance(first, list):
        return (np.array(first) + np.array(second)).tolist()
    else:
        return first + second
