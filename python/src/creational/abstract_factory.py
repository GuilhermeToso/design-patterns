from abc import ABC, abstractmethod
from typing import Optional

class Helmet(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.protection: Optional[int] = None
        self.duration: Optional[int] = None
        self.ornament: Optional[str] = None

    @abstractmethod
    def get_protection(self) -> int:
        """Returns protection points"""
        pass

    @abstractmethod
    def get_duration(self) -> int:
        """Returns duration points"""
        pass


    @abstractmethod
    def update_duration(self) -> int:
        """Update duration points"""
        pass


    @abstractmethod
    def get_ornament(self) -> str:
        """Returns ornament"""
        pass

class Clothe(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.protection: Optional[int] = None
        self.duration: Optional[int] = None
        self.design: Optional[str] = None

    @abstractmethod
    def get_protection(self) -> int:
        """Returns protection points"""
        pass

    @abstractmethod
    def get_duration(self) -> int:
        """Returns duration points"""
        pass

    @abstractmethod
    def update_duration(self) -> int:
        """Update duration points"""
        pass

    @abstractmethod
    def get_design(self) -> str:
        """Returns design"""
        pass

class Weapon(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.duration: Optional[int] = None
        self.damage: Optional[int] = None

    @abstractmethod
    def get_duration(self) -> int:
        """Returns duration points"""
        pass

    @abstractmethod
    def update_duration(self) -> int:
        """Update duration points"""
        pass

    @abstractmethod
    def attack(self):
        """Attack"""
        pass


class IronHelmet(Helmet):

    def __init__(self) -> None:
        super().__init__()
        self.duration = 10
        self.protection = 20
        self.ornament = "iron wings"


    def get_duration(self) -> int:
        return self.duration
    

    def get_protection(self) -> int:
        return self.protection
    
    def update_duration(self, value: int) -> int:
        self.duration = self.duration - value
    
    def get_ornament(self) -> str:
        return f"{self.__class__.__name__} has {self.ornament}"
    
class SteelHelmet(Helmet):

    def __init__(self) -> None:
        super().__init__()
        self.duration = 20
        self.protection = 30
        self.ornament = "steel horns"

    def get_duration(self) -> int:
        return self.duration

    def get_protection(self) -> int:
        return self.protection
    
    def update_duration(self, value: int) -> int:
        self.duration = self.duration - value
    
    def get_ornament(self) -> str:
        return f"{self.__class__.__name__} has {self.ornament}"
    
class IronClothe(Clothe):

    def __init__(self) -> None:
        super().__init__()
        self.duration = 30
        self.protection = 30
        self.design = "raw"

    def get_duration(self) -> int:
        return self.duration
    
    def get_protection(self) -> int:
        return self.protection
    
    def update_duration(self, value: int) -> int:
        self.duration = self.duration - value
    
    def get_design(self) -> str:
        return f"{self.__class__.__name__} has a {self.design} design"
    
class SteelClothe(Clothe):
    
    def __init__(self) -> None:
        super().__init__()
        self.duration = 40
        self.protection = 30
        self.design = "detailed"

    def get_duration(self) -> int:
        return self.duration
    
    def get_protection(self) -> int:
        return self.protection
    
    def update_duration(self, value: int) -> int:
        self.duration = self.duration - value
    
    def get_design(self) -> str:
        return f"{self.__class__.__name__} has a {self.design} design"

class IronWeapon(Weapon):

    def __init__(self) -> None:
        super().__init__()
        self.damage = 10
        self.duration = 20

    def get_duration(self) -> int:
        return self.duration

    def update_duration(self, value: int) -> int:
        self.duration = self.duration - value
    
    def attack(self):
        return self.damage

    
class SteelWeapon(Weapon):

    def __init__(self) -> None:
        super().__init__()
        self.damage = 15
        self.duration = 30

    def get_duration(self) -> int:
        return self.duration

    def update_duration(self, value: int) -> int:
        self.duration = self.duration - value
    
    def attack(self):
        return self.damage


class ArmorFactory(ABC):

    @abstractmethod
    def create_helmet(self) -> Helmet:
        """Create a Helmet"""
        pass

    @abstractmethod
    def create_clothe(self) -> Clothe:
        """Create a Clothe"""
        pass

    @abstractmethod
    def create_weapon(self) -> Weapon:
        """Create a weapon"""
        pass

class IronArmorFactory(ArmorFactory):

    def create_helmet(self) -> Helmet:
        return IronHelmet()

    def create_clothe(self) -> Clothe:
        return IronClothe()

    def create_weapon(self) -> Weapon:
        return IronWeapon()

class SteelArmorFactory(ArmorFactory):

    def create_helmet(self) -> Helmet:
        return SteelHelmet()

    def create_clothe(self) -> Clothe:
        return SteelClothe()

    def create_weapon(self) -> Weapon:
        return SteelWeapon()

class ArmorSet():

    def __init__(self, factory: ArmorFactory) -> None:
        self.factory = factory

    def create_set(self):
        self.helmet = self.factory.create_helmet()
        self.clothe = self.factory.create_clothe()
        self.weapon = self.factory.create_weapon()

    def get_duration(self):

        return self.helmet.get_duration() + self.clothe.get_duration() + self.weapon.get_duration()

    def get_protection(self):

        return self.helmet.get_protection() + self.clothe.get_protection()


if __name__ == "__main__":

    print("Character 1 >> Have an Iron Armor")
    iron_armor = ArmorSet(IronArmorFactory())
    iron_armor.create_set()
    print(f"Iron Armor Duration: {iron_armor.get_duration()}")
    print(f"Iron Armor Protection: {iron_armor.get_protection()}")
    print(f"Iron Weapon Damage: {iron_armor.weapon.attack()}")
    print(f"Iron Helmet Design: {iron_armor.helmet.get_ornament()}")
    print(f"Iron Clothe Design: {iron_armor.clothe.get_design()}")


    print("Caharacter 2 >> Have a Steel Armor")
    steel_armor = ArmorSet(SteelArmorFactory())
    steel_armor.create_set()
    print(f"Steel Armor Duration: {steel_armor.get_duration()}")
    print(f"Steel Armor Protection: {steel_armor.get_protection()}")
    print(f"Steel Weapon Damage: {steel_armor.weapon.attack()}")
    print(f"Steel Helmet Design: {steel_armor.helmet.get_ornament()}")
    print(f"Steel Clothe Design: {steel_armor.clothe.get_design()}")
