"""
Inventory Management System
This module provides functions to manage stock data with proper security,
style, and maintainability. Static analysis tools have been used to ensure
clean, safe, and PEP 8-compliant code.
"""

import json
from datetime import datetime

# Load stock data at startup (no need for global statements)
try:
    with open("inventory.json", "r", encoding="utf-8") as file_obj:
        stock_data = json.loads(file_obj.read())
except FileNotFoundError:
    stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add a specified quantity of an item to the stock.

    Args:
        item (str): The name of the item.
        qty (int): Quantity to add.
        logs (list, optional): List to store log messages.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid item or quantity")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a specified quantity of an item from the stock.

    Args:
        item (str): The name of the item.
        qty (int): Quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found.")


def get_qty(item):
    """
    Return the quantity of the specified item in stock.

    Args:
        item (str): Item name.

    Returns:
        int: Quantity available.
    """
    return stock_data.get(item, 0)


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file (str): Path to the JSON file.
    """
    with open(file, "w", encoding="utf-8") as file_handle:
        file_handle.write(json.dumps(stock_data))


def print_data():
    """
    Print the current inventory data to the console.
    """
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Check and return a list of items with stock quantity below the threshold.

    Args:
        threshold (int): Minimum stock level.

    Returns:
        list: Items below threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution function."""
    add_item("apple", 10)
    add_item("banana", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    print_data()


if __name__ == "__main__":
    main()
