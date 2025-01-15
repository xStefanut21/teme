import customtkinter as ctk

# Configurare stil global
ctk.set_appearance_mode("dark")  # Mod întunecat (poate fi "light" sau "system")
ctk.set_default_color_theme("green")  # Temă coloristică (poți schimba în "green" sau "dark-blue")

# Funcția de conversie
def convert_units():
    try:
        if not listbox_from.get() or not listbox_to.get():
            result_var.set("Selectează unitățile!")
            return

        from_unit = listbox_from.get()
        to_unit = listbox_to.get()
        
        try:
            value = float(value_entry.get())
        except ValueError:
            result_var.set("Valoare invalidă!")
            return

        conversion_factors = {
            "mg": 1,
            "cg": 10,
            "dg": 100,
            "g": 1000,
            "dag": 10000,
            "hg": 100000,
            "kg": 1000000,
            "t": 1000000000
        }

        if from_unit in conversion_factors and to_unit in conversion_factors:
            result = value * conversion_factors[from_unit] / conversion_factors[to_unit]

            # Ajustăm afișarea rezultatului
            if result < 0.0001:  # Pentru valori foarte mici, afișăm până la 10 zecimale
                result_var.set(f"{result:.10f}")
            else:
                result_var.set(f"{result:.4f}")
        else:
            result_var.set("Conversie nerecunoscută!")
    except Exception as e:
        result_var.set(f"Eroare: {str(e)}")

# Configurare fereastră principală
app = ctk.CTk()
app.title("Convertor de Greutăți")
app.geometry("800x600")

# Etichete și câmpuri
title_label = ctk.CTkLabel(app, text="Convertor de Greutăți", font=("Roboto", 24, "bold"))
title_label.pack(pady=20)

value_label = ctk.CTkLabel(app, text="Introduceți valoarea:", font=("Roboto", 14))
value_label.pack(pady=5)
value_entry = ctk.CTkEntry(app, placeholder_text="Ex: 1000", font=("Roboto", 14), width=300)
value_entry.pack(pady=5)

from_label = ctk.CTkLabel(app, text="Selectați unitatea de plecare:", font=("Roboto", 14))
from_label.pack(pady=5)
listbox_from = ctk.CTkOptionMenu(app, values=["mg", "cg", "dg", "g", "dag", "hg", "kg", "t"])
listbox_from.pack(pady=5)

to_label = ctk.CTkLabel(app, text="Selectați unitatea de destinație:", font=("Roboto", 14))
to_label.pack(pady=5)
listbox_to = ctk.CTkOptionMenu(app, values=["mg", "cg", "dg", "g", "dag", "hg", "kg", "t"])
listbox_to.pack(pady=5)

convert_button = ctk.CTkButton(app, text="Convertește", command=convert_units, font=("Roboto", 14))
convert_button.pack(pady=20)

# Rezultatul
result_var = ctk.StringVar()
result_label = ctk.CTkLabel(app, text="Rezultat:", font=("Roboto", 14))
result_label.pack(pady=5)
result_display = ctk.CTkLabel(app, textvariable=result_var, font=("Roboto", 18, "bold"), width=300, height=50, corner_radius=10, fg_color="pink")
result_display.pack(pady=10)

# Footer
footer_label = ctk.CTkLabel(app, text="Design by Ștefan and Abidzuk", font=("Roboto", 12), text_color="grey")
footer_label.pack(side="bottom", pady=10)

# Rulează aplicația
app.mainloop()
