from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from datetime import date
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter.ttk import Combobox
#import xlrd
#from openpyxl import Workbook
import pathlib 
from tkinter import Tk, Button, font, Label, Text, TOP, X,CENTER
from tkinter import Tk, Label
from PIL import Image, ImageTk
from tkinter import Tk, Label, Entry, Button, messagebox

#root=Tk()
#root.title("Super Market Management System")
#root.geometry("1250x1250+210+110")
background="#006994" #background
framebg="EDEDED"
framefg="#06283D"

master = Tk()
master.geometry("1270x1100")
master.title("Super Market Management System")
master.configure(bg=background)
image=Image.open("a.jpg")
photo=ImageTk.PhotoImage(image)
background_label = Label(master, image=photo)
image = image.resize((1200,900), Image.ANTIALIAS)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#top frame
Label(master, text="Email: bnmsupermarket@gmail.com", fg="black", width=10, background="pale green", anchor='e').pack(side=TOP, fill=X)
screen_width = master.winfo_screenwidth()
label_text = "Super Market Management System using Secondary Indexing"
label = Label(master, width=screen_width, height=3, background="#06283D", font=("Arial", 26), wraplength=1000)
label.config(justify=CENTER)
label.config(text=label_text)
label.config(foreground="white")  # Set the label text color to white
label.pack(side=TOP, fill=X, padx=10, pady=(10, 0))

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "12345":
        adminwindow()
    else:
        messagebox.showinfo("Try again!", "Invalid username or password")

username_label = Label(master, text="Admin Username:",font=('calibre', 12, 'normal'))
username_label.place(x=585, y=200)
username_entry = Entry(master,  font=('calibre', 10, 'normal'))
username_entry.place(x=575, y=230)

password_label = Label(master, text="Admin Password:",font=('calibre', 12, 'normal'))
password_label.place(x=585, y=265)
password_entry = Entry(master, show="*",  font=('calibre', 10, 'normal'))
password_entry.place(x=575, y=295)

btn1 = Button(master, text="LOGIN", command=login, width=15, height=2)
btn1.place(x=590, y=350)


def adminwindow():
    #adminwindows=Toplevel(master)
    #adminwindows.title("Admin Window")
    #adminwindows.geometry("500x500")
    #Label(adminwindows,text="Hello Admin!")

    # Global file paths
    datafile = "product_data.txt"
    indexfile = "primary_index.txt"
    sindexfile = "secondary_index.txt"

   
    

    def add_product():
        # Create a new window for adding a product
        add_window = tk.Toplevel(window)
        add_window.title("Add Product")
        add_window.geometry("1270x1100")
        add_window.configure(bg="light blue")

        def add():
            try:
                product_number = entry_number.get().strip()
                product_name = entry_name.get().strip()
                quantity = entry_quantity.get().strip()
                price = entry_price.get().strip()

                if not product_number or not product_name or not quantity or not price:
                    messagebox.showerror("Error", "Please fill in all fields.")
                    return

                with open(datafile, 'a') as file:
                    file.write(f"{product_number}|{product_name}|{quantity}|{price}\n")

                offset = 0
                with open(datafile, 'r') as file:
                    file.seek(0, 2)  # Move the file pointer to the end of the file
                    offset = file.tell() - len(f"{product_number}|{product_name}|{quantity}|{price}\n")-1

                with open(indexfile, 'a') as index_file:
                    index_file.write(f"{product_number}|{offset}\n")

                with open(sindexfile, 'a') as sindex_file:
                    sindex_file.write(f"{product_name}|{product_number}\n")

                messagebox.showinfo("Success", "Product added successfully.")
                add_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        label_number = tk.Label(add_window, text="Product Number:", font=('calibre', 15, 'bold'))
        label_number.place(x=380, y=100) 
        entry_number = tk.Entry(add_window, font=('calibre', 15, 'normal'))
        entry_number.place(x=600, y=105)

        label_name = tk.Label(add_window, text="Product Name:", font=('calibre', 15, 'bold'))
        label_name.place(x=380, y=150)
        entry_name = tk.Entry(add_window, font=('calibre', 15, 'normal'))
        entry_name.place(x=600, y=155)

        label_quantity = tk.Label(add_window, text="Quantity:", font=('calibre', 15, 'bold'))
        label_quantity.place(x=380, y=200)
        entry_quantity = tk.Entry(add_window, font=('calibre', 15, 'normal'))
        entry_quantity.place(x=600, y=205)   

        label_price = tk.Label(add_window, text="Price:", font=('calibre', 15, 'bold'))
        label_price.place(x=380, y=250)
        entry_price = tk.Entry(add_window, font=('calibre', 15, 'normal'))
        entry_price.place(x=600, y=255)


        button_font = font.Font(size=10)
        button_add = tk.Button(add_window, text="Add", command=add, height=1, width=11, font = button_font)
        button_add.place(x=530, y=350)

    def search_product():
        # Create a new window for searching a product
        search_window = tk.Toplevel(window)
        search_window.title("Search Product")
        search_window.geometry("1270x1100")
        search_window.configure(bg="light green")

        def search():
            try:
                product_number = entry_search.get().strip()

                if not product_number:
                    messagebox.showerror("Error", "Please enter a product name.")
                    return

                found = False
                result = ""

                with open(sindexfile, 'r') as file:
                    lines = file.readlines()

                for line in lines:
                    line = line.strip()
                    if line.startswith(product_number + "|"):
                        product_number = line.split("|")[1]
                        with open(datafile, 'r') as data_file:
                            data_lines = data_file.readlines()
                        for data_line in data_lines:
                            data = data_line.strip().split("|")
                            if data[0] == product_number:
                                result += f"Product Number: {data[0]}\n"
                                result += f"Product Name: {data[1]}\n"
                                result += f"Quantity: {data[2]}\n"
                                result += f"Price: {data[3]}\n\n"
                                found = True
                                break

                if found:
                    messagebox.showinfo("Search Result", result)
                else:
                    messagebox.showinfo("Not Found", "No products found with the given name.")
                search_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        label_search = tk.Label(search_window, text="Product Name:", font=('calibre', 15, 'bold'))
        label_search.place(x=380, y=200)

        entry_search = tk.Entry(search_window, font=('calibre', 15, 'normal'))
        entry_search.place(x=600, y=205)

        button_font = font.Font(size=10)
        button_search = tk.Button(search_window, text="Search", command=search, height=1, width=11, font = button_font)
        button_search.place(x=530, y=350)

    def delete_product():
        # Create a new window for deleting a product
        delete_window = tk.Toplevel(window)
        delete_window.title("Delete Product")
        delete_window.geometry("1270x1100")
        delete_window.configure(bg="lemon chiffon")

        def delete():
            try:
                product_number = entry_delete.get().strip()

                if not product_number:
                    messagebox.showerror("Error", "Please enter a product number.")
                    return

                with open(datafile, 'r') as file:
                    data_lines = file.readlines()

                found = False
                for i, data_line in enumerate(data_lines):
                    data = data_line.strip().split("|")
                    if data[0] == product_number:
                        data_lines[i] = data_line.replace(product_number, "$")
                        found = True
                        break

                if found:
                    with open(datafile, 'w') as file:
                        file.writelines(data_lines)

                    with open(indexfile, 'r') as index_file:
                        index_lines = index_file.readlines()

                    with open(indexfile, 'w') as index_file:
                        for index_line in index_lines:
                            if index_line.startswith(product_number + "|"):
                                continue
                            index_file.write(index_line)

                    with open(sindexfile, 'r') as sindex_file:
                        sindex_lines = sindex_file.readlines()

                    with open(sindexfile, 'w') as sindex_file:
                        for sindex_line in sindex_lines:
                            if sindex_line.endswith("|" + product_number + "\n"):
                                continue
                            sindex_file.write(sindex_line)

                    messagebox.showinfo("Success", "Product deleted successfully.")
                else:
                    messagebox.showinfo("Not Found", "No product found with the given number.")
                delete_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        label_delete = tk.Label(delete_window, text="Product Number:", font=('calibre', 15, 'bold'))
        label_delete.place(x=380, y=200)

        entry_delete = tk.Entry(delete_window, font=('calibre', 15, 'normal'))
        entry_delete.place(x=600, y=205)

        button_font = font.Font(size=10)
        button_delete = tk.Button(delete_window, text="Delete", command=delete, height=1, width=11, font = button_font)
        button_delete.place(x=530, y=350)

    def display_products():
        # Create a new window for displaying products
        display_window = tk.Toplevel(window)
        display_window.title("Display Products")
        display_window.geometry("1270x1100")
        display_window.configure(bg="light salmon")

        with open(datafile, 'r') as file:
            data_lines = file.readlines()

        with open(indexfile,'r') as ifile:
            i_line = ifile.readlines()

        with open(sindexfile,'r') as sfile:
            s_line = sfile.readlines()
        
        
        result = ""
        ifi=""
        sr=""
        
        for data_line in data_lines:
            data = data_line.strip().split("|")
            result += f"Product Number: {data[0]}\n"
            result += f"Product Name: {data[1]}\n"
            result += f"Quantity: {data[2]}\n"
            result += f"Price: {data[3]}\n\n"
        for i in i_line:
            d=i.strip().split("|")
            ifi+=d[0]
            ifi+=" "+d[1]+"\n"
        for s in s_line:
            d=s.strip().split("|")
            sr+=d[0]
            sr+=" "+d[1]+"\n"
        
        text_display = tk.Text(display_window)
        text_display.insert(tk.END, result)
        text_display.insert(tk.END,"Primary File:\n")
        text_display.insert(tk.END, ifi)
        text_display.insert(tk.END,"\n")
        text_display.insert(tk.END,"Secondary File:\n")
        text_display.insert(tk.END, sr)

        text_display.pack()

    #modify function
    def modify_product():
        modify_window = tk.Toplevel(window)
        modify_window.title("Modify Product")
        modify_window.geometry("1270x1100")
        modify_window.configure(bg="light pink")

        def modify():
            old = entry_old.get().strip()
            print(old)
            product_number = entry_number.get().strip()
            product_name = entry_name.get().strip()
            quantity = entry_quantity.get().strip()
            price = entry_price.get().strip()

            with open(sindexfile, 'r+') as file:
                lines = file.readlines()

            with open(datafile, 'r+') as da:
                data_lines = da.readlines()

            with open(indexfile, 'r+') as ia:
                index_lines = ia.readlines()

            found = False

            for i, data_line in enumerate(data_lines):
                data = data_line.strip().split("|")
                if data[0] == old:
                    data_lines[i] = f"{product_number}|{product_name}|{quantity}|{price}\n"
                    found = True
                    break

            if found:
                with open(datafile, 'w') as file:
                    file.writelines(data_lines)

                with open(sindexfile, 'r') as sindex_file:
                    sindex_lines = sindex_file.readlines()

                with open(sindexfile, 'w') as sindex_file:
                    for sindex_line in sindex_lines:
                        if sindex_line.endswith(f"|{old}\n"):
                            sindex_line = f"{product_name}|{product_number}\n"
                        sindex_file.write(sindex_line)

                offset = 0
                with open(datafile, 'r') as file:
                    file.seek(0, 2)
                    offset = file.tell() - len(f"{product_number}|{product_name}|{quantity}|{price}\n") - 1

                with open(indexfile, 'w') as index_file:
                    for index_line in index_lines:
                        if index_line.startswith(f"{old}"):
                            index_line = f"{product_number}|{offset}\n"
                        index_file.write(index_line)

                messagebox.showinfo("Found", "Product has been updated successfully!")
                modify_window.destroy()
            else:
                messagebox.showinfo("Not Found", "No product found with the given number.")

    # Create and configure GUI elements (labels, entry fields, buttons, etc.) here

          
        label_old_number = tk.Label(modify_window, text="Old Product Number:", font=('calibre', 15, 'bold'))
        label_old_number.place(x=380, y=50)
        entry_old = tk.Entry(modify_window, font=('calibre', 15, 'normal'))
        entry_old.place(x=600, y=55)

        label_number = tk.Label(modify_window, text="Product Number:", font=('calibre', 15, 'bold'))
        label_number.place(x=380, y=100)
        entry_number = tk.Entry(modify_window, font=('calibre', 15, 'normal'))
        entry_number.place(x=600, y=105)

        label_name = tk.Label(modify_window, text="Product Name:", font=('calibre', 15, 'bold'))
        label_name.place(x=380, y=150)
        entry_name = tk.Entry(modify_window, font=('calibre', 15, 'normal'))
        entry_name.place(x=600, y=155)

        label_quantity = tk.Label(modify_window, text="Quantity:", font=('calibre', 15, 'bold'))
        label_quantity.place(x=380, y=200)
        entry_quantity = tk.Entry(modify_window, font=('calibre', 15, 'normal'))
        entry_quantity.place(x=600, y=205)

        label_price = tk.Label(modify_window, text="Price:", font=('calibre', 15, 'bold'))
        label_price.place(x=380, y=250)
        entry_price = tk.Entry(modify_window, font=('calibre', 15, 'normal'))
        entry_price.place(x=600, y=255)

        button_font = font.Font(size=10)
        button_modify = tk.Button(modify_window, text="Modify", command=modify, height=1, width=11, font=button_font)
        button_modify.place(x=530, y=350)


    # Function to exit the program
    def exit_program():
        window.quit()

    # Main window
    window = tk.Tk()
    window.title("Administrator Window")
    window.geometry("1270x1100")
    window.configure(bg="#B19CD9")

    # Function to close the project title window
    def close_title_window():
        close_title_window.destroy()
        window.after(0, window.deiconify())

    # Project title window
    # title_window = tk.Toplevel(window)
    # # title_window.title("Stock Management System")
    # # title_window.geometry("600x600")
    # title_window.configure(bg="black")
    # title_label = tk.Label(title_window, text="Stock Management System", font=("sans-serif", 24), pady=20)
 
    # title_label.pack()

    # After 3 seconds, close the title window and launch the main window
    # title_window.after(3000, close_title_window)

   
    # Buttons
    button_font = font.Font(size=9)
    button_add = tk.Button(window, text="Add product", command=add_product, bg="cyan", width=18, height=2, font = button_font)
    button_add.pack(pady=10)

    button_display = tk.Button(window, text="Display product", command=display_products, bg="coral", width=18,height=2, font = button_font)
    button_display.pack(pady=10)

    button_search = tk.Button(window, text="Search product", command=search_product, bg="light green", width=18,height=2, font = button_font)
    button_search.pack(pady=10)

    button_modify = tk.Button(window, text="Modify product", command=modify_product, bg="PaleVioletRed1", width=18,height=2, font = button_font)
    button_modify.pack(pady=10)

    button_delete = tk.Button(window, text="Delete product", command=delete_product, bg="yellow", width=18, height=2, font = button_font)
    button_delete.pack(pady=10)

    button_exit = tk.Button(window, text="Exit",fg="white", command=exit_program, bg="purple", width=18, height=2, font = button_font)
    button_exit.pack(pady=10)

    window.mainloop()

#btn1 = Button(master, text="Login", command=login, width=30, padx=10, pady=10,font=button_font)
#btn1.place(x=480, y=250)


mainloop()
