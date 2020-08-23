from abc import ABC
from collections.abc import Iterable

class SumOp(ABC, Iterable):
    @property
    def sum(self):
        value = 0
        for v in self:
            if isinstance(v, ManyValues):
                value += v.sum
                return value
            elif isinstance(v, SingleValue):
                value += v.value            
            else:
                value += v
        return value
            

class SingleValue(SumOp):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self
        
        
class ManyValues(list, SumOp):
    def __init__(self, values = None):
        super().__init__()
        if values:
            for value in values:
                self.append(value)
                
 