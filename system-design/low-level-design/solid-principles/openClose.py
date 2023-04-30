# Open Close Principle - Open to extension, close to modification

"""
In Python, the interface concept is not explicitly available like in Java.
In Python, an interface is an abstract class which only contains the abstract method but not a single concrete method.
"""

from singleResponsibility import InvoiceCalculator
from abc import ABCMeta, abstractmethod

class InvoiceDAO(metaclass = ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'save') and 
                callable(subclass.save) or 
                NotImplemented)
    
    @abstractmethod
    def save(self, invoice: InvoiceCalculator) -> None:
        # Processes the invoice
        pass

class DataBaseInvoiceDAO(InvoiceDAO):
    def save(self, invoice: InvoiceCalculator) -> None:
        # @Overrides - InvoiceDAO.save()
        # saves the invoice in Database
        pass

class FileInvoiceDAO(InvoiceDAO):
    def save(self, invoice: InvoiceCalculator) -> None:
        # @Overrides - InvoiceDAO.save()
        # saves the invoice in File
        pass

if __name__ == "__main__":
    print(issubclass(DataBaseInvoiceDAO, InvoiceDAO))  # True
    print(issubclass(FileInvoiceDAO, InvoiceDAO))  # True