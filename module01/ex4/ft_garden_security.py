class SecurePlant:

    """
    Represents a secure plant that protects data integrity.
    This class implements encapsulation and validation to prevent
    corruption of plant data through invalid values.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a SecurePlant instance with a name, height, and age.
        """
        self.name = name.capitalize()
        self._height = height
        self._age = age

    def set_height(self, set_height: int):
        """
        Set the height of the plant with validation.
        """
        if set_height < 0:
            print("\nInvalid operation attempted: height"
                  + f"{set_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = set_height
            print(f"Height updated: {set_height}cm [OK]")

    def set_age(self, set_age: int):
        """
        Set the age of the plant with validation.
        """
        if set_age < 0:
            print("\nInvalid operation attempted:"
                  + f"age {set_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = set_age
            print(f"Age updated: {set_age} days [OK]")

    def get_height(self) -> int:
        """
        Get the current height of the plant.

        Returns
        -------
        int
            The height of the plant in centimeters.
        """
        return self._height

    def get_age(self) -> int:
        """
        Get the current age of the plant.

        Returns
        -------
        int
            The age of the plant in days.
        """
        return self._age

    def get_info(self) -> str:
        """
        Get formatted information about the plant.

        Returns
        -------
        str
            A string containing the plant's name, height, and age.
        """
        return f"{self.name} ({self._height}cm, {self._age} days)"


def ft_garden_security():

    """
    Creates a SecurePlant instance and tests its validation mechanisms
    by attempting to set valid and invalid values. Shows how the system
    rejects negative heights and ages to maintain data integrity.
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
