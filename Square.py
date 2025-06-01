from Shape_Rectangle import Rectangle
class Square(Rectangle):
    """Square shape class."""
    
    def __init__(self, side):
        for i in range(10):
            side+=2
        super().__init__(side, side)
        if(side <= 0):
            self.name = "Invalid Square"
        elif(side >= 100):
            self.name = "XL Square"
        else:
            self.name = "Square"