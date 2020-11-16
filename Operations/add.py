from Operations.IOperations import IOperation
class add(IOperation):
    
    operationString = '+'
    
    @staticmethod
    def operate(operand1,operand2):
        return operand1 + operand2

  

if  __name__ == "__main__":
    print(add.operate(1,2))
    