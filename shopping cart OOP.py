

# ADMIN PANEL ACCESS CODE: KHI-0021
# ADMIN USERNAME:admin1
# ADMIN PASSWORD:AdminUniquePass

from abc import ABC, abstractmethod  # Abstract class for methods login and create account
import os


class Accounts(ABC):
    
    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def login(self):
        pass
    


class Account_manager(Accounts):  # INHERITANCE

    def read_accounts(self):
        '''  The main purpose of read_accounts is to read user account information stored in a file (accounts.txt)
         and convert it into a Python dictionary format ,also Exception handling is done here if file not found empty
          dictionary is returned  '''
        try:
            with open('accounts.txt', 'r+') as f_main: # AFTER CHECKING, OPENS IT IN READ MODE
                    users_read = f_main.read()  # Save user info into users_read
                    return eval('{' + users_read + '}')  # Converting user_read into dictionary
        except FileNotFoundError:
            print('No Accounts File Found! \nA new file will be created')
            return {}



    def create_account(self):# method overridden from abstract class
        ''' This function takes input about the user info and have some basic chceks and store that user info into a
        dictionary called u_data also it creates a users file with its username and save u_data in users file also
        provide a coupon code for the first time only'''
        self.accounts=self.read_accounts()
        while True:
            while True:
                username = input('\nEnter Username:').strip()
                if len(username)==0: # CHECK IF USERNAME IS ENTERED
                    print('Username space cannot be empty\n')
                else:
                    username = username.lower()
                    break
            if username in self.accounts.keys(): # CHECK USERNAME IN [KEYS] OF self.accounts DICTIONARY
                print('Username already taken.Please use another username\n')
                break
            else:
                while True:
                    password = input('Enter Password:')
                    if len(password)==0:  # CHECK IF PASSWORD IS ENTERED
                        print("Password space cannot be empty\n")
                    else:
                        break
                while True:
                    fname = input('Enter your First name: ').strip()
                    if len(fname)==0: # CHECK IF FIRST NAME IS ENTERED
                        print('Enter a valid name\n')
                    else:
                        break
                while True:
                    lname = input('Enter your last name: ').strip()
                    if len(lname)==0: # CHECK IF BILLING ADDRESS IS ENTERED
                        print("Last name space cannot be left empty.\n")
                    else:
                        break
                while True:
                    _add = input('Enter your  billing address: ').strip()
                    if len(_add)==0: # CHECK IF BILLING ADDRESS IS ENTERED
                        print("Billing address is necessary for proceeding into the store.\n")
                    else:
                        break
                while True:
                    numb = input('Enter your Phone number: ').strip()
                    # CHECK IF INPUT DOES NOT ENTIRELY CONSIST OF DIGITS
                    if not numb.isdigit():
                        print('Please enter a number containing digits only.\n')
                    else:
                        # PROCESSING WHEN A VALID INPUT IS PROVIDED
                        break
                print('account created succefully')
                while True:
                    print('\nYou got a new user discount coupon!!\n Coupon code: NEW40    Discount:40%\n')
                    input('Press any key to continue: ').strip()
                    break
                u_data = {'u_name': username, 'Pass': password, 'f_name': fname, 'lname': lname, 'add': _add, 'phone': numb, 'u_cart': {}}
                with open(f'{username}.txt', 'w') as f_user:
                    f_user.write(str(u_data))
                self.write_data(username,password)
                break

    def write_data(self, username, password):  # write user username and password in accounts file
        with open('accounts.txt', 'a+') as f:
            f.write(f"'{username}':'{password}',\n")

   

    def login(self):# method overridden from abstract class
        """ Taking username and password for user to login to its account and checking if credentials matches or not"""

        self.accounts=self.read_accounts()
        while True:
            username = input('\nenter username:').strip()
            if len(username)==0:
                print('Username space cannot be empty\n')
            else:
                username=username.lower()
                break
        while True:
            password = input('enter password:')
            if len(password)==0:
                print('Password space cannot be left empty\n')
            else:
                break

        # CHECKING THE username IN [KEYS] AND MATCHING ITS password[VALUE] WITH IT IN THE accounts DICTIONARY


        if len(self.accounts)==0:
            print("Create atleast 1 account first")
        elif username in self.accounts.keys() and self.accounts[username] == password:
            return username
        else:
            print('\n!! Invalid Username OR Password. Try Again !!')
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            return None

class User():
    """ This class has methods for reading,wiring and creating users file"""
    def __init__(self,username):
        self.username=username
        self.data=self.read_user_file()
   
    
    
    def read_user_file(self):
        with open(f'{self.username}.txt', 'r') as f_user:
            return eval(f_user.read())
    
    def write_user_file(self):
        with open(f'{self.username}.txt', 'w') as f_user:
            f_user.write(str(self.data))

    def create_user_file(self, u_data):
        with open(f'{self.username}.txt', 'w') as f_user:
            f_user.write(str(u_data))


class Products:
    """This class products has info about the products and has 2 methods which keep check on stock"""
    def __init__(self,id,name,price,stock):
        self.id=id
        self.name=name
        self.price=price
        self.stock=stock
    
    def update_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        else:
            return False

    def is_stock_available(self, quantity):
        if self.stock > quantity or self.stock==quantity:
            return True



class Inventory:
    """This class has functions which saves inventory in a file where admin can check invertory , update inventory and
    delete products from and view products list to the user """

    def load_inv(self):  # creates a file inventory in which write products info and handle  exception file not found
        try:
            with open('inventory.txt', 'r') as inv_file:
                inv_list = []
                for line in inv_file:
                    id, name, price, stock = eval(line.strip())
                    inv_list.append(Products(id, name, price, stock))
                return inv_list
        except FileNotFoundError:
            print('*No Products File Found! \nLogin as an admin and add some products to the store*')
            return []
    



    def __init__(self):
        self.products= self.load_inv()

    

    def get_inv_id(self):  # has id of all the products
        stored_id=[]
        for inv_items in self.products:
            stored_id.append(inv_items.id)
        return stored_id
            
    def view_products(self):  # for viewing the products loaded from the file
        self.products=self.load_inv()
        print('\n\n')
        print("-------------SMART HOME SOLUTIONS!------------")
        print("______________________________________________")
        print("   id    name        :    price        | stock")
        for p in self.products:
            print(f"{p.id:4}. {p.name:15}: {'':2}RS. {p.price:7} {'':2}|{p.stock:3}")
        print("____________________________________________")
        print('\n\n')

    def view_current_inv(self):
        print('\n\n')
        print("-------------SMART HOME SOLUTIONS!------------")
        print("______________________________________________")
        print("   id    name        :    price        | stock")
        for p in self.products:  
            print(f"{p.id:4}. {p.name:15}: {'':2}RS. {p.price:7} {'':2}|{p.stock:3}")
        print("____________________________________________")
        print('\n\n')

############################################################################
######### EXCLUSIVE ADMIN CONTROL FUNCTIONS OF CLASS INVENTORY #############
############################################################################

        ##########################################
        ##   ADMIN PANEL ACCESS CODE: KHI-0021  ##
        ##   ADMIN USERNAME:admin1              ##
        ##   ADMIN PASSWORD:AdminUniquePass     ##
        ##########################################



    def update_inventory_file(self):  # UPDATES CHANGES MADE IN PRODUCTS IN THE FILE
        with open('inventory.txt', 'w') as inv_file:
            for product in self.products:
                inv_file.write(f"('{product.id}', '{product.name}', {product.price}, {product.stock})\n")

    def update_inv_stock(self):  # allows admin to update stock for existing product
        self.view_products()
        ids = self.get_inv_id()
        while True:
            _id = input("Enter product id to update the stock (or) press 'e' to go back\n -> ").strip()
            if _id == "e" or _id == "E":
                break
            if _id in ids:
                for p_items in self.products:
                    if _id == p_items.id:
                        print(f"available stock of {p_items.name} is {p_items.stock}")
                        while True:
                            stock=input('Enter stock: ').strip()
                            if not stock.isdigit():
                                print('Enter a valid quantity!')
                            else:
                                stock=int(stock)
                                p_items.stock= stock
                                self.update_inventory_file()
                                print (f'\nStock of {p_items.name}(product ID:{_id}) has been updated with {stock}!\n')
                                break
                        break
            else:
                print("Product ID not found!")

    def add_products(self):    # ADD PRODUCTS IN INVENTORY
        ids=self.get_inv_id()
        self.view_products()
        while True:
            _id=input("\nEnter product id to add in inventory (or) press 'e' to go back\n -> ").strip()
            if _id=="e" or _id=="E":
                break
            if _id in ids:
                print(f"\n*A product with the same Product Id: {_id} exists*\nPlease enter a different Product ID!\n")
            else:
                while True:
                    name=input("Enter product name: ").strip()
                    if len(name)==0:
                        print("!Product name cannot be left Empty!\n")
                    else:
                        break
                while True:
                    price=input("Enter product price: ").strip()
                    if not price.isdigit():   # CHECK IF INPUT DOES NOT CONTAIN ANY OTHER CHARACTER INSTEAD OF DIGITS
                        print('\nEnter a valid quantity !\n')
                    else:
                        price=int(price)
                        break
                while True:
                    stock=input('Enter the stock: ').strip()
                    if not stock.isdigit():   # CHECK IF INPUT DOES NOT CONTAIN ANY OTHER CHARACTER INSTEAD OF DIGITS
                        print('\nEnter a valid quantity !\n')
                    else:
                        stock=int(stock)
                        new_product=Products(_id,name,price,stock)
                        self.products.append(new_product)
                        print(f'\n {name} (product ID:{_id}) added to the store inventory\n')
                        self.update_inventory_file()
                        break
                    break
    
    def remove_products(self): # Allows admin to remove any product
        ids=self.get_inv_id()
        self.view_products()
        while True:
            _id=input("Enter product id to remove the product from store inventory (or) press 'e' to go back\n -> ").strip()
            if _id=="e" or _id=="E":
                break
            if _id in ids:
                for p_items in self.products:
                    if _id == p_items.id:
                        self.products.remove(p_items)
                        self.update_inventory_file()
                        print(f"\nProduct {p_items.name} (product id:{_id}) has been removed from the inventory.\n")
                        break
            else:
                print("Product ID not found!")
#############################################################################################################


class Cart(Inventory): #ASSOCIATION
    """ This class has all the function user will use while shopping ex:shopping history,add to cart,logout"""
    def __init__(self):
        super().__init__()
        self.cart = {}  # cart is a dictionary which stores products name and its quantity add by the user
        self.bill = 0.0
        self.coupon=None

    def add_to_cart(self):  # allow user to add their favourite products in the cart and has some checks if product exists or not
        ids = super().get_inv_id()
        while True:

            self.view_current_inv()
            user_input = (input("Enter ID of product\nor press 'e' to go back\n->  "))
            if user_input=='e' or user_input=='E':
                break

            if user_input in ids:
                for item in self.products:
                    if item.id == user_input:
                        if item.stock==0:
                            print('\nOut of Stock\n')
                            break

                        while True:
                            quantity=input('\nEnter quantity: ').strip()
                            if not quantity.isdigit():
                                print('\nEnter a valid quantity\n ')
                            else:
                                quantity=int(quantity)
                                if quantity>0:
                                    if item.is_stock_available(quantity):  # Check stock availability
                                        item.update_stock(quantity)  # Update stock
                                        self.bill += item.price * quantity # calculate total bill
                                        print(f" {quantity} {item.name}  Added to your cart")
                                        print(f"Remaining stock for {item.name}: {item.stock}")
                                        if item.name in self.cart.keys():
                                            self.cart[item.name]["quantity"] += quantity
                                            break
                                        else:
                                            self.cart[item.name] = {'price': item.price, 'quantity': quantity}
                                        break
                                    else:
                                        print(f"\nSorry, only {item.stock} items available in stock for {item.name}")
                                else:
                                    print('\nEnter a Valid quantity\n')
                        
                        break
                    
            else:
                print('_______________________________________________________')
                print("\n||  Product ID not found!  ||")

    def view_cart(self): # allow user to see their cart
        print('______________________________________')
        print ('\n -------  -----Your Cart-----  -------\n')
        if len(self.cart)==0:
            print ('* Your Cart is Empty :(\n----------------------\n\n')
            print('______________________________________\n')
        else:
            for product_name, details in self.cart.items():
                print(f"{product_name:16} RS. {details['price']} each  x {details['quantity']}")
            deliverycharges=300
            print('\n_____________________________________')
            print(f"Sub Total:                 Rs. {self.bill}")        
            print(f"Standard delivery charges: Rs.{deliverycharges}") 
            if self.coupon==None:
                print(f'\nTotal bill:              Rs. {self.bill+deliverycharges}')
            else:
                calc_disc= self.bill* Cart.discount_coupons[self.coupon]
                print(f"Coupon discount {((Cart.discount_coupons[self.coupon])*100)}% OFF: -Rs.{calc_disc}")
                print(f'\nTotal bill:              Rs. {(self.bill+deliverycharges)-calc_disc}')
            print('______________________________________')
            print('______________________________________\n')


    def remove_from_cart(self): # allow user to remove from cart by using product id and stock up the inventory when user does remove anything from cart

        if len(self.cart)==0: # empty cart situation
            self.view_cart()
            print("*" * 6, "ADD PRODUCTS TO THE CART TO REMOVE", "*" * 6)
            print('_'*46,'\n\n')
        else:
            ids=super().get_inv_id()
            while True:
                self.view_current_inv()
                print()
                self.view_cart()
                user_input = (input("Enter ID of product from inventory corresponding to the product in your cart\nor press 'e' to go back\n->  ")).strip()
                if user_input=='e' or user_input=='E':
                    break

                if  user_input in ids:
                    for item in self.products:
                        if item.id == user_input:
                            if item.name in self.cart.keys():
                                while True:
                                    quantity=input('\nEnter quantity: ').strip()
                                    if not quantity.isdigit():
                                        print('\nEnter a valid quantity\n ')
                                    elif quantity == '0' :
                                        print("\nEnter a Valid Quantity!")
                                    else:
                                        quantity=int(quantity)
                                        if quantity <= self.cart[item.name]['quantity']:
                                            self.cart[item.name]['quantity']-=quantity
                                            if self.cart[item.name]['quantity'] == 0:
                                                self.cart.pop(item.name)
                                            self.bill-= (item.price * quantity)
                                            item.stock+=quantity # added item back to stock
                                            print(f"\n-> {quantity} {item.name} removed from the cart!\n")
                                            break
                                        else:
                                            print('\nQuantity exceeds the existing number of this product !!')
                            elif item.name not in self.cart.keys():
                                print ('\nItem is not in the cart!')
                            
                            break
                else:
                    print('_______________________________________________________')
                    print("\n||  Product ID not found!  ||")                                            
                                

    def shop_hist(self,data): # show users previous purchases with date and time and has check history is not available
        username=data.get('u_name')
        f_user_r=open(f'{username}.txt','r')
        f_user_r.seek(0)
        read=f_user_r.read()
        u_data=eval(read)
        u_cart=u_data['u_cart']
        print ('\n\n\n\n\n________________________________________________________')
        print ('___________________SHOPPING HISTORY___________________\n')
        print ('  ------date/time:  --------- items purchase:---- ')
        if len(u_cart)==0:
            print('            No Shopping History !\n\n')
        else:
            for date,history in u_cart.items():#saving history
                cart_history=''
                total=0
                c_code=None
                for name,details in list(history.items()):
                    if name =='coupon':
                        c_code=history[name]['code']
                        del history[name]
                    else:
                        price=details['price']
                        quantity=details['quantity']
                        total+= (price * quantity)
                        cart_history=cart_history+ f"{name:10}  --- Rs. {price} x {quantity}\n{'':27}"
                print (f'\n{date}   :     {cart_history}')
                print (f'-> Delivery Charges:  Rs.300\n')
                if c_code==None:
                    print(f"Sub Total:                  Rs.{total}")
                    print(f"Standard Delivery Charges:  Rs.",300)
                    print(f'  ::: Total bill:           Rs.{total+300}\n')
                else: # if coupon is added
                    disc_am=(total*Cart.discount_coupons[c_code])
                    print(f"Sub Total:                 Rs.{total}")
                    print(f"Standard Delivery Charges: Rs.",300)
                    print(f"Discount coupon used for {(Cart.discount_coupons[c_code])*100}% OFF")
                    print (f'::: Total bill:           Rs.{(total+300)-disc_am}\n')
                print (f'{"":8}-----------------------------------{"":5} ')
            print ('________________________________________________________')
            print ('________________________________________________________\n\n\n')


    
    def checkout(self,data):
        """allow user to checkout their cart and pay bill from 2 methods and has some chceks for checking user inputs  """
        username=data.get('u_name')
        u_cart=data.get('u_cart')
        if len(self.cart)==0: # CHECK IF cart DICTIONARY IS EMPTY
            print('\n\n No items in cart. Add atleast one product to proceed to checkout !!')
        else:
            self.view_cart()
            
            while True:
                confirm=input('\nSelect a suitable option\n (y)  To proceed or make changes\n (d)  Use Discount Coupon\n (n)  To go back:\n ->').strip()
                if confirm == "Y" or confirm =="y":

                    while True:
                        pay=input("\nSelect Payment Method\n1. Cash on Delivery\n2. Credit/Debit Card\n ->").strip()
                        if pay=='1':
                            if self.coupon==None:
                                print(f"You have to pay Rs.{self.bill+300} to our delivery rider!")
                                break
                            else:
                                dis=self.bill*Cart.discount_coupons[self.coupon]
                                print(f"You have to pay Rs.{(self.bill+300)-dis} to our delivery rider!")
                                break


                        elif pay=='2':
                            while True:
                                card=input('Enter your 16 digit Credit Card Number: ').strip()
                                if not card.isdigit():
                                    print('\nEnter a Valid credit Card number\n')

                                elif len(card)!=16:
                                    print('\nEnter complete Card number\n')
                                else:
                                    break 

                            while True:
                                c_name=input("Enter Card Holder Name: ").strip()
                                c_list=c_name.split()
                                if not all(alpha.isalpha() for alpha in c_list):
                                    print("\nEnter a valid name containig alphabets only\n")
                                else:
                                    break

                            while True:
                                c_exp = input("Enter Card Expiry Date [FORMAT: MM/YY]: " ).strip()
                                if len(c_exp)!=5 and not c_exp[:2].isdigit() and not c_exp[3:].isdigit() and c_exp[2] != '/':
                                    print('\nInvalid date format\n')
                                    continue
                                # exception for chceking the card credentials
                                try:
                                    mm, yy = map(int, c_exp.split('/'))
                                except ValueError:
                                    print('\nInvalid date format\n')
                                    continue

                                if not (1 <= mm <=12):
                                    print("\nInvalid date\n")
                                    continue
                                if (yy == 24) and (1 <= mm <= 7):
                                    print('\nCard Expired')
                                    continue
                                if (yy < 24) and (1 <= mm <= 12):
                                    print("\nCard Expired\n")
                                    continue
                                if (yy > 24) and (1 <= mm <= 12):
                                    break
                                break
                            while True:
                                c_cvv = input("\nEnter cvv written at the back of your card: ").strip()
                                if not c_cvv.isdigit():
                                    print("\nInvalid input\n")
                                    
                                elif len(c_cvv) != 3:
                                    print('\nInput exceeds 3-digit range\n')
                                else:
                                    break
                            print("\n ( *PROCCESSING PAYMENT FROM CARD...) \n\n")
                            self.view_cart()               
                            if self.coupon == None:
                                print(f" Rs.{self.bill+300} have been deducted from your card!")
                                break
                            else:
                                dis=self.bill*Cart.discount_coupons[self.coupon]
                                print(f" Rs.{(self.bill+300)-dis} have been deducted from your card!")
                                break
                        else:
                            print("\nEnter a Valid option\n")
                    f_user_w=open(f'{username}.txt','w') # OPEN USER FILE IN WRITE MODE TO OVERWRITE OLD DATA WITH UPDATED DATA.

                    from datetime import datetime 
                    curr_datetime = datetime.now() # GET THE CURRENT DATE AND TIME 
                    format = curr_datetime.strftime("%Y-%m-%d / %H:%M") # FORMAT THE CURRENT DATE AND TIME
                    # SAVING THE "self.cart" DICTIONARY IN THE "u_cart" DICTIONARY WHICH IS SAVED IN THE USER DATA "data" DICTIONARY
                    self.cart['coupon']={'code':self.coupon}
                    data['u_cart'][format]=self.cart  
                    final_udata=str(data)
                    f_user_w.write(final_udata)
                    f_user_w.close()
                    print("\n\nThank You for placing your order. Your order will be delivered to your billing address within a week. :)\n")
                    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n')
                    self.cart.clear() # CLEARING cart DICTIONARY FOR FURTHER PURCHASE
                    self.bill-=self.bill # CLEARING THE BILL FOR FURTHER PURCHASE
                    self.update_inventory_file() # UPDATING THE INVENTORY FILE WITH THE CURRENT AVAILABLE STOCK
                    self.coupon=None  # RESETING THE COUPON CODE FOR ANOTHER PURCHASE
                    break
                elif confirm=="n" or confirm=="N":
                    print()
                    break
                elif confirm=='d' or confirm=='D':
                    if self.coupon==None:
                        self.coupon=self.discount(u_cart)
                    else:
                        print('\nA Coupon is already used')
                    
                elif confirm!="n" or "N" or "y" or "Y":
                    print('\n!! CHOOSE A VALID OPTION !!')
    
    # DISCOUNT COUPON DICTIONARY HAVING [KEY]=COUPON CODE(str) AND [VALUE]=PERCENT DISCOUNT CONVERTED INTO DECIMAL FOR CALCULATION(float)
    discount_coupons={'NEW40':0.40,
                      'OFF30':0.30,
                      'OFF25':0.25}
   
    def discount(self,u_cart): #provide checks for coupns if it is already availed or can be availed
        while True:
            u_input=input('\nEnter the coupon code or (e) to go back\n -> ').strip()
            if u_input=='e' or u_input=='E':
                return None
            if u_input in Cart.discount_coupons.keys():
                if u_input == 'NEW40':
                    if len(u_cart)==0:
                        print(f'\nCoupon {u_input} is availed!\n')
                        return u_input
                    else:
                        print('\nYou are not eligible for the particular discount.\nIts only for the new users for their first purchase!\n')
                else:
                    print(f'\nCoupon {u_input} is availed!\n')
                    return u_input
            else:
                print('\nInvalid Coupon Code\n')
                

    def logout(self): # allows user to logout from the account
        print('\n|*| Are you sure you want to logout of your account?\nDoing so will clear your cart for the current session. |*|\n')
        while True:
            confirm=input('Press (y) for yes       press (n) for No\n -> ').strip()
            if confirm == 'y' or confirm =='Y':
                self.cart.clear()
                self.bill-=self.bill
                self.products=self.load_inv()
                self.coupon=None
                print('\n____________________________________________\n   Logging Out...   \n\nThank you for your visit. Hoping to see you again! :)\n')
                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n')
                return True
            elif confirm == 'n' or confirm =='N':
                print('\nGoing Back to the Main Menu...\n')
                return False
            else:
                print('\nEnter a Valid option! ')



class Store:
    """This class has the outlook of the store user options ,admin options all are here"""
    def __init__(self):
        self.account=Account_manager()
        self.loggedin_user=None

    def user_menu(self,User):
        
        while True:
                
            print('__________________')
            print('<>  MAIN MENU  <>')
            print('------------------')
            a=input("\n1.View Product List\n2. Add to cart\n3.Remove from Cart\n4.View cart\n5.View Shopping History\n6.Proceed to checkout\n7.Log out\nSelect serial number of any one:\n->").strip()

            # VIEW PRODUCT LIST
            if a=='1': 
                print('\n\n')
                run_c.view_current_inv() # running the cart object
                
                                    
            # ADD PRODUCTS TO CART
            elif a=='2':  
                run_c.add_to_cart()  # running the cart object
                
                
            # REMOVE PRODUCTS FROM CART    
            elif a=='3':
                run_c.remove_from_cart()  # running the cart object
                pass
                
            # VIEW CART
            elif a=='4':
                print('\n\n\n')
                run_c.view_cart()   # running the cart object
                
            # VIEW SHOPPING HISTORY
            elif a=='5':
                run_c.shop_hist(User)   # running the cart object
            # CHECKOUT
            elif a=='6':
                run_c.checkout(User)    # running the cart object

                # LOGOUT OF ACCOUNT        
            elif a == '7':
                logout=run_c.logout()
                if logout:
                    break
    
            else:
                print('\n!! CHOOSE AN APPROPRIATE OPTION !!\n')

    def admin_menu(self):
        """ provide options for the admin to make changes in the application ie; add products,delete user file,add stock
         ,view registered account"""
        while True:
            print('\n   < ADMIN PANEL > \n')
            print('1. View Inventory')
            print('2. Add products to Inventory')
            print('3. Remove products from Inventory')
            print('4. Update stock of existing Products')
            print('5. View Registered Accounts')
            print('6. Delete a user account and its data')
            print('7. Logout from Admin Account\n')
            option = input('Select an option: ').strip()
            if option == '1':
                run_items.view_products()  # running the inventory object

            elif option == '2':
                run_items.add_products()  # running the inventory object

            elif option == '3':
                run_items.remove_products()  # running the inventory object

            elif option == '4':
                run_items.update_inv_stock()  # running the inventory object

            elif option == '5':

                print('\n\n-----Registered Users-----\n')
                print('*** Usernames *** ')
                user_numbers = 0
                counter = 1
                user_accounts = run_app.account.read_accounts()
                for username in user_accounts.keys():
                    print(f'{counter}.  {username}')
                    user_numbers += 1
                    counter += 1
                print(f'\nTotal No. of users: {user_numbers}\n\n')


            elif option == '6':  #  Delete a user account and its data
                print('\n\n-----Registered Users-----\n')
                print('*** Usernames *** ')
                user_numbers = 0
                counter = 1
                user_accounts = run_app.account.read_accounts()
                for username in user_accounts.keys():
                    print(f'{counter}.  {username}')
                    user_numbers += 1
                    counter += 1
                print(f'\nTotal No. of users: {user_numbers}\n\n')
                while True:
                    username = input('\nEnter the username of the account in the given space to delete the user\n(OR) press ENTER key to go back\n -> ').strip().lower()
                    # if username == 'e' or username == 'E':
                    if len(username)==0:
                        break
                    if username in user_accounts.keys():
                        try:
                            os.remove(f'{username}.txt')
                        except FileNotFoundError:
                            print('\nUser File Already Deleted')
                        del user_accounts[username]
                        with open('accounts.txt', 'w') as f:
                            for uname, passw in user_accounts.items():
                                f.write(f"'{uname}':'{passw}',\n")
                        print(f'\nAccount {username} deleted successfully')
                        break

                    elif os.path.exists(f'{username}.txt'):
                        os.remove(f'{username}.txt')
                        print(f'\nAccount already deleted. Deleted the abandoned user file {username}.txt')
                        break

                    else:
                        print(f'\nNo account found with username {username}')
            elif option == '7':
                print('\nLogging out...')
                print('\n--LOGGED OUT OF ADMIN ACCOUNT--\n\n')
                break
            else:
                print('\n!! Enter a Valid Option!! \n')

    def main_menu(self):
        while True:
            print('\n\n======================================')
            print('| Welcome To THE SMART HOME SOLUTIONS" |')
            print('======================================\n')
            print('1. User')
            print('2. Admin')
            print('\n3. Exit Application\n')
            choice = input('\nSelect an option:').strip()
            
            # USER LOGIN
            if choice=='1':  
                while True:
                    print('\n--------------------')
                    print('1. Create Account')
                    print('2. Login')
                    print('press "e" to go back\n')
                    choice_1 = input('\nSelect an option:').strip()
                    # CREATE AN ACCOUNT
                    if choice_1=='e' or choice_1== 'E':
                        break
                    if choice_1=='1':
                        self.account.create_account()
                    
                    # LOGIN
                    elif choice_1=='2':
                        self.loggedin_user=self.account.login()
                        if self.loggedin_user:
                            user=User(self.loggedin_user)
                            user_data=user.read_user_file()
                            fname=user_data.get('f_name')
                            print(f'\n\n\n\n\n ===================LOGIN SUCCESSFUL.\n\n----Welcome "{fname}!"----')
                            self.user_menu(user_data)
                        
                       
                    else:
                        print ('\nEnter a valid option! ')
            
            # ADMIN LOGiN
            elif choice=='2':
                        ##########################################
                        ##   ADMIN PANEL ACCESS CODE: KHI-0021  ##
                        ##   ADMIN USERNAME:admin1              ##
                        ##   ADMIN PASSWORD:AdminUniquePass     ##
                        ##########################################
                while True:
                    print('\n  <Admin Authentication>')
                    access_code=input('\nEnter the UNIQUE ACCESS CODE provided to you\n(Or) Enter "e" to exit Admin Authentication\n-> ').strip()
                    
                    if access_code=='e' or access_code=='E':
                        break
                    if access_code=='KHI-0021':
                        print ('   <ACCESS GRANTED! >\n')
                        while True:
                            while True:
                                a_username=input('Enter admin username: ').strip().lower()
                                if len(a_username)==0:
                                    print('\nUsername space cannot be left empty\n')
                                else:
                                    break
                            while True:
                                a_pass=input('Enter password: ').strip()
                                if len(a_pass)==0:
                                    print('\nPassword space cannot be left empty\n ')
                                else:
                                    break
                            if (a_username=='admin1') and (a_pass=='AdminUniquePass'):
                                print('\n\n****************************')
                                print('     <#> Admin access <#>   ')
                                print('****************************')
                                self.admin_menu()
                                break
                    
                            else:
                                print("Invalid credentials\n")
                                break
                    else:
                        print("\n   < ACCESS DENIED! > \nPlease Enter the approprate code\n\n\n")
            # EXIT THE APPLICATION
            elif choice=='3':
                print('\nApplication closed!\n')
                break
            else:
                print('\n! Invalid Choice !')
                print('==================')


run_items=Inventory()  # object of inventory class
run_app=Store()  # object of store class
run_c=Cart()  # object of cart class
run_app.main_menu()
