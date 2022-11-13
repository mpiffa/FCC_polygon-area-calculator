import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        """
        An instance of a Rectangle represented as a string should look like: Rectangle(width=5, height=10)
        """
        string_to_print = f"{type(self).__name__}(width={self.width}, height={self.height})"
        return string_to_print

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        """ 
        Returns area (width * height) 
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Returns perimeter (2 * width + 2 * height)
        """
        return 2 * (self.height + self.width)

    def get_diagonal(self):
        """
        Returns diagonal ((width ** 2 + height ** 2) ** .5)
        """
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        """
        Returns a string that represents the shape using lines of "*". The number of lines should 
        be equal to the height and the number of "*" in each line should be equal to the width. 
        There should be a new line (\n) at the end of each line. If the width or height is larger than 50, 
        this should return the string: "Too big for picture.".
        """
        picture = ""
        if self.height < 50 and self.width < 50:
            for n in range(self.height):
                picture += "*" * self.width +"\n"
            return picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        """
        Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in 
        shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and 
        a height of 8 could fit in two squares with sides of 4.
        """
        if  self.width < shape.width or self.height < shape.height:
            return 0
        elif self.width == shape.width and self.height == shape.height:
            return 1
        else: 
            number = math.floor(self.width / shape.width) * math.floor(self.height / shape.height)
            return number
        


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side, side)

    def __str__(self):
        """
        An instance of a Square represented as a string should look like: Square(side=9)
        """
        string_to_print = f"{type(self).__name__}(side={self.height})"
        return string_to_print
    def set_side(self, side):
        self.width = self.height = side

    def set_height(self, height):
        self.width = self.height = height

    def set_width(self, width):
        self.width = self.height = width
    