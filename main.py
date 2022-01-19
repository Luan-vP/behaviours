from abc import ABC
from dataclasses import dataclass
import random
from typing import List, Optional
from behaviour import *

@dataclass
class Person:
    name: str
    behaviours: List[Behaviour]

    def speak(self) -> None:
        behavioural_effects = [effect for behaviour in self.behaviours for effect in behaviour.effects]
        print(f"I feel {random.sample(behavioural_effects, 1)[0]}")


def main() -> None:
    """
    Main function.
    """

    dave = Person(name="Dave", behaviours=[Vegan])
    for i in range(10):
        dave.speak()
    

if __name__ == "__main__":
    main()


    

    