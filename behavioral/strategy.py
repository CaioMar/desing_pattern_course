from abc import ABC
import math

class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        discriminant = b*b - 4*a*c
        if discriminant < 0:
            return complex(0, (-1)*discriminant) 
        return complex(discriminant, 0)


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        discriminant = b*b - 4*a*c
        if discriminant < 0:
            return float('nan')
        return complex(discriminant, 0)

class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        disc = self.strategy.calculate_discriminant(a, b, c)
        sqrt = complex(math.sqrt(disc.real), math.sqrt(disc.imag))

        solution_1 = (-b + sqrt)/(2*a)
        solution_2 = (-b - sqrt)/(2*a)
        return solution_1, solution_2

if __name__ == "__main__":
    obj = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
    print(obj.solve(1,1,1))
    
    obj = QuadraticEquationSolver(RealDiscriminantStrategy())
    print(obj.solve(1,1,1))