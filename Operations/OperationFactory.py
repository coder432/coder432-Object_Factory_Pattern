from Operations.add import add
from Operations.subtract import subtract
from Operations.multiply import multiply
class OperationFactory(object):
    
    __instance = None

    def __init__(self):
        
        if OperationFactory.__instance is not None:
            raise Exception(" Singleton class")
        

        self.operationsMap = {
            '+' : add,
            '-' : subtract,
            '*' : multiply
        }
        OperationFactory.__instance = self


    @staticmethod
    def getInstance():
        if OperationFactory.__instance is None:
            OperationFactory()
        return OperationFactory.__instance


    def getOperation(self,operationString):
        if operationString in self.operationsMap:
            return self.operationsMap[operationString]
        raise NotImplementedError("Class not implemented for {}".format(operationString))
        
        

    def register(self,cls):
        self.operationsMap[cls.operationString] = cls
        
    



