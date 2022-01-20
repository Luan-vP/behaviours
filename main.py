import json
from dataclasses import dataclass
import random
from typing import List, Optional
from behaviour import *

# TODO: Enums for roles?

@dataclass
class Person:
    '''A person has a name, and a list of behaviours'''
    name: str
    behaviours: List[str]

    def speak(self) -> None:
        '''Describe how the person feels based on their behaviours'''
        selected_behaviour = random.choice(self.behaviours)
        try:
            print(f"{self.name} says: I feel {random.choice(behaviours_dict[selected_behaviour].effects)}")
        except KeyError:
            print(f"{self.name} says: I don't know how being {selected_behaviour} makes me feel")

            # What could I do with yield here..? 
            # yield from self.speak()


def main() -> None:
    """
    Main function.
    """
    with open('people.json') as people_file:
        people = json.load(people_file)
    
    people_dict = {}
    for person in people:
        people_dict[person['name'].lower()] = Person(person['name'], person['behaviours'])

    print(people_dict)

    for person in people_dict.keys():
        people_dict[person].speak()
    

if __name__ == "__main__":
    main()


    

    