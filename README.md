# 🐱 Michibook

**Michibook** es una red social para amantes de los gatos.  
Permite registrarse, publicar "maullidos" (pensamientos o mensajes sobre gatos) y reaccionar a los maullidos de otros usuarios.  

Está desarrollada con **Django 5.2**, **Django Channels** y **Daphne**, lo que permite interacción en tiempo real mediante **WebSockets**.

---

## 📋 Requisitos de Instalación

Antes de comenzar, asegúrate de tener instalado en tu sistema:

- **Python 3.10+**
- **Git**

--- 

## ⚙️ Instalación

Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/usuario/michibook.git
cd michibook
```

Crea y activa el entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

Instala los requerimientos:

```bash
pip install -r requirements.txt
```
Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

```bash

SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

```

Aplica las migraciones y crea un superusuario:

```bash
python manage.py migrate

python manage.py createsuperuser

```

## 🚀 Ejecución

Para correr el servidor en desarrollo con Django:

```bash

python manage.py runserver

```

Luego abre http://localhost:8000 en tu navegador.

## 🛠️ Construido con 

* [Django] (https://docs.djangoproject.com/en/5.2/)

* [Django_Channels] (https://channels.readthedocs.io/en/latest/)

* [Daphne] (https://pypi.org/project/daphne/)

* [BootStrap] (https://getbootstrap.com/)

* [Choices] (https://github.com/Choices-js/Choices)

* [Flatpickr] (https://flatpickr.js.org/)

## ✒️ Autor

* **Carlos Cruz** - *Programador y diseñador* - [R2d2cruz] (https://github.com/R2d2cruz)

## 💻 Consideraciones de Diseño

- **Paleta de Colores**:  
  Se utilizó una gama de tonos cálidos y marrones, inspirada en el pelaje de los gatos y en el ambiente acogedor de las cafeterías. Esto le da a la aplicación una apariencia amigable y cómoda para el usuario, evitando colores excesivamente brillantes.

- **Modelo `UserProfile`**:  
  Se creó un modelo adicional al usuario de Django para almacenar información extendida de la cuenta (foto de perfil, biografía, etc.), manteniendo una separación clara entre la autenticación y los datos de perfil.

- **Plantillas HTML Modulares**:  
  Se modularizaron los templates para facilitar la reutilización de código y mantener la coherencia visual en toda la aplicación, reduciendo duplicación y simplificando el mantenimiento.

---

## 📜 Próximas Funcionalidades Planeadas

- **Sistema de Amigos**:  
  Posibilidad de agregar amigos, con una sección dedicada para visualizarlos y ver exclusivamente sus maullidos.

- **Respuestas a Maullidos**:  
  Implementar un sistema de comentarios o respuestas dentro de cada publicación para fomentar la interacción.

- **Etiquetas y Filtros**:  
  Añadir la opción de crear y asignar tags a las publicaciones, permitiendo filtrar el contenido por temas de interés.