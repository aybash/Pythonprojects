def calculate_discount(price, discount_percent):
 
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    

    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the result
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"After a discount of {discount_percentage}%, the final price is: ${final_price:.2f}")
except ValueError:
    print("Error: Please enter valid numbers for the price and discount percentage.")
