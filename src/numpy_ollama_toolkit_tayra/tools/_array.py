# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Array implementations for Ollama."""
import numpy as np
from ._exceptions import ShapeMismatchError

__all__ = [
    'add',
    'add_matrix',
]


def add[T: (float, list[float])](
    first: T,
    second: T
) -> T:
    """Adds the two numbers or arrays.

    Parameters
    ----------
    first : T
        The first number or array.
    second : T
        The second number or array.

    Returns
    -------
    result : T
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


def _get_shape(
    l: list[list[float]]
) -> tuple[int, ...]:
    """Returns the shape of matrix.

    Parameters
    ----------
    l : list[list[float]]
        The list of lists of floats.

    Returns
    -------
    result : tuple[int, ...]
        The lengths of the rows.
    """
    return tuple([len(r) for r in l])


def add_matrix(
    a: list[list[float]],
    b: list[list[float]]
) -> list[list[float]]:
    """Adds two matrices and returns the sum.

    Parameters
    ----------
    a, b : list[list[float]]
        The two matrices to be added.

    Returns
    -------
    result : list[list[float]]
        The sum of the two matrices.

    Raises
    ------
    ShapeMismatchError
        The shapes of the two parameters must be same.
    TypeError
        The given parameters cannot be interpreted as matrices.

    Notes
    -----
    The sum of two matrices are defined as
    a matrices every whose element is the sum of the original two.

    Examples
    --------
    This is a easy example of addition:

    >>> from numpy_ollama_toolkit_tayra.tools import add_matrix
    >>> a = [
    ...     [1., 2., 3.],
    ...     [3., 4., 5.],
    ... ]
    >>> b = [
    ...     [2., 4., 6.],
    ...     [5., 7., 9.],
    ... ]
    >>> add_matrix(a, b)
    [[3., 6., 9.,], [8., 11., 14.,],]
    """
    shape_a = _get_shape(a)
    shape_b = _get_shape(b)
    shape_ab = shape_a + shape_b
    if min(shape_a) != max(shape_a):
        raise TypeError('`a` is not a valid array.')
    if min(shape_b) != max(shape_b):
        raise TypeError('`b` is not a valid array.')
    if min(shape_ab) != max(shape_ab):
        raise ShapeMismatchError('`a` and `b` must have the same shape.')
    if len(a) != len(b):
        raise ShapeMismatchError('`a` and `b` must have the same shape.')
    a_array = np.array(a)
    b_array = np.array(b)
    return (a_array + b_array).tolist()
