#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def garden_operations(pattern) -> None:
    if (pattern == "PlantError"):
        raise PlantError("The tomato plant is wilting!")
    elif (pattern == "Water"):
        raise WaterError("Not enough water in the tank!")
    elif (pattern == "all"):
        return open("42")
    print("Operation completed successfully")
    return (pattern)


def test_custom() -> None:
    for pattern in ("PlantError", "Water", "all"):

        if (pattern == "all"):
            print("Testing catching all garden errors...")
        else:
            print(f"Testing {pattern}Error...")

        try:
            garden_operations(pattern)
        except:
            pass



if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

