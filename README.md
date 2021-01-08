# PTRestApi

## API Rest en Django para una aplicación de TODO List.

### -Lenguaje
    * Python 3.8.6
### -Framework
    * Django 3.1.3
    * Django rest framework 3.12.3

### Paquetes
    * django-cors-headers

### Instalacion de requisitos:
    pip install -r requirements.txt

### Antes de Probar puede ser necesario usar los siguientes comandos:
    * python3 manage.py makemigrations restApi
    * python3 manage.py migrate

### Para probar la aplicación usar el siguiente comando:
    * python3 manage.py runserver

### Para ver los resultados de la API hacer la consulta a la siguiente dirección http://127.0.0.1:8000/api/

### Para ingresar nuevos datos es necesario enviar por POST datos en formato JSON.

### Para modificar un dato con PUT se usa la siguiente direccion http://127.0.0.1:8000/api/{nombre}/ enviando datos en formato JSON.

# NOTA:
*Debido a los CORS se instaló corsheaders link: https://github.com/adamchainz/django-cors-headers
*Si se instala en el navegador un desactivador de CORS no es necesario este paquete.