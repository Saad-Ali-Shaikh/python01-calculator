class Calculator:
    def add(self, x,  y):
        return x + y
    def sub(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x,y):
        if y == 0:
            return 'Cannot divide by zero'
        return x/y
