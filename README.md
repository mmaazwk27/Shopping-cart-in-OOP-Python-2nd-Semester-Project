# 🛒 Smart Home Solutions - Console-based shopping cart application using OOP in Python (2nd Semester Project)

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Style](https://img.shields.io/badge/style-Object--Oriented-green)

![Academic Project](https://img.shields.io/badge/License-Academic-blueviolet?style=for-the-badge&logo=bookstack&logoColor=white)&nbsp;
![Made in Pakistan](https://img.shields.io/badge/Made%20In-Pakistan-006600?style=for-the-badge&logo=pakistan&logoColor=white)

A Python-based console application that simulates an e-commerce platform for smart home devices. This system supports user and admin functionalities including inventory management, account handling, cart operations, and secure login—all backed by file-based storage.

## 📦 Features

### 👤 User Panel
- Create a new user account
- Login with credentials
- Browse available inventory
- Add or remove items from the cart
- View cart and total cost
- Apply coupon codes for discounts
- Checkout and save purchase history

### 🔐 Admin Panel
- Secure access with unique access code and credentials
- View all inventory items
- Add new products to inventory
- Remove or update existing products
- View all registered user accounts
- Delete specific user accounts and their saved data

## 📁 File-Based Storage

- **accounts.txt**: Stores all user credentials.
- **<username>.txt**: Stores individual user purchase history and profile data.
- **inventory.txt**: Contains details about products in the store.

## 🏗️ Project Structure

```
📁 Shopping-cart-in-OOP-Python-2nd-semester-project/
│
├── inventory.txt        # Contains product details for inventory  
├── cart.py              # Cart operations class
├── shopping cart OOP.py # Main app 
├── accounts.txt         # Stores usernames and passwords
├── *.txt                # One file per user with shopping data
├── README.md            # Project documentation
```

## 🚀 Getting Started

 **Run the Application**  
   ```bash
   shopping cart OOP.py
   ```

## 🛂 Admin Credentials

```
Access Code:     KHI-0021
Username:        admin1
Password:        AdminUniquePass
```

## 💸 COUPONS

```

code: NEW40   → 40% off (for new users only)
code: OFF25   → 25% off
code: OFF30   → 30% off
```

---

## 🌟 EXTRA FEATURES IN THE CODE

✅ DISCOUNT COUPONS  
✅ STOCK MANAGEMENT  
✅ ADMIN ACCOUNT WITH ACCESS CODE  
✅ PAYMENT PROCESS METHOD  

## 📌 Example Products

You can prepopulate `inventory.txt` with sample entries like:
```
('1','SmartLight', 1500, 10)
('2','SmartThermostat', 4500, 5)
('3','WiFiPlug', 1000, 15)
```

## 📚 Future Enhancements

- Migrate to SQLite or PostgreSQL database
- Add GUI using Tkinter or PyQt
- Password encryption using `hashlib`
- Export shopping history as PDF or CSV
- Add delivery & billing modules

---

# 👨‍💻 Author 

**Muhammad Maaz Wali Khan**
-- 🔗 [GitHub: @mmaazwk27](https://github.com/mmaazwk27)
- ### Collaborator
    - **Mehak Duseja**
-- 🔗 [GitHub: @MehakDuseja](https://github.com/MehakDuseja)
   - **Eman Zaheer**
-- 🔗 [GitHub: @emanzaheer](https://github.com/emanzaheer)

