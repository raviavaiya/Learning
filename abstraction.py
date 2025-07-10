from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"
    
class Square(Shape):
    def draw(self):
        return "Drawing a Square"
    
c = Circle()
s = Square()
print(c.draw())  # Output: Drawing a Circle
print(s.draw())  # Output: Drawing a Square