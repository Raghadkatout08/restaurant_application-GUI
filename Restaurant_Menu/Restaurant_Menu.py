import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

prices = {
    "Pizza": {"Small": 5, "Medium": 7 , "Large":10},
    "Burger": {"Classic": 5, "Big": 7},
    "Soft Drink": {"": 2},
    "Extra Cheese": {"": 1},
    "Extra Ketchup": {"": 1}
}

def submit_order():
    # Retrieve user inputs
    pizza_quantity = pizza_quantity_var.get() 
    pizza_size = pizza_size_var.get()
    burger_quantity = burger_quantity_var.get() 
    burger_size = burger_size_var.get()
    soft_drinks_quantity = soft_drinks_quantity_var.get()
    extra_cheese_quantity = extra_cheese_var.get()
    extra_ketchup_quantity = extra_ketchup_var.get()
    order_type = order_type_var.get()

    total_price = calculate_total_price(pizza_quantity, pizza_size, burger_quantity, burger_size, soft_drinks_quantity, extra_cheese_quantity, extra_ketchup_quantity)
    
    show_order_summary(order_type, pizza_quantity, pizza_size, burger_quantity, burger_size, soft_drinks_quantity, extra_cheese_quantity, extra_ketchup_quantity, total_price)
    

def calculate_total_price(pizza_quantity, pizza_size, burger_quantity, burger_size, soft_drinks_quantity, extra_cheese_quantity, extra_ketchup_quantity):
    total_price = 0 

    # Calculate price for Pizza
    pizza_price = prices["Pizza"][pizza_size]
    total_price += pizza_quantity * pizza_price

    # Calculate price for Burger
    burger_price = prices["Burger"][burger_size]
    total_price += burger_quantity * burger_price

    # Calculate price for Soft Drink
    soft_drinks_price = prices["Soft Drink"][""]
    total_price += soft_drinks_quantity * soft_drinks_price

    # Calculate price for Extra Cheese
    extra_cheese_price = prices["Extra Cheese"][""]
    total_price += extra_cheese_quantity * extra_cheese_price

    # Calculate price for Extra Ketchup
    extra_ketchup_price = prices["Extra Ketchup"][""]
    total_price += extra_ketchup_quantity * extra_ketchup_price

    return total_price
 

def show_order_summary(order_type, pizza_quantity, pizza_size, burger_quantity, burger_size, soft_drinks_quantity, extra_cheese_quantity, extra_ketchup_quantity, total_price):
    summary_window = tk.Toplevel(root)
    summary_window.title("Order Summary")

    summary_text = f"Order Type: {order_type}\n\n" \
                   f"Pizza - Quantity: {pizza_quantity}, Size: {pizza_size}\n\n" \
                   f"Burger - Quantity: {burger_quantity}, Size: {burger_size}\n\n" \
                   f"Soft Drinks - Quantity: {soft_drinks_quantity}\n\n" \
                   f"Extra Cheese - Quantity: {extra_cheese_quantity}\n\n" \
                   f"Extra Ketchup - Quantity: {extra_ketchup_quantity}\n\n" \
                   f"Total Price: ${total_price:.2f}"
    
    messagebox.showinfo("Order Summary", summary_text)
    print(summary_text)
    confirm = messagebox.askquestion("Confirm Order", "Do you want to confirm this order?")
    if confirm == 'yes':
        messagebox.showinfo("Order Confirmed", "Your order has been confirmed!")
    else:
        messagebox.showinfo("Order Canceled", "Your order has been canceled.")

    
# Create a TKinter application window
root = tk.Tk()

# Set widnow title and size
root.title("Restaurant Menu")
root.geometry("800x800")

# set custom styles
root.configure(bg="#f7f5fa")
label_font= ("Alkes", 12)
Entry_font= ("Arial", 12)
button_font= ("Arial", 12, "bold")

# Create labels
tk.Label(root, text="Restaurant Menu application", font=("Arial", 20), pady=10, bg="#d6ebe1").grid(row=0, column=0, columnspan=2)


price_label = tk.Label(root, text="Menu Prices", font=("Arial", 20), pady=10, bg="#d6ebe1")
price_label.grid(row=13, column=0, columnspan=2)

# Display the list of prices
row_counter = 14
for item, sizes in prices.items():
    tk.Label(root, text=item, font=label_font, bg="#e1d6eb").grid(row=row_counter, column=0, padx=10, pady=5, sticky="e")
    size_prices = ", ".join([f"{size}: ${price}" for size, price in sizes.items()])
    label = tk.Label(root, text=size_prices, font=label_font, bg="#f7f5fa")
    label.grid(row=row_counter, column=1, padx=10, pady=5, sticky="w")
    label.configure(foreground="gray")
    row_counter += 1
    



# Create Entry Fields for user input

# Pizza Section
tk.Label(root, text="Pizza Quantity: ", font=label_font, bg="#e1d6eb").grid(row=1, column=0, padx=10, pady=5, sticky="e")
pizza_quantity_var = tk.IntVar()
pizza_quantity_scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, variable=pizza_quantity_var)
pizza_quantity_scale.grid(row=1, column=1, padx=10, pady=5, sticky="w")
pizza_quantity_scale.set(0) 


tk.Label(root, text="Pizza Size: ", font=label_font, bg="#e1d6eb").grid(row=2, column=0, padx=10, pady=5, sticky="e")
pizza_size_var = tk.StringVar() 
pizza_size_dropdown  = ttk.Combobox(root, textvariable=pizza_size_var, values=["Small", "Medium", "Large"], font=Entry_font)
pizza_size_dropdown .grid(row=2, column=1, padx=10, pady=5, sticky="w")
pizza_size_dropdown .current(0)

# Burger Section 
tk.Label(root, text="Burger Quantity: ", font=label_font, bg="#e1d6eb").grid(row=3, column=0, padx=10, pady=5, sticky="e")
burger_quantity_var = tk.IntVar()
burger_quantity_scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, variable=burger_quantity_var)
burger_quantity_scale.grid(row=3, column=1, padx=10, pady=5, sticky="w")
burger_quantity_scale.set(0) 

tk.Label(root, text="Burger Size: ", font=label_font, bg="#e1d6eb").grid(row=4, column=0, padx=10, pady=5, sticky="e")
burger_size_var = tk.StringVar() 
burger_size_dropdown  = ttk.Combobox(root, textvariable=burger_size_var, values=["Classic", "Big"], font=Entry_font)
burger_size_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="w")
burger_size_dropdown .current(0)

# Soft Drinks Section 
tk.Label(root, text="Soft Drinks Quantity: ", font=label_font, bg="#e1d6eb").grid(row=5, column=0, padx=10, pady=5, sticky="e")
soft_drinks_quantity_var = tk.IntVar()
soft_drinks_quantity_scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, variable=soft_drinks_quantity_var)
soft_drinks_quantity_scale.grid(row=5, column=1, padx=10, pady=5, sticky="w")
soft_drinks_quantity_scale.set(0)

# Extra Cheese Section
extra_cheese_var = tk.IntVar()
extra_cheese_var.set(0) 
tk.Label(root, text="Extra Cheese:", font=label_font, bg="#e1d6eb").grid(row=6, column=0, padx=10, pady=5, sticky="e")
tk.Radiobutton(root, text="No", variable=extra_cheese_var, value=0, font=Entry_font, bg="#f7f5fa").grid(row=6, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Yes", variable=extra_cheese_var, value=1, font=Entry_font, bg="#f7f5fa").grid(row=6, column=2, padx=10, pady=5, sticky="w")

# Extra Ketchup Section
extra_ketchup_var = tk.IntVar()
extra_ketchup_var.set(0) 
tk.Label(root, text="Extra Ketchup:", font=label_font, bg="#e1d6eb").grid(row=7, column=0, padx=10, pady=5, sticky="e")
tk.Radiobutton(root, text="No", variable=extra_ketchup_var, value=0, font=Entry_font, bg="#f7f5fa").grid(row=7, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Yes", variable=extra_ketchup_var, value=1, font=Entry_font, bg="#f7f5fa").grid(row=7, column=2, padx=10, pady=5, sticky="w")

# Order Type Section
tk.Label(root, text="Would you prefer Takeaway or Dine-in for your order?", font=label_font, bg="#e1d6eb").grid(row=9, column=0, padx=10, pady=5, sticky="e")
order_type_var = tk.StringVar()
order_type_var.set("Takeaway")
tk.Radiobutton(root, text="Takeawar", variable=order_type_var, value="Takeaway", font= Entry_font, bg="#f7f5fa").grid(row=9, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Dine in", variable=order_type_var, value="Dine in", font=Entry_font, bg="#f7f5fa").grid(row=10, column=1, padx=10, pady=5, sticky="w")


# Order Summary Button 
ttk.Button(root, text="Order Summary", command=submit_order, style="Bold.TButton").grid(row=12, columnspan=2, pady=10)




style = ttk.Style()
style.configure("Bold.TButton", font=button_font)


root.mainloop()