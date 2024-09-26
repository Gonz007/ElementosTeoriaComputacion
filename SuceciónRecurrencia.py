import tkinter as tk
from tkinter import ttk

def calcular_sucesion_recurrencia(n, a_0, c1, c2, output):
    # Limpiar el contenido del cuadro de texto
    output.delete(1.0, tk.END)
    
    # Inicializamos la lista de sucesiones
    sucesiones = []
    
    # Condición inicial
    sucesiones.append(a_0)
    
    # Mostrar la condición inicial
    output.insert(tk.END, f"a₀ = {a_0}\n")

    # Cálculo de las primeras sucesiones
    for i in range(1, n):
        a_k = c1 * sucesiones[i - 1] + c2
        sucesiones.append(a_k)
        output.insert(tk.END, f"a₍{i}₎ = {c1} * a₍{i-1}₎ + {c2} = {c1} * {sucesiones[i-1]} + {c2} = {a_k}\n")
    
    # Fórmula general antes de simplificar (la estructura es 2^n para c1 = 2)
    output.insert(tk.END, "\nFórmula general antes de simplificar:\n")
    for i in range(n):
        termino_general = f"a₍{i}₎ = {c1}^{i} * {a_0} + {c2} * ({c1}^{i} - 1) / ({c1} - 1)"
        output.insert(tk.END, f"{termino_general}\n")
    
    # Fórmula simplificada (si c1 es una constante específica como 2)
    output.insert(tk.END, "\nFórmula general simplificada (solo para valores conocidos de c1 y c2):\n")
    if c1 == 2:
        for i in range(n):
            termino_simplificado = f"a₍{i}₎ = {(a_0 + c2)} * 2^{i} - {c2}"
            output.insert(tk.END, f"{termino_simplificado}\n")
    else:
        output.insert(tk.END, "No se puede simplificar para el valor actual de c1.\n")

def interfaz():
    # Crear ventana principal
    window = tk.Tk()
    window.title("Sucesiones Recursivas")
    
    # Etiqueta de instrucciones
    label = ttk.Label(window, text="Introduce los parámetros de la sucesión:")
    label.pack(pady=10)

    # Condición inicial
    ttk.Label(window, text="Condición inicial a₀:").pack()
    entrada_a0 = ttk.Entry(window)
    entrada_a0.pack(pady=5)
    
    # Coeficiente c1 (multiplicador de a_{k-1})
    ttk.Label(window, text="Coeficiente c1 (para a_{k-1}):").pack()
    entrada_c1 = ttk.Entry(window)
    entrada_c1.pack(pady=5)
    
    # Constante c2 (término independiente)
    ttk.Label(window, text="Constante c2 (término independiente):").pack()
    entrada_c2 = ttk.Entry(window)
    entrada_c2.pack(pady=5)
    
    # Número de términos
    ttk.Label(window, text="Número de términos:").pack()
    entrada_n = ttk.Entry(window)
    entrada_n.pack(pady=5)

    # Cuadro de texto para mostrar los resultados
    output = tk.Text(window, height=20, width=60)
    output.pack(pady=10)

    # Función de acción del botón
    def ejecutar_calculo():
        n = int(entrada_n.get())
        a_0 = int(entrada_a0.get())
        c1 = int(entrada_c1.get())
        c2 = int(entrada_c2.get())
        calcular_sucesion_recurrencia(n, a_0, c1, c2, output)

    # Botón para calcular la sucesión
    boton = ttk.Button(window, text="Calcular Sucesión", command=ejecutar_calculo)
    boton.pack(pady=5)
    
    # Mostrar ventana
    window.mainloop()

# Iniciar la interfaz
interfaz()