from Operations.OperationFactory import OperationFactory
from Operations.devide import devide
if __name__ == "__main__":

    
    factory = OperationFactory.getInstance()
    factory.register(devide)
    while(True):
        line = input().split()
        op1,operation,op2 = int(line[0]),line[1],int(line[2])
        print(factory.getOperation(operation).operate(op1,op2))



