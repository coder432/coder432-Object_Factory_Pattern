from Operations.IOperations import IOperation

class subtract(IOperation):
    
    operationString = '-'
    
    @staticmethod
    def operate(operand1,operand2):
        return operand1 - operand2

    @classmethod
    def showOperation(cls, operand1, operand2):
        return str(operand1) + cls.operationString + str(operand2) 