#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_nbr: int = int(temp_str)
    if (temp_nbr > 40):
        raise ValueError(
            f"{temp_nbr}°C is too hot for plants (max 40°C)"
        )
    if (temp_nbr < 0):
        raise ValueError(
            f"{temp_nbr}°C is too cold for plants (min 0°C)"
        )
    return temp_nbr


def test_temperature() -> None:
    for temp_str in ("25", "abc", "100", "-50"):
        print()
        print(f"Input data is '{temp_str}'")
        try:
            temperature: int = input_temperature(temp_str)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(
                f"Caught input_temperature error: {error}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
