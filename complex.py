class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        

    def add(self, other): # (a + bi) + (b + di) = (a+b) + (b+d)i
        realPart = self.real + other.real
        imaginaryPart = self.imaginary + other.imaginary
        return Complex(realPart, imaginaryPart)

    def sub(self, other): 
        realPart = self.real - other.real
        imaginaryPart = self.imaginary - other.imaginary
        return Complex(realPart, imaginaryPart)
    
    def multiply(self, other):
        realPart = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginaryPart = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(realPart, imaginaryPart)
    
    def divide(self, other): # (c+di) ->>> complex conjugate (c-di)
        denom = other.real **2 + other.imaginary **2
        conjugate = Complex(other.real, -other.imaginary)
        