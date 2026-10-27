#!/usr/bin/env python3

def garden_operations(operation_number) -> None:
    if (operation_number == 0):
        return int("abc")
    elif (operation_number == 1):
        return (2 / 0)
    elif (operation_number == 2):
        return open("42")
    elif (operation_number == 3):
        return ("abc" + 123)
    print("Operation completed successfully")
    return (operation_number)


def test_error_types() -> None:
    for num in (0, 1, 2, 3, 4):
        print(f"Testing operation {num}...")
        try:
            garden_operations(num)
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError
        ) as e:
            print(f"Caught TypeError: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
