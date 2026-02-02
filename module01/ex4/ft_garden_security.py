class SecurePlant:

    """
    Represents a secure plant that protects data integrity.
    This class implements encapsulation and validation to prevent
    corruption of plant data through invalid values.
    
    Attributes
    ----------
        name : The name of the plant.
        _height : The height of the plant in centimeters (private attribute).
        _age : The age of the plant in days (private attribute).
    
    Methods
    -------
        set_height(height: int)
            Sets the plant height with validation against negative values.
        set_age(age: int)
            Sets the plant age with validation against negative values.
        get_height() -> int
            Returns the current height of the plant.
        get_age() -> int
            Returns the current age of the plant.
        get_info() -> str
            Returns formatted information about the plant.
    """

    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self._height = height
        self._age = age
    
    
    def set_height(self, set_height: int):
        if set_height < 0:
            print(f"\nInvalid operation attempted: height {set_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = set_height
            print(f"Height updated: {set_height}cm [OK]")

    def set_age(self, set_age: int):
        if set_age < 0:
            print(f"\nInvalid operation attempted: age {set_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = set_age
            print(f"Age updated: {set_age} days [OK]")

    def get_height(self)-> int:
        return self._height

    def get_age(self)-> int:
        return self._age

    def get_info(self)->str:
        return f"{self.name} ({self._height}cm, {self._age} days)"


def ft_garden_security():

    """    
    Creates a SecurePlant instance and tests its validation mechanisms
    by attempting to set valid and invalid values. Shows how the system
    rejects negative heights and ages to maintain data integrity.
    
    Returns
    -------
    None
        This function does not return any value.
        It only prints information to the standard output.
    """

    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {rose.name}")
          
    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)

    print(f"\nCurrent plant: {rose.get_info()}")

if __name__ == "__main__":
    ft_garden_security()
