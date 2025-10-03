from pyscript import document

menu_prices = {
    "Sushi": 50,
    "Salmon": 150,
    "Curry": 30,
    "Drink": 20
}

def compute_order(event):
    customer_name = document.getElementById("cust_name").value or "Unknown"
    customer_address = document.getElementById("cust_address").value or "N/A"
    customer_contact = document.getElementById("cust_contact").value or "N/A"

    selected_items = []
    total = 0

    if document.getElementById("item_sushi").checked:
        selected_items.append("Sushi")
        total += menu_prices["Sushi"]
    if document.getElementById("item_salmon").checked:
        selected_items.append("Salmon")
        total += menu_prices["Salmon"]
    if document.getElementById("item_curry").checked:
        selected_items.append("Curry")
        total += menu_prices["Curry"]
    if document.getElementById("item_drink").checked:
        selected_items.append("Drink")
        total += menu_prices["Drink"]

    if selected_items:
        items_str = "\n".join(f"{item} - ₱{menu_prices[item]}" for item in selected_items)
    else:
        items_str = "No items selected."

    summary_text = (
        f"Order Summary:\n"
        f"Customer Name: {customer_name}\n"
        f"Address: {customer_address}\n"
        f"Contact: {customer_contact}\n\n"
        f"Ordered Items:\n{items_str}\n\n"
        f"Total Amount: ₱{total}"
    )

    document.getElementById("summary").innerHTML = f"<pre>{summary_text}</pre>"