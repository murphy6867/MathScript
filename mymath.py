from unittest import result


class mymath:
    def __init__(self):
        pass
    def add(num1, num2):
        return (f"Answer {num1} + {num2} = {num1 + num2}")
    
    def minus(num1, num2):
        return (f"Answer {num1} - {num2} = {num1 - num2}")
    
    def minus(num1, num2):
        return (f"Answer {num1} - {num2} = {num1 - num2}")
    
    def probability2(num1, num2):
        return (f"Probability is : {num1 * num2}")
    
    def fibo(self, num1):
        if (num1 < 0):
            print("Input not corlected")
        elif (num1 == 0):
            return 0
        elif (num1 == 1):
            return 1
        else:
            return self.fibo(num1 - 1) + self.fibo(num1 - 2)
    
    def fac(self, num1):
        fact = 1
        for i in range(1, num1+1):
            fact = fact * i
        return fact
    
def main():
    #x = float(input("Enter num 1 : "))
    #y = float(input("Enter num 2 : "))
    
    a = mymath()
    print(a.fac(5))
    
if __name__ == "__main__":
    main()