import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import random  # Simulated prediction

# ---------- Simulated Prediction Function ----------
def predict_freshness(image_path):
    return random.choice(["Fresh", "Not Fresh", "Old"])

# ---------- Analyze Button Function ----------
def analyze_image():
    if not app_data.get("file_path"):
        messagebox.showwarning("No File", "Please upload a Tilapia image.")
        return

    result = predict_freshness(app_data["file_path"])

    color_map = {
        "Fresh": "green",
        "Not Fresh": "orange",
        "Old": "saddlebrown"
    }

    result_box.config(
        text=f"{result}",
        bg=color_map.get(result, "#f0f0f0"),
        fg="white"
    )

# ---------- Upload Button Function ----------
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        file_name = os.path.basename(file_path)
        file_label.config(text=file_name)

        img = Image.open(file_path)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

        app_data["file_path"] = file_path

# ---------- Initialize App ----------
app_data = {}

root = tk.Tk()
root.title("Group 7")
root.geometry("800x500")
root.configure(bg='white')

# ---------- Title ----------
title = tk.Label(root, text="Tilapia Freshness Detection Tool", font=("Helvetica", 20, "bold"), fg="#0873ff", bg="white")
title.pack(pady=20)

# ---------- Main Frame ----------
main_frame = tk.Frame(root, bg="white")
main_frame.pack(pady=10)

# ---------- Upload Frame ----------
upload_frame = tk.Frame(main_frame, bg="#f5f5f5", padx=20, pady=20)
upload_frame.grid(row=0, column=0, padx=20)

upload_label = tk.Label(upload_frame, text="Upload Tilapia Image", font=("Helvetica", 14, "bold"), bg="#f5f5f5")
upload_label.pack(pady=10)

file_label = tk.Label(upload_frame, text="No file chosen", bg="#f5f5f5", font=("Helvetica", 10))
file_label.pack()

upload_button = tk.Button(upload_frame, text="Choose File", command=upload_file)
upload_button.pack(pady=5)

analyze_button = tk.Button(upload_frame, text="Analyze", bg="dodgerblue", fg="white", font=("Helvetica", 12), command=analyze_image)
analyze_button.pack(pady=10)

image_label = tk.Label(upload_frame, bg="#f5f5f5")
image_label.pack(pady=10)

# ---------- Result Frame ----------
result_frame = tk.Frame(main_frame, bg="white", padx=20, pady=20)
result_frame.grid(row=0, column=1, padx=20, sticky="n") 

result_title = tk.Label(result_frame, text="Result", font=("Helvetica", 14, "bold"), bg="white")
result_title.pack(pady=(10, 10))

# Fixed-size result box
result_box = tk.Label(
    result_frame,
    text="",
    font=("Helvetica", 14, "bold"),
    width=30,
    height=2,
    bg="#f0f0f0",
    fg="black",
    relief="solid",
    bd=1
)
result_box.pack(pady=10)


# ---------- Start GUI ----------
root.mainloop()
