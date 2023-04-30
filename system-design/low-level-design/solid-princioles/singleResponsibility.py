class Marker:
    def __init__(self, name: str, colour: str, year: int, price: float) -> None:
        self.name = name
        self.colour = colour
        self.year = year
        self.price = price

"""
Invoice Class Responsibilities:
1. Calculating the Total
2. Printing the Invoice
3. Saving to Database
"""
class Invoice:
    def __init__(self, marker: Marker, qty: int) -> None:
        self.marker = marker
        self.qty = qty
    
    def calculateTotal(self) -> int:
        price = self.marker.price * self.qty
        return price
    
    def printInvoice(self) -> None:
        # prints the invoice
        pass

    def saveToDB(self) -> None:
        # saves to DB
        pass


"""
Converting this into Single Responsibility by breaking up the responsibilities in different classes
"""

# Any calculation logic will change in this class & not affect other classes
class InvoiceCalculator:
    def __init__(self, marker: Marker, qty: int) -> None:
        self.marker = marker
        self.qty = qty
    
    def calulateTotal(self) -> int:
        price = self.marker.price * self.qty
        return price

class InvoicePrinter:
    def __init__(self, invoice: InvoiceCalculator) -> None:
        self.invoice = invoice
    
    def printInvoice(self) -> None:
        # prints the invoice
        pass

# Data Access Layer - save in DB / in file / send in MQ, anywhere
class InvoiceDAO:
    def __init__(self, invoice: InvoiceCalculator) -> None:
        self.invoice = invoice

    def saveToDB(self) -> None:
        # saves to DB
        pass