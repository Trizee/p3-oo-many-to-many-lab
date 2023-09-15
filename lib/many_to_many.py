class Author:
    
    def __init__(self,name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    
    def __init__(self,title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        if isinstance(author,Author):
            self._author = author
        else:
            raise Exception('Not a valid Author')
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,book):
        if isinstance(book,Book):
            self._book = book
        else:
            raise Exception('Not a valid book')
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,date):
        if isinstance(date,str):
            self._date = date
        else:
            raise Exception('Not a valid date')
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,amount):
        if isinstance(amount,int):
            self._royalties = amount
        else:
            raise Exception('Not a valid amount')

    @classmethod    
    def contracts_by_date(cls):
        return sorted(cls.all,key=lambda c: c.date)
        

Joe = Author('Joe')
bok = Book('Bok')
con1 = Contract(Joe,bok,'01/01/01',123123)

print(con1)

Joe.contracts()