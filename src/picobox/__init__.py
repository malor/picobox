"""Dependency injection framework designed with Python in mind."""

from ._box import Box, ChainBox
from ._scopes import Scope, singleton, threadlocal, noscope
from ._stack import push, put, get, pass_


__all__ = [
    'Box',
    'ChainBox',

    'Scope',
    'singleton',
    'threadlocal',
    'noscope',

    'push',
    'put',
    'get',
    'pass_',
]
