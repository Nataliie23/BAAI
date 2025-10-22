#This is a program for a retail store
#We are making a Product Discount Calculator


#Data provided:
products = [{"name": "Laptop", "price" : 1200, "category": "Electronics"},
            {"name": "Shirt", "price": 45, "category": "Clothing"},
            {"name": "Phone", "price": 800, "category": "Electronics"},
            {"name": "Shoes", "price": 120, "category": "Clothing"},
            {"name": "Tablet", "price": 350, "category": "Electronics"},
            {"name": "Jacket", "price": 95, "category": "Clothing"},
            {"name": "Book", "price": 25, "category": "Books"},
            {"name": "Headphones", "price": 150, "category": "Electronics"}]

print("=== PRODUCT DISCOUNT CALCULATOR ===")
print("   ")
total_original = 0
total_discount = 0
total_final = 0 

for product in products:
    price = product["price"] 
    category = product["category"]

    if category == "Electronics":
        if price >= 1000:
            discounts = "20%"
            discount = price * 0.20
        elif price >= 500:
            discounts = "15%"
            discount = price * 0.15
        else:
            discounts = "10%"
            discount = price * 0.10

    elif category == "Clothing":
        if price >= 100:
            discounts = "25%"
            discount = price * 0.25
        else:
            discounts = "15%"
            discount = price * 0.15

    elif category == "Books":
        discounts = "10%"
        discount = price * 0.10 

    else:
        discount = 0.0  
        discounts = "0%"

    final_price = price - discount 
    
    total_original += price
    total_discount += discount
    total_final += final_price
    
    print(f"Product: {product['name']}")
    print(f"Category: {product['category']}" )
    print(f"Original Price: ${product['price']}")
    print(f"Discount: {discounts}")
    print(f"Final Price: {final_price}")
    print(f"        ")
    
print("=== SUMMARY ===")

total_products = len(products)
print (f"Total products: {total_products}")


print(f"Total Original Price: ${total_original}")
print(f"Total Discount: ${total_discount}")
print(f"Final price: {total_final}")
