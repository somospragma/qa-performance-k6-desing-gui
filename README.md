# Arquetipo Python GUI graficador de propuestas para Pruebas de Performance

![Python](https://img.shields.io/badge/python-3.12.5-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?logo=python&logoColor=white)

## Features

- GUI Graficador de stages propuestos
  - Pruebas pico + Generación stage para k6
  - Pruebas de carga + Generación stage para k6

## Estructura de proyecto
````
qa-performance-k6-design-gui
 ┣ README.md
 ┣ requirements.txt (Script para pruebas de escenario POST)
 ┗ graficador.py (Contiene los stages que son llamados desde los script de pruebas)
````

## Ejecución local
### Requisitos previos
* Ambiente virtual (Opcional)
* Instalación de librerías (Archivo de requisitos)

### Comandos de instalación
* Clonar el proyecto

```bash
  git clone https://github.com/somospragma/qa-performance-k6-desing-gui
```

* Ir al directorio del proyecto

```bash
  cd qa-performance-k6-design-gui
```
* Entorno virtual (Opcional)
  * Creación del entorno virtual `python -m venv enviroment-name`
  * Activar el entorno virtual
    * Windows: `enviroment-name/Scripts/activate`
    * MacOS: `source enviroment-name/bin/activate`

* Instalación Tkinter para Python
Para Windows la instalación oficial de Python ya incluye Tkinter por defecto. No se instala con pip ni con un comando adicional, ya que viene integrado con Python. Para instalación en MacOS
```
brew install python-tk 
```

* Instalación de librerías en el equipo (o en el entorno virtual)
```
`pip install -r requirements.txt`
```

### Ejecución
```
python graficador.py
```

> [!WARNING]
> Durante la ejecución de la aplicación, la **terminal usada queda 'ocupada'** mientras la interfaz de usuario de Tkinter está en funcionamiento.  
> En algunos casos, si **no** se cierra el graficador utilizando el botón diseñado para detener el hilo correctamente, el proceso seguirá en ejecución en segundo plano, y la terminal permanecerá bloqueada. En ese caso, será necesario **finalizar manualmente el proceso** desde el Administrador de Tareas (Windows) o con `kill` en la terminal (Linux/Mac).

### Uso de funcionalidades
Una vez iniciada la aplicación, se puede elegir entre dos opciones, pruebas de carga y pruebas pico.
* Pruebas de carga: Se puede elegir el número de rampas con las que se necesite la gráfica, a medida que se va seleccionando alguna de las opciones disponibles, van apareciendo más parámetros de entrada configurables según lo deseado.
* Pruebas pico: Los parámetros de entrada que aparecen en pantalla son referentes a la caracteristicas del pico que se requiera y el número de estos.
* Botón graficar: Cuando se utiliza esta opción, se mostrará la gráfica en pantalla según la prueba elegida en ese momento y parámetros ingresados, además en la parte derecha de la gráfica se mostrará el **script correspondiente al Stage que se plantea en Grafana K6**.
* Botóm cerrar: Cierra la aplicación de forma correcta, internamente detiene el proceso.



## Autores

| [<img src="https://gitlab.com/uploads/-/system/user/avatar/25199087/avatar.png?width=800" width=115><br><sub>Laura María Granados García</sub>](https://gitlab.com/laura.granados) <br/> |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |