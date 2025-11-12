import streamlit as st

# ===== Data =====
book_ids = [1, 2, 3, 4, 5]
titles = ["Python Basics", "AI & ML", "Data Science", "Web Development", "Cyber Security"]
stocks = [10, 5, 8, 6, 4]
prices = [250, 400, 300, 350, 500]

# ===== Admin Credentials =====
admin_username = "admin"
admin_password = "1234"

# ===== Streamlit App =====
st.title("📚 Python Book Store")
st.write("Welcome to the Python Book Store! Choose an option from below:")

menu = st.sidebar.radio("Navigation", ["Show All Books", "Buy a Book", "Add New Book (Admin Only)", "Exit"])

# --- Option 1: Show All Books ---
if menu == "Show All Books":
    st.subheader("📖 Available Books")
    st.table({
        "ID": book_ids,
        "Title": titles,
        "Stock": stocks,
        "Price (Rs.)": prices
    })

# --- Option 2: Buy a Book ---
elif menu == "Buy a Book":
    st.subheader("🛒 Buy a Book")
    for i in range(len(book_ids)):
        st.write(f"**{book_ids[i]}. {titles[i]}** — Stock: {stocks[i]} | Price: Rs.{prices[i]}")

    book_id = st.number_input("Enter Book ID to buy", min_value=1, max_value=max(book_ids), step=1)
    if st.button("Proceed to Buy"):
        if book_id in book_ids:
            index = book_ids.index(book_id)
            if stocks[index] > 0:
                name = st.text_input("Enter your name")
                confirm = st.radio(f"Do you want to buy '{titles[index]}' for Rs.{prices[index]}?", ["No", "Yes"])
                if confirm == "Yes" and name:
                    stocks[index] -= 1
                    st.success(f"✅ Purchase Successful!\n\n**Customer:** {name}\n**Book:** {titles[index]}\n**Amount:** Rs.{prices[index]}")
                elif not name:
                    st.warning("Please enter your name to proceed.")
            else:
                st.error("Sorry, this book is out of stock.")
        else:
            st.error("Invalid Book ID.")

# --- Option 3: Add New Book (Admin Only) ---
elif menu == "Add New Book (Admin Only)":
    st.subheader("🔐 Admin Panel - Add New Book")
    username = st.text_input("Admin Username")
    password = st.text_input("Admin Password", type="password")

    if username == admin_username and password == admin_password:
        new_title = st.text_input("Enter new book title")
        new_stock = st.number_input("Enter stock quantity", min_value=1, step=1)
        new_price = st.number_input("Enter price (Rs.)", min_value=1, step=50)
        if st.button("Add Book"):
            new_id = max(book_ids) + 1
            book_ids.append(new_id)
            titles.append(new_title)
            stocks.append(new_stock)
            prices.append(new_price)
            st.success(f"✅ Book '{new_title}' added successfully!")
    else:
        if username or password:
            st.error("Invalid admin credentials.")

# --- Option 4: Exit ---
elif menu == "Exit":
    st.subheader("👋 Thank you for visiting the Python Book Store!")
    st.write("Come back soon!")

