from pyscript import document

# Symbol: (Element Name, Atomic Number, Atomic Mass)
non_metals = {
    "H":  ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C":  ("Carbon", 6, 12.011),
    "N":  ("Nitrogen", 7, 14.007),
    "O":  ("Oxygen", 8, 15.999),
    "F":  ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P":  ("Phosphorus", 15, 30.974),
    "S":  ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I":  ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222.0),
}


def element_checker(event):
    result_div = document.getElementById("result")
    symbol = document.getElementById("element_name").value.strip().title()

    if symbol == "":
        result_div.innerHTML = "<span class='text-warning fw-bold'>Please enter a symbol.</span>"
        return

    if symbol in non_metals:
        name, number, mass = non_metals[symbol]
        result_div.innerHTML = f"""
        <b>Element Symbol:</b> {symbol}<br>
        <b>Element Name:</b> {name}<br>
        <b>Atomic Number:</b> {number}<br>
        <b>Atomic Mass:</b> {mass}
        """
    else:
        result_div.innerHTML = f"""
        <span class="text-danger fw-bold">
        The element "{symbol}" does not exist in the non-metals list.
        </span>
        """