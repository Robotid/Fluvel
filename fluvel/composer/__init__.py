from fluvel.composer.Factory import Factory
from fluvel.composer.Animator import Animator
from fluvel.composer.Prefab import Prefab

__all__ = [
    "Factory",
    "Animator",
    "Prefab"
]

from typing import TypeAlias
from fluvel.core.abstract_models.ABCAbstractPage import Page

Canvas: TypeAlias = Page