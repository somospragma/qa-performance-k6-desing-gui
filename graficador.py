import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

global entry_r1, entry_r2, entry_r3, entry_cte1, entry_cte2, entry_cte, entry_cte1_val, entry_cte2_val, entry_cte_val
global radio1, radio2, radio3
global seleccion_anterior
global entry_ri, entry_ri_val, entry_rf, entry_n_picos, entry_ri_pico, entry_pico_val, entry_t_pico, entry_rf_pico


radio1 = None
radio2 = None
radio3 = None

entry_r1 = None
entry_r2 = None
entry_r3 = None

entry_cte1 = None
entry_cte2 = None
entry_cte = None

entry_cte1_val = None
entry_cte2_val = None
entry_cte_val = None

def generar_script_k6_carga(datos_script):
    encabezado = "// STAGE PARA K6 \nstages = [\n"
    pie = "];"

    tiempo = datos_script[0]
    valores = datos_script[1]

    cuerpo = ""
    c = 0
    i_v = 0

    for i in range(0,len(tiempo)):
        if c == 2:
            c = 0
            i_v+=1
        cuerpo+= f"{{ duration: '{tiempo[i]}s', target: {valores[i_v]}}},\n"
        c+=1
    c = 0
    i_v = len(valores)-2
    for i in range(len(tiempo)-2,0,-1):
        if c == 2:
            c = 0
            i_v-=1
        cuerpo+= f"{{ duration: '{tiempo[i]}s', target: {valores[i_v]}}},\n"
        c+=1

    cuerpo+= f"{{ duration: '{tiempo[0]}s', target: 0}}\n"
    return encabezado+cuerpo+pie

def generar_script_k6_pico(datos_script):
    tiempo = datos_script[0]
    valores = datos_script[1]
    n_picos = datos_script[2]

    encabezado = "// STAGE PARA K6 \nstages = [\n" + \
                f"{{ duration: '{tiempo[0]}', target: {valores[0]} }},\n" + \
                f"{{ duration: '{tiempo[1]}', target: {valores[0]} }},\n"
    pie = f"{{ duration: '{tiempo[1]}', target: 0 }}"+"\n];"

    cuerpo = f"{{ duration: '{tiempo[2]}', target: {valores[1]} }},\n" + \
            f"{{ duration: '{tiempo[3]}', target: {valores[1]} }},\n" + \
            f"{{ duration: '{tiempo[4]}', target: {valores[0]} }},\n"

    return encabezado+cuerpo*n_picos[0]+pie

def on_selection_change(*args):
    global seleccion_anterior
    global radio1, radio2, radio3
    global entry_ri, entry_ri_val, entry_rf, entry_n_picos, entry_ri_pico, entry_pico_val, entry_t_pico, entry_rf_pico

    selected_value = equation_var.get() 

    if selected_value == "Prueba pico" and seleccion_anterior != "Prueba pico":
        for widget in frame_inputs.winfo_children():
            widget.destroy()
        for widget in frame_rampas.winfo_children():
            widget.destroy()

        # Rampa inicial y final
        ttk.Label(frame_inputs, text="Duración rampa inicial (seg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_ri = ttk.Entry(frame_inputs,width=5)
        entry_ri.insert(0, "30")  # Valor por defecto
        entry_ri.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Valor constante entre picos
        ttk.Label(frame_inputs, text="Valor cte entre picos (seg):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        entry_ri_val = ttk.Entry(frame_inputs,width=5)
        entry_ri_val.insert(0, "30")  # Valor por defecto
        entry_ri_val.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Tiempo entre picos
        ttk.Label(frame_inputs, text="Duración entre picos (seg):").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        entry_rf = ttk.Entry(frame_inputs,width=5)
        entry_rf.insert(0, "30")  # Valor por defecto
        entry_rf.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        # Definir el número de picos
        ttk.Label(frame_inputs, text="Número de picos:").grid(row=0, column=6, padx=5, pady=5, sticky="e")
        entry_n_picos = ttk.Entry(frame_inputs,width=5)
        entry_n_picos.insert(0, "3")  # Valor por defecto
        entry_n_picos.grid(row=0, column=7, padx=5, pady=5, sticky="w")

        # Datos de definición del pico como tal
        ttk.Label(frame_inputs, text="Duración rampa subida pico (seg):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_ri_pico = ttk.Entry(frame_inputs,width=5)
        entry_ri_pico.insert(0, "30")  # Valor por defecto
        entry_ri_pico.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Valor máximo pico:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        entry_pico_val = ttk.Entry(frame_inputs,width=5)
        entry_pico_val.insert(0, "80")  # Valor por defecto
        entry_pico_val.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración pico:").grid(row=1, column=4, padx=5, pady=5, sticky="e")
        entry_t_pico = ttk.Entry(frame_inputs,width=5)
        entry_t_pico.insert(0, "30")  # Valor por defecto
        entry_t_pico.grid(row=1, column=5, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración rampa bajada pico (seg):").grid(row=1, column=6, padx=5, pady=5, sticky="e")
        entry_rf_pico = ttk.Entry(frame_inputs,width=5)
        entry_rf_pico.insert(0, "30")  # Valor por defecto
        entry_rf_pico.grid(row=1, column=7, padx=5, pady=5, sticky="w")

        seleccion_anterior = "Prueba pico"

    elif selected_value == "Prueba de carga" and seleccion_anterior != "Prueba de carga":
        for widget in frame_inputs.winfo_children():
            widget.destroy()
        for widget in frame_rampas.winfo_children():
            widget.destroy()

        variable.set(1)  # El valor por defecto es 1

        # Radio Buttons
        ttk.Label(frame_rampas, text="Número de rampas:").grid(row=1, column=0, padx=1, pady=1)
        radio1 = tk.Radiobutton(frame_rampas, text="1", variable=variable, value=1, command=actualizar_vista)
        radio2 = tk.Radiobutton(frame_rampas, text="2", variable=variable, value=2, command=actualizar_vista)
        radio3 = tk.Radiobutton(frame_rampas, text="3", variable=variable, value=3, command=actualizar_vista)

        radio1.grid(row=1, column=1, sticky="w", padx=1, pady=1)
        radio2.grid(row=1, column=2, sticky="w", padx=1, pady=1)
        radio3.grid(row=1, column=3, sticky="w", padx=1, pady=1)

        # Rampa 1
        ttk.Label(frame_inputs, text="Duración rampa 1 (seg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_r1 = ttk.Entry(frame_inputs,width=5)
        entry_r1.insert(0, "30")  # Valor por defecto
        entry_r1.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Valor carga final (request/s):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        entry_cte_val = ttk.Entry(frame_inputs,width=5)
        entry_cte_val.insert(0, "200")  # Valor por defecto
        entry_cte_val.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración carga final (seg):").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        entry_cte = ttk.Entry(frame_inputs,width=5)
        entry_cte.insert(0, "300")  # Valor por defecto
        entry_cte.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        seleccion_anterior = "Prueba de carga"
    else:
        pass

def close_app():
    root.quit()  # Detiene el bucle mainloop
    root.destroy()  # Cierra la ventana

def update_time(x):
    x_new = []
    count = 0
    for value in x:
        count+=value
        x_new.append(count)
    return x_new

def update_graph(tiempo_total,valores_total,datos_script):
    # Tipo de prueba para el título
    selected_equation = equation_var.get()

    # Calcular el área bajo la curva, es decir las peticiones totales
    area_bajo_la_curva = np.trapezoid(valores_total, tiempo_total)

    # Limpia la gráfica anterior
    ax.clear()

    # Se grafica y se agregan detalles
    ax.plot(tiempo_total, valores_total, label="Peticiones por segundo")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_title(f"{selected_equation} - {max(valores_total)} peticiones por segundo")

    # Mostrar el total de peticiones en la gráfica
    plt.text(1, 1, "#Peticiones esperadas: {:,.0f}".format(area_bajo_la_curva).replace(",","."), fontsize=10, color='red',weight='bold')

    # Borrar lo que había en el cuadro de texto y colocar el nuevo script de stage para k6
    text_box.delete("1.0", tk.END)

    if (len(datos_script[1])==2 and len(datos_script[0])>4):
        text_box.insert("1.0", generar_script_k6_pico(datos_script))
    else:
        text_box.insert("1.0", generar_script_k6_carga(datos_script))

    # Actualiza la gráfica
    canvas.draw()
    error_label.config(text="")  # Limpiar errores

def plot_graph():
    global entry_r1, entry_r2, entry_r3, entry_cte1, entry_cte2, entry_cte, entry_cte1_val, entry_cte2_val, entry_cte_val
    global entry_ri, entry_ri_val, entry_rf, entry_n_picos, entry_ri_pico, entry_pico_val, entry_t_pico, entry_rf_pico
    seleccion = variable.get()

    selected_value = equation_var.get()
    if selected_value == "Prueba pico":
        t_ri=int(entry_ri.get())            # Tiempo rampa inicial
        ri_val=int(entry_ri_val.get())      # Valor entre picos
        t_rf=int(entry_rf.get())            # Tiempo entre picos
        n_picos=int(entry_n_picos.get())    # Número de picos

        t_ri_pico=int(entry_ri_pico.get())  # Tiempo rampa inicial inicial pico
        pico_val=int(entry_pico_val.get())  # Valor máximo pico
        t_pico=int(entry_t_pico.get())      # Tiempo duración del pico
        t_rf_pico=int(entry_rf_pico.get())  # Tiempo rampa final pico

        t = update_time([0,t_ri,t_rf] + [t_ri_pico,t_pico,t_rf_pico,t_rf]*n_picos + [t_ri])
        y = [0,ri_val,ri_val] + [pico_val,pico_val,ri_val,ri_val]*n_picos + [0]

        # Se organizan datos para generación de script de stages para k6
        datos_script = [[t_ri, t_rf]+[t_ri_pico,t_pico,t_rf_pico], [ri_val,pico_val], [n_picos]]

        # Graficar e imprimir script
        update_graph(t,y,datos_script)

    elif selected_value == "Prueba de carga":
        if seleccion == 1:
            try:
                # Variables del usuario para graficar
                t_subida1=int(entry_r1.get())
                t_cte=int(entry_cte.get())
                r3=int(entry_cte_val.get())

                # Datos para la gráfica
                tiempo_total = update_time([0,t_subida1,t_cte,t_subida1])
                valores_total = [0,r3,r3,0]

                # Se organizan datos para generación de script de stages para k6
                datos_script = [[t_subida1, t_cte], [r3]]

                # Graficar e imprimir script
                update_graph(tiempo_total,valores_total,datos_script)
            except ValueError:
                error_label.config(text="Por favor, ingresa valores numéricos válidos.")
            except Exception as e:
                error_label.config(text=f"Error: {str(e)}")
        elif seleccion == 2:
            try:
                # Variables del usuario para graficar
                t_subida1=int(entry_r1.get())
                t_subida2=int(entry_r2.get())

                t_cte1=int(entry_cte1.get())
                t_cte=int(entry_cte.get())

                r1=int(entry_cte1_val.get())
                r3=int(entry_cte_val.get())

                # Datos para la gráfica
                tiempo_total = update_time([0,t_subida1,t_cte1,t_subida2,t_cte,t_subida2,t_cte1,t_subida1])
                valores_total = [0,r1,r1,r3,r3,r1,r1,0]

                # Se organizan datos para generación de script de stages para k6
                datos_script = [[t_subida1, t_subida2, t_cte1, t_cte], [r1, r3]]

                # Graficar e imprimir script
                update_graph(tiempo_total,valores_total,datos_script)
            except ValueError as e:
                error_label.config(text="Por favor, ingresa valores numéricos válidos.")
            except Exception as e:
                error_label.config(text=f"Error: {str(e)}")
        else:
            try:
                # Variables del usuario para graficar
                t_subida1=int(entry_r1.get())
                t_subida2=int(entry_r2.get())
                t_subida3=int(entry_r3.get())

                t_cte1=int(entry_cte1.get())
                t_cte2=int(entry_cte2.get())
                t_cte=int(entry_cte.get())

                r1=int(entry_cte1_val.get())
                r2=int(entry_cte2_val.get())
                r3=int(entry_cte_val.get())

                # Datos para la gráfica
                tiempo_total = update_time([0,t_subida1,t_cte1,t_subida2,t_cte2,
                                            t_subida3,t_cte,t_subida3,
                                            t_cte2,t_subida2,t_cte1,t_subida1])
                valores_total = [0,r1,r1,r2,r2,r3,r3,r2,r2,r1,r1,0]

                # Se organizan datos para generación de script de stages para k6
                datos_script = [[t_subida1, t_subida2, t_subida3, t_cte1, t_cte2, t_cte], [r1, r2, r3]]

                # Graficar e imprimir script
                update_graph(tiempo_total,valores_total,datos_script)
            except ValueError:
                error_label.config(text="Por favor, ingresa valores numéricos válidos.")
            except Exception as e:
                error_label.config(text=f"Error: {str(e)}")
    else:
        pass


def actualizar_vista():
    global entry_r1, entry_r2, entry_r3, entry_cte1, entry_cte2, entry_cte, entry_cte1_val, entry_cte2_val, entry_cte_val

    seleccion = variable.get()

    for widget in frame_inputs.winfo_children():
        widget.destroy()

    if seleccion == 1:
        # Rampa 1
        ttk.Label(frame_inputs, text="Duración rampa 1 (seg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_r1 = ttk.Entry(frame_inputs,width=5)
        entry_r1.insert(0, "30")  # Valor por defecto
        entry_r1.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Valor carga final (request/s):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        entry_cte_val = ttk.Entry(frame_inputs,width=5)
        entry_cte_val.insert(0, "200")  # Valor por defecto
        entry_cte_val.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración carga final (seg):").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        entry_cte = ttk.Entry(frame_inputs,width=5)
        entry_cte.insert(0, "300")  # Valor por defecto
        entry_cte.grid(row=0, column=5, padx=5, pady=5, sticky="w")
    elif seleccion == 2:
        # Rampa 1
        ttk.Label(frame_inputs, text="Duración rampa 1 (seg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_r1 = ttk.Entry(frame_inputs,width=5)
        entry_r1.insert(0, "30")  # Valor por defecto
        entry_r1.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Valor cte 1 (request/s):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        entry_cte1_val = ttk.Entry(frame_inputs,width=5)
        entry_cte1_val.insert(0, "50")  # Valor por defecto
        entry_cte1_val.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración cte 1 (seg):").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        entry_cte1 = ttk.Entry(frame_inputs,width=5)
        entry_cte1.insert(0, "30")  # Valor por defecto
        entry_cte1.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        # Rampa 2
        ttk.Label(frame_inputs, text="Duración rampa 2 (seg):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_r2 = ttk.Entry(frame_inputs,width=5)
        entry_r2.insert(0, "30")  # Valor por defecto
        entry_r2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Rampa 3
        ttk.Label(frame_inputs, text="Valor carga final (request/s):").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        entry_cte_val = ttk.Entry(frame_inputs,width=5)
        entry_cte_val.insert(0, "200")  # Valor por defecto
        entry_cte_val.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración carga final (seg):").grid(row=1, column=4, padx=5, pady=5, sticky="e")
        entry_cte = ttk.Entry(frame_inputs,width=5)
        entry_cte.insert(0, "300")  # Valor por defecto
        entry_cte.grid(row=1, column=5, padx=5, pady=5, sticky="w")
    else:
        # Rampa 1
        ttk.Label(frame_inputs, text="Duración rampa 1 (seg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_r1 = ttk.Entry(frame_inputs,width=5)
        entry_r1.insert(0, "30")  # Valor por defecto
        entry_r1.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Valor cte 1 (request/s):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        entry_cte1_val = ttk.Entry(frame_inputs,width=5)
        entry_cte1_val.insert(0, "50")  # Valor por defecto
        entry_cte1_val.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración cte 1 (seg):").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        entry_cte1 = ttk.Entry(frame_inputs,width=5)
        entry_cte1.insert(0, "30")  # Valor por defecto
        entry_cte1.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        # Rampa 2
        ttk.Label(frame_inputs, text="Duración rampa 2 (seg):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_r2 = ttk.Entry(frame_inputs,width=5)
        entry_r2.insert(0, "30")  # Valor por defecto
        entry_r2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Valor cte 2 (request/s):").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        entry_cte2_val = ttk.Entry(frame_inputs,width=5)
        entry_cte2_val.insert(0, "80")  # Valor por defecto
        entry_cte2_val.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración cte 2 (seg):").grid(row=1, column=4, padx=5, pady=5, sticky="e")
        entry_cte2 = ttk.Entry(frame_inputs,width=5)
        entry_cte2.insert(0, "30")  # Valor por defecto
        entry_cte2.grid(row=1, column=5, padx=5, pady=5, sticky="w")

        # Rampa 3
        ttk.Label(frame_inputs, text="Duración rampa 3 (seg):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_r3 = ttk.Entry(frame_inputs,width=5)
        entry_r3.insert(0, "30")  # Valor por defecto
        entry_r3.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Valor carga final (request/s):").grid(row=2, column=2, padx=5, pady=5, sticky="e")
        entry_cte_val = ttk.Entry(frame_inputs,width=5)
        entry_cte_val.insert(0, "200")  # Valor por defecto
        entry_cte_val.grid(row=2, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_inputs, text="Duración carga final (seg):").grid(row=2, column=4, padx=5, pady=5, sticky="e")
        entry_cte = ttk.Entry(frame_inputs,width=5)
        entry_cte.insert(0, "300")  # Valor por defecto
        entry_cte.grid(row=2, column=5, padx=5, pady=5, sticky="w")

# Ventana principal
root = tk.Tk()
root.title("Graficador de propuestas pruebas Performance")

# Para la distribución de los elementos de la ventana
root.rowconfigure(0, weight=0)  # frame_selection
root.rowconfigure(1, weight=0)  # frame_rampas
root.rowconfigure(2, weight=0)  # frame_inputs
root.rowconfigure(3, weight=1)  # frame_main grafica
root.columnconfigure(0, weight=1)

# Frame de las opciones de tipo de prueba
frame_selection = ttk.Frame(root, padding=10, relief="ridge", borderwidth=2)
frame_selection.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Label de la lista desplegable y ubicación
ttk.Label(frame_selection, text="Selecciona el tipo de prueba:").grid(row=0, column=0, padx=5, pady=5)

# Valor por defecto de la lista desplegable
seleccion_anterior = "Prueba de carga"
equation_var = tk.StringVar(value="Prueba de carga")

# Lista desplegable con los tipos de prueba
equation_menu = ttk.Combobox(frame_selection, textvariable=equation_var,
                            values=["Prueba de carga", "Prueba pico"], state="readonly")

# Ubicación de la lista desplegable
equation_menu.grid(row=0, column=1, padx=5, pady=5)

# Asociar un evento al cambio de valor
equation_var.trace_add("write", on_selection_change)

# Botón para graficar
btn_plot = ttk.Button(frame_selection, text="Graficar", command=plot_graph)
btn_plot.grid(row=0, column=2, padx=5, pady=5)

# Botón para cerrar la aplicación
close_button = tk.Button(frame_selection, text="Cerrar", command=close_app)
close_button.grid(row=0, column=15, padx=5, pady=5)

# Frame donde va el numero de rampas
frame_rampas = ttk.Frame(root, padding=2, relief="ridge", borderwidth=2)
frame_rampas.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Frame donde van los elementos de la prueba pico
frame_pico = ttk.Frame(root, padding=10, relief="ridge", borderwidth=2)
frame_pico.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
frame_pico.columnconfigure(0, weight=1)
frame_pico.columnconfigure(1, weight=1)
frame_pico.columnconfigure(2, weight=1)
frame_pico.columnconfigure(3, weight=1)
frame_pico.columnconfigure(4, weight=1)
frame_pico.columnconfigure(5, weight=1)
frame_pico.columnconfigure(6, weight=1)
frame_pico.columnconfigure(7, weight=1)

# Radio button
variable = tk.IntVar(value=1)  # El valor por defecto es 1

ttk.Label(frame_rampas, text="Número de rampas:").grid(row=1, column=0, padx=1, pady=1, sticky="n")
radio1 = tk.Radiobutton(frame_rampas, text="1", variable=variable, value=1, command=actualizar_vista)
radio2 = tk.Radiobutton(frame_rampas, text="2", variable=variable, value=2, command=actualizar_vista)
radio3 = tk.Radiobutton(frame_rampas, text="3", variable=variable, value=3, command=actualizar_vista)

radio1.grid(row=1, column=1, sticky="w", padx=1, pady=1)
radio2.grid(row=1, column=2, sticky="w", padx=1, pady=1)
radio3.grid(row=1, column=3, sticky="w", padx=1, pady=1)

# Obtener tamaño de la pantalla
screen_width = root.winfo_screenwidth()
root.geometry(f"{screen_width}x600") 

# Frame de los input de prueba de carga
frame_inputs = ttk.Frame(root, padding=10, relief="ridge", borderwidth=2)
frame_inputs.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
frame_inputs.columnconfigure(0, weight=1)
frame_inputs.columnconfigure(1, weight=1)
frame_inputs.columnconfigure(2, weight=1)
frame_inputs.columnconfigure(3, weight=1)
frame_inputs.columnconfigure(4, weight=1)
frame_inputs.columnconfigure(5, weight=1)

# Rampa 1
ttk.Label(frame_inputs, text="Duración rampa 1 (seg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_r1 = ttk.Entry(frame_inputs,width=5)
entry_r1.insert(0, "30")  # Valor por defecto
entry_r1.grid(row=0, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frame_inputs, text="Valor carga final (request/s):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_cte_val = ttk.Entry(frame_inputs,width=5)
entry_cte_val.insert(0, "200")  # Valor por defecto
entry_cte_val.grid(row=0, column=3, padx=5, pady=5, sticky="w")

ttk.Label(frame_inputs, text="Duración carga final (seg):").grid(row=0, column=4, padx=5, pady=5, sticky="e")
entry_cte = ttk.Entry(frame_inputs,width=5)
entry_cte.insert(0, "300")  # Valor por defecto
entry_cte.grid(row=0, column=5, padx=5, pady=5, sticky="w")

frame_main = ttk.Frame(root, padding=10, relief="ridge", borderwidth=2)
frame_main.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

# Frame del cuadro de texto de salida script k6
frame_text = tk.Frame(frame_main, width=150, bg="lightgray")  # Frame para texto
frame_text.pack(side="right", fill="y", padx=5, pady=5)

# Texto del script k6
text_box = tk.Text(frame_text, wrap="word", width=45, height=10)
text_box.pack(fill="both", expand=True, padx=5, pady=5)

# Gráfica
fig, ax = plt.subplots(figsize=(10, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_main)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Para los errores
error_label = ttk.Label(frame_main, text="", foreground="red")
error_label.pack(side="bottom", pady=10)

# Loop de la interfaz
root.mainloop()