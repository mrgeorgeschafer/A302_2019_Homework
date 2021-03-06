class Calculator:
    """A calculator that will implememt one of 4 mathematical operations,
    in addition to clearing the calculator (resetting to zero).
    """
    
    def __init__(self, val = 0.0):
        self.val = val
    
    def add(self, AddVal):
        """Return the sum of the numbers."""
        self.val = self.val + AddVal
        return self
    
    def sub(self, SubVal):
        """Return the difference of the numbers."""
        self.val = self.val - SubVal
        return self

    def mul(self, MulVal):
        """Return the product of the numbers."""
        self.val = self.val * MulVal
        return self
    
    def div(self, DivVal):
        """Return the quotient of the numbers."""
        self.val = self.val / DivVal
        return self

    def clr(self):
        """Return the sum of the numbers."""
        self.val = 0
        return self
    
    def result(self):
        return self.val
        
    
def assertAlmostEqual(a, b):
    """ A function that tests the approximate equality of two floating point numbers. """
    assert round(a-b, 7) == 0, "{} is not equal to {}.".format(a, b)

c1 = Calculator()    # Create an instance of a calculator
c2 = Calculator(50)    # Create another calculator, initialized with 50

# Test individual methods, and that the two instances properly
# track their own state.
c1.add(2);           assertAlmostEqual(c1.result(), 2)
c1.mul(4);           assertAlmostEqual(c1.result(), 8)
c2.add(50);          assertAlmostEqual(c2.result(), 100)
c1.div(8);           assertAlmostEqual(c1.result(), 1)
c1.sub(-3.);         assertAlmostEqual(c1.result(), 4)
c2.div(c1.result()); assertAlmostEqual(c2.result(), 25)

print ("All tests passed! You have a working calculator!")
