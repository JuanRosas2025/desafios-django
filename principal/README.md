Buenas profesor
Este "MD" es para explicar el funcionamiento de las rutas de "miweb"

1° Abrir directamente el servidor lleva a la pagina principal, en la que solo se saluda al usuario
con el mensaje "Hola desde Django"

2° Al usar la ruta "http://127.0.0.1:8000/saludame/(Nombre a preferencia)/"
    mostrara un saludo personalizado dependiedo de que se agrega despues de (saludame)
    Nota: Al ser de tipo String, pueden usarse tanto letras como numeros e incluso espacios

3° Al usar la ruta "http://127.0.0.1:8000/numero/(Numero de preferencia)/"
    mostrara un saludo y el numero seleccionado, esto es porque en urls.py, la variable es cambiada a "int<>" en vez de "str<>" (Los <> van fuera de el comando pero hacerlo lo detecta como comando incluso aqui), al ser un "int" no considera letras o espacios

Todo esto funciona ya que en views.py, estan las "def" de cada uno y son llamadas cada que se hace request

Sin mas que agregar, aviso que quedo atento a cualquier comentario o duda
Espero que tenga buena semana profesor