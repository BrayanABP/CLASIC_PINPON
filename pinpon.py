import pygame
import sys
import random

pygame.init()

ANCHO = 1000
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("CLASIC PINPON")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# reloj controlador de FPS
fps = pygame.time.Clock()

# Variables juego
velocidad_pelota = [5, 5]
puntos_izquierda = 0
puntos_derecha = 0
juego_pausado = False
jugador_izquierda = ""
jugador_derecha = ""

# raquetas y pelota
raqueta_izquierda = pygame.Rect(50, ALTO // 2 - 60, 20, 120)
raqueta_derecha = pygame.Rect(ANCHO - 70, ALTO // 2 - 60, 20, 120)
pelota = pygame.Rect(ANCHO // 2 - 15, ALTO // 2 - 15, 30, 30)

# Función texto
def mostrar_texto(texto, tamaño, x, y, color):
    fuente = pygame.font.Font(None, tamaño)
    superficie_texto = fuente.render(texto, True, color)
    pantalla.blit(superficie_texto, (x, y))

# Función cuenta regresiva
def cuenta_regresiva():
    for i in range(5, 0, -1):
        pantalla.fill(NEGRO)
        mostrar_texto(str(i), 100, ANCHO // 2 - 50, ALTO // 3, BLANCO)
        pygame.display.flip()
        pygame.time.wait(1000)

    pantalla.fill(NEGRO)
    mostrar_texto("¡Ahora!", 100, ANCHO // 2 - 150, ALTO // 3, BLANCO)
    pygame.display.flip()
    pygame.time.wait(1000)

# Función mostrar nombres establecidos
def pantalla_ingreso_nombres():
    global jugador_izquierda, jugador_derecha
    ingresando_nombres = True
    nombre_actual = "Jugador Izquierda"
    texto_entrada = ""
    input_box = pygame.Rect(ANCHO // 4, ALTO // 3, 400, 50)
    color_input_box = (255, 255, 255)

    while ingresando_nombres:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if nombre_actual == "Jugador Izquierda":
                        jugador_izquierda = texto_entrada
                        nombre_actual = "Jugador Derecha"
                        texto_entrada = ""
                    elif nombre_actual == "Jugador Derecha":
                        jugador_derecha = texto_entrada
                        ingresando_nombres = False
                        break
                elif evento.key == pygame.K_BACKSPACE:
                    texto_entrada = texto_entrada[:-1]
                else:
                    texto_entrada += evento.unicode

        pantalla.fill(NEGRO)
        mostrar_texto(f"{nombre_actual}, ingresa tu nombre:", 40, ANCHO // 4, ALTO // 4, BLANCO)
        pygame.draw.rect(pantalla, color_input_box, input_box, 2)
        mostrar_texto(texto_entrada, 30, ANCHO // 4 + 10, ALTO // 3 + 10, BLANCO)
        pygame.display.flip()

# Juego
def juego():
    global puntos_izquierda, puntos_derecha, velocidad_pelota, juego_pausado
    global jugador_izquierda, jugador_derecha

    # Mostrar nombres
    pantalla_ingreso_nombres()

    # cuenta regresiva
    cuenta_regresiva()

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Pausar o reiniciar el juego
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    juego_pausado = not juego_pausado
                if evento.key == pygame.K_p:
                    puntos_izquierda = 0
                    puntos_derecha = 0
                    pelota.x = ANCHO // 2 - 15
                    pelota.y = ALTO // 2 - 15
                    velocidad_pelota = [random.choice([5, -5]), random.choice([5, -5])]
                    # Iniciar cuenta regresiva al presionar P
                    cuenta_regresiva()

        if juego_pausado:
            pantalla.fill(NEGRO)
            mostrar_texto("Juego Pausado", 60, ANCHO // 4, ALTO // 3, BLANCO)
            mostrar_texto("Presiona Q para reanudar", 40, ANCHO // 4, ALTO // 2, BLANCO)
            mostrar_texto("Presiona P para reiniciar", 40, ANCHO // 4, ALTO // 1.6, BLANCO)
            pygame.display.flip()
            continue

        # Movimiento raquetas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and raqueta_izquierda.top > 0:
            raqueta_izquierda.y -= 7
        if teclas[pygame.K_s] and raqueta_izquierda.bottom < ALTO:
            raqueta_izquierda.y += 7
        if teclas[pygame.K_UP] and raqueta_derecha.top > 0:
            raqueta_derecha.y -= 7
        if teclas[pygame.K_DOWN] and raqueta_derecha.bottom < ALTO:
            raqueta_derecha.y += 7

        # Movimiento pelota
        pelota.x += velocidad_pelota[0]
        pelota.y += velocidad_pelota[1]

        # Rebote pelota en la pantalla
        if pelota.top <= 0 or pelota.bottom >= ALTO:
            velocidad_pelota[1] = -velocidad_pelota[1]

        # Rebote en las raquetas
        if pelota.colliderect(raqueta_izquierda) or pelota.colliderect(raqueta_derecha):
            velocidad_pelota[0] = -velocidad_pelota[0]

        # Punto para la derecha
        if pelota.left <= 0:
            puntos_derecha += 1
            pelota.x = ANCHO // 2 - 15
            pelota.y = ALTO // 2 - 15
            velocidad_pelota = [random.choice([5, -5]), random.choice([5, -5])]

        # Punto para la izquierda
        if pelota.right >= ANCHO:
            puntos_izquierda += 1
            pelota.x = ANCHO // 2 - 15
            pelota.y = ALTO // 2 - 15
            velocidad_pelota = [random.choice([5, -5]), random.choice([5, -5])]

        # Verificar ganador
        if puntos_izquierda == 10 or puntos_derecha == 10:
            ganador = jugador_izquierda if puntos_izquierda == 10 else jugador_derecha
            perdedor = jugador_derecha if ganador == jugador_izquierda else jugador_izquierda
            pantalla.fill(NEGRO)
            mostrar_texto(f"¡{ganador} es el ganador!", 60, ANCHO // 4, ALTO // 3, BLANCO)
            mostrar_texto(f"{perdedor} es el perdedor.", 40, ANCHO // 4, ALTO // 2, BLANCO)
            mostrar_texto("Presiona P para reiniciar", 40, ANCHO // 4, ALTO // 1.6, BLANCO)
            pygame.display.flip()
            while True:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_p:
                        puntos_izquierda = 0
                        puntos_derecha = 0
                        pelota.x = ANCHO // 2 - 15
                        pelota.y = ALTO // 2 - 15
                        velocidad_pelota = [random.choice([5, -5]), random.choice([5, -5])]
                        return  # Reiniciar juego principal

        # Mostrar en pantalla
        pantalla.fill(NEGRO)
        # Línea separadora
        pygame.draw.aaline(pantalla, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))
        # Nombres de los jugadores (más abajo para evitar choque con puntos)
        mostrar_texto(jugador_izquierda, 30, 50, 50, BLANCO)
        mostrar_texto(jugador_derecha, 30, ANCHO - 150, 50, BLANCO)
        # Puntos
        mostrar_texto(f"{puntos_izquierda}", 60, ANCHO // 4 - 30, 50, BLANCO)
        mostrar_texto(f"{puntos_derecha}", 60, ANCHO * 3 // 4 - 30, 50, BLANCO)
        # Raquetas y pelota
        pygame.draw.rect(pantalla, BLANCO, raqueta_izquierda)
        pygame.draw.rect(pantalla, BLANCO, raqueta_derecha)
        pygame.draw.ellipse(pantalla, BLANCO, pelota)

        pygame.display.flip()
        fps.tick(60)

juego()
