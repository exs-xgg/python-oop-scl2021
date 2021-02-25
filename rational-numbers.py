

class Rational:
    def __init__(self, n, d):
        r = reduce(n,d)
        self.n = r[0]
        self.d = r[1]
        
    def add(self, otherFrac): # (a/b) + (c/d) = (a*d + c*b) / (b*d)
        denominator = self.d * otherFrac.d
        numerator = self.n * otherFrac.d + self.d * otherFrac.n
        return Rational(numerator,denominator)
        
    def subtract(self, otherFrac): # (a/b) - (c/d) = (a*d - c*b) / (b*d)
        denominator = self.d * otherFrac.d
        numerator = self.n * otherFrac.d - self.d * otherFrac.n
        return Rational(numerator,denominator)
   
    def multiply(self, otherFrac): # (a/b) * (c/d) = (a*c) / (b*d)
        numerator = self.n * otherFrac.n
        denominator = self.d * otherFrac.d
        return Rational(numerator, denominator)
    
    def divide(self, otherFrac): # (a/b) * (c/d) = (a/b) * (d/c)
        numerator = self.n * otherFrac.d
        denominator = self.d * otherFrac.n
        return Rational(numerator, denominator)

    def equal(self, otherFrac):
        if (self.n == otherFrac.n) and (self.d == self.d):
            print("They are Equal")
        else:
            print("Not Equal")
        
    def toString(self):
        return '%d/%d' % self.n, self.d


# ==== function ===

def reduce(n,d):
    if n < d:
        smaller = n
        bigger = d
    else:
        smaller = d
        bigger = n
    
    temp = 1
    for i in range (1, smaller + 1):
        if smaller%i == 0 and bigger%i == 0:
            temp = i
        
        
    n = int(n/temp)
    d = int(d/temp)
    
    return [n,d]