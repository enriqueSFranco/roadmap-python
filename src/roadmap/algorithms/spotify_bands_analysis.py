""" 
OASIS VS LINKIN PARK

EJERCICIO:
Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
¡Dos de las bandas más grandes de la historia están de vuelta!
Desarrolla un programa que se conecte al API de Spotify y los compare.
Requisitos:
1. Crea una cuenta de desarrollo en https://developer.spotify.com.
2. Conéctate al API utilizando tu lenguaje de programación.
3. Recupera datos de los endpoint que tú quieras.
Acciones:
1. Accede a las estadísticas de las dos bandas.
   Por ejemplo: número total de seguidores, escuchas mensuales,
   canción con más reproducciones...
2. Compara los resultados de, por lo menos, 3 endpoint.
3. Muestra todos los resultados por consola para notificar al usuario.
4. Desarrolla un criterio para seleccionar qué banda es más popular.
"""

"""
Endpoint para obtener el token de acceso
   curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"
"""
