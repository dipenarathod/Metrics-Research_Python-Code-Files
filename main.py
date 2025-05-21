from Shape_Rectangle import Shape,Rectangle
from Circle import Circle
from Square import Square
from Shape_Calculator import ShapeCalculator
def main():
    """Example function using the shape classes."""
    calculator = ShapeCalculator()
    
    # Create various shapes
    rect = Rectangle(5, 10)
    square = Square(7)
    circle = Circle(4)
    
    # Add shapes to calculator
    calculator.add_shape(rect)
    calculator.add_shape(square)
    calculator.add_shape(circle)
    
    # Calculate metrics
    total_area = calculator.total_area()
    avg_perimeter = calculator.average_perimeter()
    largest = calculator.find_largest_shape()
    
    # Print results
    print(f"Total area: {total_area:.2f}")
    print(f"Average perimeter: {avg_perimeter:.2f}")
    
    if largest:
        print(f"Largest shape: {largest.describe()}")


if __name__ == "__main__":
    main()