from abc import ABC
from dataclasses import dataclass
from typing import List, Optional

def main() --> None:
    """
    Main function.
    """
    
    class Behaviour(ABC):

        goodness: float
        category: str
        exclusive: bool


    @dataclass
    class Person:
        name: str
        behaviours: List[Behaviour]

if __name__ == "__main__":
    main()
    # Do the real code
    print('test')

    

    