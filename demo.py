def calculate_stats(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers), sum(numbers) / len(numbers), min(numbers), max(numbers)


def print_report(numbers):
    total, average, min_val, max_val = calculate_stats(numbers)
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")


if __name__ == "__main__":
    data = [10, 3, 7, 25, 1, 18, 4]
    print_report(data)
