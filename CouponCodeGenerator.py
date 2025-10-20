import random
import string
import csv
from datetime import datetime

def generate_coupon(length=10, prefix="", suffix="", chars=string.ascii_uppercase + string.digits):
    """Generate a single coupon code."""
    middle = ''.join(random.choices(chars, k=length))
    return f"{prefix}{middle}{suffix}"

def generate_coupons(n=10, length=10, prefix="", suffix=""):
    """Generate a list of unique coupon codes."""
    coupons = set()
    while len(coupons) < n:
        code = generate_coupon(length, prefix, suffix)
        coupons.add(code)
    return list(coupons)

def save_to_csv(coupons, filename="coupons.csv"):
    """Save the generated coupons to a CSV file with timestamps."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Coupon Code", "Created At"])
        for code in coupons:
            writer.writerow([code, datetime.now().isoformat()])

# Example usage:
if __name__ == "__main__":
    total_coupons = 20
    code_length = 8
    prefix = "SALE-"
    suffix = "-2025"

    coupons = generate_coupons(n=total_coupons, length=code_length, prefix=prefix, suffix=suffix)
    save_to_csv(coupons)

    print(f"{total_coupons} coupons generated and saved to 'coupons.csv'")
