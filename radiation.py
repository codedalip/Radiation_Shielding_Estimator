import tkinter as tk
from tkinter import ttk, messagebox
import math

# 📌 Attenuation coefficients (μ in cm^-1)
attenuation_data = {
    "Aluminum": 0.17,
    "Lead": 1.24,
    "Water": 0.095,
    "Polyethylene": 0.09,
    "Titanium": 0.24,
    "Concrete": 0.12
}

def calculate():
    try:
        material = material_var.get()
        thickness = float(entry_thickness.get())
        i0 = float(entry_i0.get())

        mu = attenuation_data[material]
        transmitted_intensity = i0 * math.exp(-mu * thickness)
        transmission_percent = (transmitted_intensity / i0) * 100
        dose_reduction = 100 - transmission_percent

        result_text.set(f"Transmitted Radiation: {transmission_percent:.2f}%\nDose Reduction: {dose_reduction:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for thickness and intensity.")

# 🧱 GUI Layout
root = tk.Tk()
root.title("Radiation Shielding Estimator")

tk.Label(root, text="Select Material:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
material_var = tk.StringVar(value="Aluminum")
material_menu = ttk.Combobox(root, textvariable=material_var, values=list(attenuation_data.keys()), state="readonly")
material_menu.grid(row=0, column=1, padx=10)

tk.Label(root, text="Thickness (cm):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_thickness = tk.Entry(root)
entry_thickness.grid(row=1, column=1, padx=10)

tk.Label(root, text="Initial Intensity (I₀):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_i0 = tk.Entry(root)
entry_i0.grid(row=2, column=1, padx=10)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=15)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, fg="blue", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
