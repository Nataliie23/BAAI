#This is a program for a retail store
#We are making a Product Discount Calculator

print("=== PRODUCT DISCOUNT CALCULATOR ===")
print("   ")
#Data provided:
products = [{"name": "Laptop", "price" : 1200, "category": "Electronics"},
            {"name": "Shirt", "price": 45, "category": "Clothing"},
            {"name": "Phone", "price": 800, "category": "Electronics"},
            {"name": "Shoes", "price": 120, "category": "Clothing"},
            {"name": "Tablet", "price": 350, "category": "Electronics"},
            {"name": "Jacket", "price": 95, "category": "Clothing"},
            {"name": "Book", "price": 25, "category": "Books"},
            {"name": "Headphones", "price": 150, "category": "Electronics"}]


total_original = 0
total_discount = 0
total_final = 0 

for product in products:
    price = product["price"] 

#Discounts percentage
    if price >= 1000:
        discounts = "20%"
    elif price >= 500:
        discounts = "15%"
    else:
        discounts = "10%"


#Discounts
    if price >= 1000:
        discount = price * 0.2
    elif price >= 500:
        discount = price * 0.15
    else:
        discount = price * 0.1

    final_price = price - discount #ChatGPT helped me realized I am missing this last part of the code, 
                                #but the rest  of "discount" I did by myself.
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
print(f"Total Dicount: ${total_discount}")
print(f"Final price: {total_final}")
