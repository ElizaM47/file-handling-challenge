def calculate_discount(price, discount_percent):
    """Return final price after discount IF discount >= 20%, else original price."""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price


try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    if price < 0 or discount_percent < 0:
        print("Price and discount must be non-negative.")
    else:
        final_price = calculate_discount(price, discount_percent)
        if discount_percent >= 20:
            print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
        else:
            print(f"No discount applied. Original price: {final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
