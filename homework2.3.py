def calculate_vat(amount=100):
    vat_amount = amount * 0.2
    # by default function return None
    return vat_amount

total = calculate_vat(100)
print(total)