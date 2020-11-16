from abc import ABCMeta as ABC,abstractmethod
class IOperation(metaclass = ABC):
    
    @abstractmethod
    def operate(self, *parameter_list):
        raise NotImplementedError

    @abstractmethod
    def showOperation(self, *parameter_list):
        raise NotImplementedError


    