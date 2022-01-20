from abc import ABC
import json
from dataclasses import *
import random
from typing import List, Optional

@dataclass
class Behaviour:

    goodness: float
    category: str
    effects: List[str]

json_data = json.load(open('behaviours.json'))

behaviours_dict = {}
for behaviour in json_data:
    behaviours_dict[behaviour['name'].lower()] = Behaviour(behaviour['goodness'], behaviour['category'], behaviour['effects'])

print(behaviours_dict)
