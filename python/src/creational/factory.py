from abc import ABC, abstractmethod
from typing import Optional

class Product(ABC):

    """
    Product interface class

    ...

    Attributes
    ----------
    name : str
        The name of the product
    price : float
        The price of the product

    Methods
    -------

    get_price()
        Return the product's price
    get_description()
        Return the product's description

    """

    def __init__(self, name: Optional[str] = None, price:Optional[float] = None) -> None:
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self) -> str:
        """Return the product's description"""
        pass

    @abstractmethod
    def get_price(self) -> float:
        """Returns the product's price"""
        pass


class Electronics(Product):
    
    """
    Eeletronic's product class

    ...

    Attributes
    ----------
    name : str
        The name of the eletronic
    price : float
        The price of the eletronic
    warranty_years: int
        The warranty years of the eletronic

    Methods
    -------

    get_price()
        Return the eletronic's price
    get_description()
        Return the eletronic's description

    """

    def __init__(self, name: str, price: float, warranty_years: int) -> None:
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def get_price(self) -> float:
        return self.price
    
    def get_description(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, Warranty: {self.warranty_years} years"
    
class Book(Product):

    """
    Book's product class

    ...

    Attributes
    ----------
    title : str
        The title of the book
    price : float
        The price of the book
    author: str
        The author of the book

    Methods
    -------

    get_price()
        Return the book's price
    get_description()
        Return the book's description

    """

    def __init__(self, title: str, price: float, author: str) -> None:
        super().__init__(name=title, price=price)
        self.author = author

    def get_price(self) -> float:
        return self.price
    
    def get_description(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, Author: {self.author}"
    
class Clothing(Product):
    """
    Clothing's product class

    ...

    Attributes
    ----------
    name : str
        The name of the clothing
    price : float
        The price of the clothing
    size: str
        The size of the clothing

    Methods
    -------

    get_price()
        Return the clothing's price
    get_description()
        Return the clothing's description

    """

    def __init__(self, name: str, price: float, size: str) -> None:
        super().__init__(name, price)
        self.size = size

    def get_price(self) -> float:
        return self.price
    
    def get_description(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, Size: {self.size}"
    
class ProductFactory(ABC):

    """
    ProductFactory is the factory interface for the product

    ...

    Methods
    -------

    create : Product
        Return an instance of the Product class
    """

    @abstractmethod
    def create(self) -> Product:
        """Factory method"""
        pass

class EletronicFactory(ProductFactory):

    """
    EletronicFactory is the factory interface for the Eletronic

    ...

    Methods
    -------

    create : Eletronic
        Return an instance of the Eletronic class
    """

    def create(self) -> Product:
        return Electronics(name="Smatphone", price=699.99, warranty_years=2)
    
class BookFactory(ProductFactory):

    """
    BookFactory is the factory interface for the Book

    ...

    Methods
    -------

    create : Book
        Return an instance of the Book class
    """

    def create(self) -> Product:
        return Book(title="The Lord of the Rings", price=59.99, author="J.R.R. Tolkien")
    
class ClothingFactory(ProductFactory):

    """
    ClothingFactory is the factory interface for the Clothing

    ...

    Methods
    -------

    create : Clothing
        Return an instance of the Clothing class
    """

    def create(self) -> Product:
        return Clothing(name="T-shirt", price=19.99, size="L")
    

def client_order(factory: ProductFactory) -> None:
    product = factory.create()
    print(f"Client: I'm currently creating a {product.__class__.__name__}")
    print(f"Description - {product.get_description()}\n")    

if __name__ == "__main__":

    print("App: Launching with Electronics Factory")
    client_order(EletronicFactory())

    print("App: Launching with Book Factory")
    client_order(BookFactory())

    print("App: Launchin with Clothing Factory")
    client_order(ClothingFactory())