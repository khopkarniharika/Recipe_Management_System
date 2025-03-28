import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage
import json
import os
from PIL import Image, ImageTk

# JSON file to store recipes
FILE_NAME = "recipes.json"

# Function to load recipes from file
def load_recipes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Function to save recipes to file
def save_recipes():
    with open(FILE_NAME, "w") as file:
        json.dump(recipes, file, indent=4)

# Function to add a new recipe
def add_recipe():
    name = simpledialog.askstring("New Recipe", "Enter Recipe Name:")
    if not name:
        return
    ingredients = simpledialog.askstring("Ingredients", "Enter Ingredients (comma-separated):")
    steps = simpledialog.askstring("Steps", "Enter Preparation Steps:")
    
    if name and ingredients and steps:
        recipes[name] = {"Ingredients": ingredients, "Steps": steps}
        save_recipes()
        update_listbox()
        messagebox.showinfo("Success", "Recipe Added Successfully!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Function to view selected recipe details
def view_recipe():
    try:
        selected_recipe = listbox.get(listbox.curselection())
        recipe = recipes.get(selected_recipe, {})
        if recipe:
            details = f"Ingredients:\n{recipe['Ingredients']}\n\nSteps:\n{recipe['Steps']}"
            messagebox.showinfo(selected_recipe, details)
    except:
        messagebox.showwarning("Selection Error", "Please select a recipe!")

# Function to delete a recipe
def delete_recipe():
    try:
        selected_recipe = listbox.get(listbox.curselection())
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{selected_recipe}'?"):
            del recipes[selected_recipe]
            save_recipes()
            update_listbox()
            messagebox.showinfo("Success", "Recipe Deleted Successfully!")
    except:
        messagebox.showwarning("Selection Error", "Please select a recipe!")

# Function to update the listbox with recipes
def update_listbox():
    listbox.delete(0, tk.END)
    for recipe in recipes.keys():
        listbox.insert(tk.END, recipe)

# GUI Setup
root = tk.Tk()
root.title("Recipe Management System")
root.geometry("500x500")

# Load background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to place the background
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Title Label
title_label = tk.Label(root, text="Recipe Management", font=("Arial", 16, "bold"), bg="#FFE4B5", fg="black")
title_label_window = canvas.create_window(250, 30, window=title_label)

# Listbox to display recipes
listbox = tk.Listbox(root, width=50, height=10, bg="white", fg="black")
listbox_window = canvas.create_window(250, 150, window=listbox)
update_listbox()

# Buttons with Styling
btn_frame = tk.Frame(root, bg="#FFD700")
canvas.create_window(250, 350, window=btn_frame)

btn_add = tk.Button(btn_frame, text="Add Recipe", command=add_recipe, width=15, bg="#FFA500", fg="white")
btn_add.grid(row=0, column=0, padx=5)

btn_view = tk.Button(btn_frame, text="View Recipe", command=view_recipe, width=15, bg="#32CD32", fg="white")
btn_view.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(btn_frame, text="Delete Recipe", command=delete_recipe, width=15, bg="red", fg="white")
btn_delete.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()
