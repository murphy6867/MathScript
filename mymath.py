
from math import factorial


class mymath:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.factorial = factorial
    def add(self):
        return (f"Answer {self.num1} + {self.num2} = {self.num1 + self.num2}")
    
    def minus(self):
        return (f"Answer {self.num1} - {self.num2} = {self.num1 - self.num2}")
    
    def probability2(self):
        return (f"Probability is : {self.num1 * self.num2}")
    
    def factorial(n):
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        else:
            return self.factorial(n - 1) + self.factorial(n - 2)
        
        
def main():
    x = float(input("Enter num 1 : "))
    y = float(input("Enter num 2 : "))
    
    test = mymath(x, y)
    
    print(test.add())
    
if __name__ == "__main__":
    main()