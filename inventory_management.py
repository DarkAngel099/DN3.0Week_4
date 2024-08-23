
product_names = []

def add_product(product_name):
    """Add a product to the list."""
    product_names.append(product_name)
    print(f"Product '{product_name}' added.")

def remove_product(product_name):
    """Remove a product from the list."""
    if product_name in product_names:
        product_names.remove(product_name)
        print(f"Product '{product_name}' removed.")
    else:
        print(f"Product '{product_name}' not found.")

def update_product(old_name, new_name):
    """Update a product name in the list."""
    if old_name in product_names:
        index = product_names.index(old_name)
        product_names[index] = new_name
        print(f"Product '{old_name}' updated to '{new_name}'.")
    else:
        print(f"Product '{old_name}' not found.")

product_details = {}

def add_product_details(name, quantity, price):
    """Add product details to the dictionary."""
    product_details[name] = {'quantity': quantity, 'price': price}
    print(f"Product details for '{name}' added.")

def update_product_details(name, quantity=None, price=None):
    """Update product details in the dictionary."""
    if name in product_details:
        if quantity is not None:
            product_details[name]['quantity'] = quantity
        if price is not None:
            product_details[name]['price'] = price
        print(f"Product details for '{name}' updated.")
    else:
        print(f"Product '{name}' not found.")

def delete_product_details(name):
    """Delete product details from the dictionary."""
    if name in product_details:
        del product_details[name]
        print(f"Product details for '{name}' deleted.")
    else:
        print(f"Product '{name}' not found.")


def create_product_catalog():
    """Create a catalog of products using tuples."""
    product_catalog = [
        ('Widget', 50, 19.99),
        ('Gadget', 100, 29.99),
        ('Doodad', 75, 14.99),
    ]
    return product_catalog

def display_catalog(product_catalog):
    """Display the product catalog."""
    print("\nProduct Catalog:")
    for product in product_catalog:
        print(f"Name: {product[0]}, Quantity: {product[1]}, Price: ${product[2]:.2f}")


product_categories = set()

def add_category(category):
    """Add a category to the set."""
    product_categories.add(category)
    print(f"Category '{category}' added.")

def remove_category(category):
    """Remove a category from the set."""
    if category in product_categories:
        product_categories.remove(category)
        print(f"Category '{category}' removed.")
    else:
        print(f"Category '{category}' not found.")


def generate_price_report():
    """Generate a report of products sorted by price."""
    sorted_products = sorted(product_details.items(), key=lambda item: item[1]['price'])
    print("\nPrice Report:")
    for name, details in sorted_products:
        print(f"Name: {name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

def find_products_in_price_range(min_price, max_price):
    """Find products that fall within a certain price range."""
    products_in_range = {name for name, details in product_details.items() if min_price <= details['price'] <= max_price}
    print(f"\nProducts in price range ${min_price:.2f} - ${max_price:.2f}: {products_in_range}")


if __name__ == "__main__":
    add_product("Widget")
    add_product("Gadget")
    add_product("Doodad")

    
    update_product("Widget", "Super Widget")

    
    add_product_details("Super Widget", 50, 19.99)
    add_product_details("Gadget", 100, 29.99)
    add_product_details("Doodad", 75, 14.99)

    
    update_product_details("Gadget", price=24.99)

    
    generate_price_report()

    
    find_products_in_price_range(15, 25)

    
    add_category("Electronics")
    add_category("Household")
    remove_category("Household")

    
    catalog = create_product_catalog()
    display_catalog(catalog)
