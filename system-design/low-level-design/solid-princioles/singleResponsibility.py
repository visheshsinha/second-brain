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