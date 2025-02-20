"""automaticall run doctests"""

import doctest

import pyrho


def test_doctests():
    """
    Find all modules and attempt to run doctest using pytest
    """
    doctest.testmod(pyrho.core.utils, verbose=True, raise_on_error=True)
