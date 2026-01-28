class SecurePlant:

    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self._height = height
        self._age = age
    
    
    def set_height(self, set_height: int):
        if set_height < 0:
            print(f"Invalid operation attempted: height {set_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = set_height
            print(f"Height updated: {set_height}cm [OK]")

    def set_age(self, set_age: int):
        if set_age < 0:
            print(f"Invalid operation attempted: height {set_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = set_age
            print(f"Age updated: {set_age} days [OK]")

    def get_height(self)-> int:
        return self._height

    def get_age(self)-> int:
        return self._age

    def get_info(self)->str:
        return f"{self.name}: ({self._height}cm, {self._age} days)"


def ft_garden_security():

    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {rose.name}")
          
    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-7)

    print(f"\nCurrent plant: {rose.get_info()}")

if __name__ == "__main__":
    ft_garden_security()
