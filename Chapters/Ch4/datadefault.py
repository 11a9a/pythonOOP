# implementing default values in data classes

from dataclasses import dataclass, field
import random

def getrandomprice():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = field(default=10)
    price: float = field(default_factory=getrandomprice)


b1 = Book()
print(b1)