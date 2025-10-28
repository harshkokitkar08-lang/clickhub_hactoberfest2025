#write your code here
def unlock_ship(a, b, c):
    # Convert bits to decimal
    decimal_value = a * (2**2) + b * (2**1) + c * (2**0)

    # Check if power of 2
    if decimal_value > 0 and (decimal_value & (decimal_value - 1)) == 0:
        return "Yes! Ship Unlocked."
    else:
        return "No! Better luck next time."


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(unlock_ship(a, b, c))
