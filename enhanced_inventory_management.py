# enhanced_inventory_management.py

import json
import threading
import time
import os

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
            else:
                print(f"Not enough {item_name} in stock to remove {quantity}.")
        else:
            print(f"Item {item_name} not found in inventory.")

    def check_stock(self, item_name):
        return self.items.get(item_name, 0)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.items, file)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename):
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    self.items = json.load(file)
                print(f"Inventory loaded from {filename}.")
            else:
                print(f"File {filename} does not exist.")
        except IOError as e:
            print(f"Error loading inventory from file: {e}")

    def restock_alerts(self, threshold=10):
        while True:
            for item_name, quantity in self.items.items():
                if quantity < threshold:
                    print(f"Restock Alert: {item_name} is low in stock ({quantity} left).")
            time.sleep(5)  # Check every 5 seconds

# Create an inventory instance
inventory = Inventory()

# Perform some operations
inventory.add_item("Widget", 20)
inventory.add_item("Gadget", 5)
inventory.remove_item("Widget", 5)

# Save the inventory state to a file
inventory.save_to_file("inventory.json")

# Load the inventory state from the file and print it
inventory.load_from_file("inventory.json")
print("Current Inventory:", inventory.items)

# Start a thread to check for restocking alerts
alert_thread = threading.Thread(target=inventory.restock_alerts)
alert_thread.daemon = True  # Daemon thread will close when the main program exits
alert_thread.start()

# Run the program for some time to see restock alerts
time.sleep(20)
