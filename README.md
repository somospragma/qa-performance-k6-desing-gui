<h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://f.hubspotusercontent20.net/hubfs/2829524/Copia%20de%20LOGOTIPO_original-2.png"></a>
  <br>
  Arquetipo Python GUI graficador de propuestas para Pruebas de Performance
  <br>
</h1>

<h4 align="center">Proyecto base de <a href="https://github.com/karatelabs/karate" target="_blank">Pragma</a>.</h4>


<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Python">
  </a>
  <a href="https://docs.python.org/3/library/tkinter.html">
    <img src="https://img.shields.io/badge/GUI-Tkinter-yellow.svg" alt="Tkinter">
  </a>
  <a href="https://grafana.com/oss/k6/">
    <img src="https://img.shields.io/badge/Performance%20Testing-k6-gray.svg" alt="k6">
  </a>
</p>

El siguiente proyecto es una herramienta visual para graficar y diseñar propuestas de pruebas de Performance realizada en Python-Tkinter, también proporciona el script base del stage correspondiente a la gráfica generada para Grafana K6.

<p align="center">
  <a href="#topicos">Topicos</a> •
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#features">Features</a> •
  <a href="#estructura-de-proyecto">Estructura de proyecto</a> •
  <a href="#ejecución-local">Ejecución local</a> •
  <a href="#uso-de-funcionalidades">Uso de funcionalidades</a> •
  <a href="#autores">Autores</a> •
  <a href="#relacionados">Relacionados</a> •
  <a href="#roadmap">Roadmap</a>
</p>


## Topicos

* Python
* Tkinter
* matplotlib

## Tecnologias
### This project required:
- [Python] last version
- [Tkinter] last version
- [matplotlib] last version

Nota: 
*   Para Windows la instalación oficial de Python ya incluye Tkinter por defecto. No se instala con pip ni con un comando adicional, ya que viene integrado con Python.
*   Para MacOS/

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
pip install -r requirements.txt
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
* Botón cerrar: Cierra la aplicación de forma correcta, internamente detiene el proceso.



## Autores

| [<img src="https://gitlab.com/uploads/-/system/user/avatar/25199087/avatar.png?width=800" width=115><br><sub>Laura María Granados García</sub>](https://gitlab.com/laura.granados) <br/> |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |


## Relacionados

- [qa-performance-grafanak6](https://github.com/somospragma/qa-performance-grafanak6)


## Roadmap

- [Guia QA](https://github.com/orgs/somospragma/repositories?q=qa) - (En construcción) Una guia de proyectos Orientados a la Calidad de Software

