# Proyecto de Django Rest Framework para Gestión de transacciones mediante Json

## Descripción del Proyecto

Este proyecto es una aplicación basada en Django Rest Framework que se utiliza para leer datos de un archivo de Excel, que limpia y valida estos datos, 
y luego los envia a varios endpoints de una API a través de solicitudes POST. El archivo de Excel contiene varias hojas, 
cada una de las cuales se corresponde con un tipo de datos específico, como "Transacciones", "Categorías", "Comercios" y "Keywords". 
Cada tipo de datos tiene un conjunto de campos requeridos que deben estar presentes para que los datos sean válidos.

## Principales Componentes del Proyecto

- **Django Rest Framework**: Marco de trabajo utilizado para construir la API.
- **Pandas**: Biblioteca para manipulación y análisis de datos utilizada para leer y limpiar los datos del archivo de Excel.
- **Requests**: Biblioteca para realizar solicitudes HTTP a los endpoints de la API.
- **Poetry**: Poetry resuelve y gestiona automáticamente las dependencias del proyecto
- **locust**:Locust permite simular múltiples usuarios concurrentes enviando solicitudes a una aplicación para evaluar su rendimiento bajo condiciones de carga.
  Su diseño es altamente flexible, facilitando la definición de escenarios de prueba mediante scripts en Python,
  y ofrece una interfaz web intuitiva para monitorizar y controlar las pruebas en tiempo real.

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

1. Clonar el repositorio a tu máquina local usando:
   ```bash
   git clone https://github.com/usuario/repositorio.git


Navega a la carpeta del proyecto con:

bash

cd repositorio

Instala las dependencias necesarias con:

bash

    pip install -r requirements.txt

Uso

Para ejecutar el script principal y cargar los datos desde el archivo de Excel a la API:

    Asegúrate de que el servidor de Django esté corriendo:

    bash

python manage.py runserver

Ejecuta el script principal:

bash

    python retrieve.py

Despliegue

Para desplegar este proyecto en otro sistema, sigue estos pasos:

    Configurar el entorno virtual (opcional pero recomendado):

    bash

python -m venv venv
source venv/bin/activate   # En Windows usa `venv\Scripts\activate`

Instalar las dependencias:

bash

pip install -r requirements.txt

Configurar la base de datos:

    Configura la base de datos en settings.py según tu entorno.
    Aplica las migraciones:

    bash

    python manage.py migrate

Ejecutar el servidor de desarrollo:

bash

    python manage.py runserver

    Configurar las variables de entorno:
        Asegúrate de configurar las variables de entorno necesarias, 
        como las credenciales de la base de datos y la configuración del servidor.

    Probar la aplicación:
        Asegúrate de que todas las rutas y endpoints funcionen correctamente 
        visitando http://127.0.0.1:8000 en tu navegador.

Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

    Haz un fork del repositorio.
    Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
    Haz tus cambios y haz commit de ellos (git commit -m 'Añadir nueva característica').
    Envía tus cambios a tu fork (git push origin feature/nueva-caracteristica).
    Abre un Pull Request en el repositorio original.

Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
Contacto

Para cualquier consulta o sugerencia, puedes contactarnos a través de:

    Email: mariotorreslagos@gmail.com
    GitHub: wottan32
