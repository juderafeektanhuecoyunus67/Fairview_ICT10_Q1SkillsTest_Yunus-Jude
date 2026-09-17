"""
Main calculation logic for Coffee Shop Receipt Generator using PyScript.
Calculates sumtotal, 12% VAT tax, and grand total.
PEP 8 Compliant.
"""

from pyscript import document, display


def generate_order(e):
    """Calculates order costs and updates the DOM receipt view."""
    # the list of **tuples** items linking checkbox element IDs into prices..
    items = [
        ("item1", 150.00),
        ("item2", 160.00),
        ("item3", 180.00),
        ("item4", 168.00),
        ("item5", 170.00)
    ]

    sumtotal = 0.00

    # Loop through each item to calculate sum/total for selected checkboxes
    for item_id, price in items:
        checkbox = document.getElementById(item_id)
        if checkbox and checkbox.checked:
            sumtotal += price

    # Calculating Tax & Sum/Total
    tax = sumtotal * 0.12
    total = sumtotal + tax

    # Building exact matching HTML receipt layout **string**
    receipt_html = f"<p>Sumtotal: ₱{sumtotal:.2f}</p>"
    receipt_html += f"<p>Tax: ₱{tax:.2f}</p>"
    receipt_html += f"<p><u>Sum/Total:</u> ₱{total:.2f}</p>"

    # Making receipt string directly into output div target
    document.getElementById("output1").innerHTML = receipt_html