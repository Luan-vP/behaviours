from abc import ABC
from dataclasses import dataclass
import random
from typing import List, Optional

@dataclass
class Behaviour(ABC):

    goodness: float
    category: str
    effects: List[str]

class Vegan(Behaviour):
    """
    Vegan behaviour
    """

    goodness = 0.8
    category = "diet"
    effects = ["healthy", "ethical"]