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


def garden_operations(pattern: str) -> None:
    if (pattern == "PlantError"):
        raise PlantError("The tomato plant is wilting!")
    elif (pattern == "Water"):
        raise WaterError("Not enough water in the tank!")
    return


def test_custom() -> None:
    for pattern in ("PlantError", "Water", "all"):

        if (pattern == "all"):
            print("Testing catching all garden errors...")
            for error in ("PlantError", "Water"):
                try:
                    garden_operations(error)
                except GardenError as e:
                    print(f"Caught WaterError: {e}")

        else:
            print(f"Testing {pattern}Error...")
        try:
            garden_operations(pattern)
        except (
            PlantError,
            WaterError,
        ) as e:
            print(f"Caught PlantError: {e}")
        print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_custom()
