# CLASIC PINPON

## Descripción
Este es un juego clásico tipo Pong creado con PyGame. Dos jugadores controlan paletas para devolver una pelota y anotar puntos. El primer jugador en llegar a 10 puntos gana el juego.

## Funciones:
- **Juego de 2 jugadores**: Cada jugador controla una paleta para evitar que la pelota pase al otro lado.
- **Ingreso de nombres**: Los jugadores deben ingresar su nombre antes de comenzar el juego.
- **Cuenta regresiva**: Se muestra una cuenta regresiva de 5 a 1 antes de que el juego comience.
- **Pausar y reanudar**: Puedes pausar el juego presionando la tecla `Q` y reanudarlo presionando `Q` nuevamente.
- **Reiniciar juego**: Usa la tecla `P` para reiniciar el juego en cualquier momento.
- **Ganador y perdedor**: El primer jugador en alcanzar 10 puntos es el ganador, y el juego muestra al ganador y al perdedor en pantalla.
- **Pelota con dirección aleatoria**: La pelota cambiará de dirección cada vez que se marque un punto.

## Controles jugador 1 y 2
- **Jugador 1 (Izquierda)**:
  - `W` para mover la paleta hacia arriba.
  - `S` para mover la paleta hacia abajo.
- **Jugador 2 (Derecha)**:
  - `Flecha arriba` para mover la paleta hacia arriba.
  - `Flecha abajo` para mover la paleta hacia abajo.

## Cómo jugar
1. Ejecuta el archivo `pinpon.py`.
2. Ingresa los nombres de los jugadores en la pantalla de inicio.
3. El juego comienza con una cuenta regresiva de 5 a 1.
4. Controla las raquetas para devolver la pelota y ganar puntos.
5. El primer jugador en llegar a 10 puntos gana.
6. Usa la tecla `Q` para pausar el juego y `P` para reiniciarlo en cualquier momento.

## importante
Instalar la libreria PyGame con el siguiente comando:
   ```bash
   pip install pygame
