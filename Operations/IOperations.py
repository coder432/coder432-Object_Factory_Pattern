class IOperation(object):
    
    def operate(self, *parameter_list):
        raise NotImplementedError

    def showOperation(self, *parameter_list):
        raise NotImplementedError


    