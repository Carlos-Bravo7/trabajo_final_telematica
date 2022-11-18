# trabajo_final_telematica
Trabajo final usando contenedores en Ubuntu

Buenos dias profe:
a continuación le voy a decir 2 formas para poder porbar el proyecto:

la primera es:
1-) descarga estos archivos y los guarda en una carpeta que se llame trabajo_final y esta carpeta la coloca en el escritorio

2-) entra a la carpeta desde la terminal y ejecuta el comando sudo python3.10 pagina_principal.py

3-) ya con esto la pagina debe abrir en el localhost:8050 y desde ahí la puede probar

la segunda es:
1-) descarga estos archivos y los guarda en una carpeta que se llame trabajo_final y esta carpeta la coloca en el escritorio

2-) entra a la carpeta desde la terminal y ejecuta el comando sudo docker build . -t trabajo_final

3.) espera a que se cree la imagen la cual va a tener el nombre de trabajo_final 

4-) una ves creada la imagen la corre con el comando sudo docker run -d trabajo final (esta va a correr en el localhost:8050)
  4.1) tambien puede ejecutar el comando sudo docker run -it trabajo final bash lo cual lo va a llevar a dentro de la imagen y ya estando dentro de ella puede correr
       el comando de sudo python3.10 pagina_principal.py
5-) Y ya una ves que entre al localhost desde el navegador lo va a poder ver

Muchas gracias, y espero que tenga un muy buen dia.
