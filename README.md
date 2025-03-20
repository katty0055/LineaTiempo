# LineaTiempo
#Para clonar este proyecto utilizasndo VSCode (Windows):
#*Abrir una ventana de VSCode
#*Seleccionar "Clonar el repositorio Git"
#*Pegamos el siguiente enlace "https://github.com/katty0055/LineaTiempo.git" en la caja de texto y presionamos enter
*Indicamos la carpeta en donde se va a guardar nuestro proyecto
*Abrimos en la ventana
*En la barra de navegacion seleccionamos los tres puntos que estan a lado de "Ir", luego terminal, nuevo terminal
*Desde powerShell
*Instalamos python si no lo tenemos
*Creamos un entorno virtual con el comando 
  python -m venv venv
*Activamos el entorno con los comandos
  cd venv\Scripts\
  .\activate.bat
*Volvemos a la carpeta raiz
  cd ..
  cd..
  cd .\LineaTiempo\
* Instalamos las dependencias
    pip install -r requirements.txt
*Configurar el archivo .env
*Realizamos las migraciones
  python manage.py makemigrations
  python manage.py migrate
*Creamos el superusuario
  python manage.py createsuperuser
*Ejecutamos el servidor en nuestro local

