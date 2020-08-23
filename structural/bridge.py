from abc import ABC

class Shape:
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer
        self.renderer.what_to_render_as = self

    def draw(self):
        print(self.renderer)

    def __str__(self):
        return str(self.renderer)

class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return self.shape

    @what_to_render_as.setter
    def what_to_render_as(self, value):
        self.shape = value

class VectorRenderer(Renderer):
    def __str__(self):
        return 'Drawing %s as lines' %self.what_to_render_as.name
        

class RasterRenderer(Renderer):
    def __str__(self):
        return 'Drawing %s as pixels' %self.what_to_render_as.name


        
### reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
if __name__ == "__main__":
    triangle = Triangle(VectorRenderer())
    print(triangle)

    square = Square(VectorRenderer())
    square.draw()

    square = Square(RasterRenderer())
    square.draw()
