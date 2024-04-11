import string

jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks, code, and data. JupyterLab is
flexible: configure and arrange the user interface to support a wide
range of workflows in data science, scientific computing, and machine
learning. JupyterLab is extensible and modular: write plugins that add
new components and integrate with existing ones. """

palabras = jupyter_info.lower().split()

c = input("Ingrese un caracter: ")
if(c in string.ascii_letters):
    print(f"Las palabras que contienen \"{c}\" son: ")
    for palabra in palabras: 
        if (c in palabra): print(palabra)
else:
    print("No se ingreso un caracter")

