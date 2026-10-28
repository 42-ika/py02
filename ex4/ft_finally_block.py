#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if ('A' <= plant_name[0] <= 'Z'):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(s1: str, s2: str, s3: str) -> None:
    print("Opening watering system")
    try:
        for plants in (s1, s2, s3):
            water_plant(plants)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system("Tomato", "Lettuce", "Carrots")
    print("\nTesting invalid plants...")
    test_watering_system("Tomato", "lettuce", "carrots")
    print("\nCleanup always happens, even with errors!")
