# coding=utf-8
import pygame, sys
from pygame.locals import *

from AbstractFactory.FabricaElfos import FabricaElfos
from AbstractFactory.FabricaHumanos import FabricaHumanos
from AbstractFactory.FabricaOrcos import FabricaOrcos
from AbstractFactory.FabricaPrincipal import FabricaPrincipal

DIMENSIONES = (650, 500)
COLOR_TEXTO = (243, 255, 0)


def principal():
    pygame.init()
    jugando = True

    ventana = pygame.display.set_mode(DIMENSIONES)
    pygame.display.set_caption("Catálogo de personajes I")

    Fuente = pygame.font.SysFont("Arial", 30)
    LabelRazas = Fuente.render("Razas", 0, COLOR_TEXTO)
    LabelTitulo = Fuente.render("Catalogo de personajes I", 0, COLOR_TEXTO)
    LabelPersonaje = Fuente.render("Personaje", 0, COLOR_TEXTO)
    LabelArma = Fuente.render("Arma", 0, COLOR_TEXTO)
    LabelArmadura = Fuente.render("Armadura", 0, COLOR_TEXTO)
    LabelCabeza = Fuente.render("Cabeza", 0, COLOR_TEXTO)

    # Imagenes, rectángulos y demás de todos los botones
    imagen_boton1 = pygame.image.load('Imagenes/BotonHumanos.png')
    rect_boton_1 = imagen_boton1.get_rect()
    rect_boton_1.topleft = (20, 130)
    imagen_boton2 = pygame.image.load('Imagenes/BotonElfos.png')
    rect_boton_2 = imagen_boton2.get_rect()
    rect_boton_2.topleft = (20, 210)
    imagen_boton3 = pygame.image.load('Imagenes/BotonOrcos.png')
    rect_boton_3 = imagen_boton3.get_rect()
    rect_boton_3.topleft = (20, 290)

    # Listado de botones en un diccionario
    botones = []

    botones.append({'nombre': "BotonHumanos", 'imagen': imagen_boton1, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'nombre': "BotonElfos", 'imagen': imagen_boton2, 'rect': rect_boton_2, 'on_click': False})
    botones.append({'nombre': "BotonOrcos", 'imagen': imagen_boton3, 'rect': rect_boton_3, 'on_click': False})

    # Fondo
    imagen_fondo = pygame.transform.scale(pygame.image.load('Imagenes/fondo9.jpg'), DIMENSIONES)

    # Imagen negra inicial
    imagen_arma = pygame.transform.scale(pygame.image.load('Imagenes/inicial.jpg'), (150, 150))
    imagen_armadura = pygame.transform.scale(pygame.image.load('Imagenes/inicial.jpg'), (150, 150))
    imagen_cabeza = pygame.transform.scale(pygame.image.load('Imagenes/inicial.jpg'), (150, 150))
    imagen_personaje = pygame.transform.scale(pygame.image.load('Imagenes/inicial.jpg'), (150, 150))

    # Intento 1 de poner imagenes
    Posiciones = []

    Posiciones.append({'posicionarma': (450, 110)})

    while jugando:

        ventana.blit(imagen_fondo, (0, 0))
        ventana.blit(LabelRazas, (60, 60))
        ventana.blit(LabelTitulo, (170, 10))
        ventana.blit(LabelPersonaje, (270, 60))
        ventana.blit(imagen_personaje, (250, 110))
        ventana.blit(LabelArmadura, (470, 60))
        ventana.blit(imagen_armadura, (450, 110))
        ventana.blit(LabelArma, (300, 280))
        ventana.blit(imagen_arma, (250, 330))
        ventana.blit(LabelCabeza, (480, 280))
        ventana.blit(imagen_cabeza, (450, 330))

        dibujar_botones(botones, ventana)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Detectar clicks
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect(mouse[0], mouse[1], 1, 1)
                    if boton['on_click']:
                        if boton['nombre'] == 'BotonHumanos':
                            objeto_arma = FabricaHumanos().CrearArma()
                            imagen_arma = objeto_arma.imagenarma()
                            objeto_armadura = FabricaHumanos().CrearArmadura()
                            imagen_armadura = objeto_armadura.imagenarmadura()
                            objeto_cabeza = FabricaHumanos().CrearCabeza()
                            imagen_cabeza = objeto_cabeza.imagencabeza()
                            objeto_personaje = FabricaHumanos().CrearPersonaje()
                            imagen_personaje = objeto_personaje.imagenpersonaje()
                        elif boton['nombre'] == 'BotonElfos':
                            objeto_arma = FabricaElfos().CrearArma()
                            imagen_arma = objeto_arma.imagenarma()
                            objeto_armadura = FabricaElfos().CrearArmadura()
                            imagen_armadura = objeto_armadura.imagenarmadura()
                            objeto_cabeza = FabricaElfos().CrearCabeza()
                            imagen_cabeza = objeto_cabeza.imagencabeza()
                            objeto_personaje = FabricaElfos().CrearPersonaje()
                            imagen_personaje = objeto_personaje.imagenpersonaje()
                        elif boton['nombre'] == 'BotonOrcos':
                            objeto_arma = FabricaOrcos().CrearArma()
                            imagen_arma = objeto_arma.imagenarma()
                            objeto_armadura = FabricaOrcos().CrearArmadura()
                            imagen_armadura = objeto_armadura.imagenarmadura()
                            objeto_cabeza = FabricaOrcos().CrearCabeza()
                            imagen_cabeza = objeto_cabeza.imagencabeza()
                            objeto_personaje = FabricaOrcos().CrearPersonaje()
                            imagen_personaje = objeto_personaje.imagenpersonaje()
                        else:
                            print "ERROR GRAVÍSIMO IMPERDONABLE"

            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False

        pygame.display.flip()
        pygame.display.update()


def pantalla_bienvenida():
    pygame.init()
    ventana_bienvenido = pygame.display.set_mode(DIMENSIONES)
    Fuente = pygame.font.SysFont("Arial", 60)

    #IMÁGENES Y RECTÁNGULOS DE LA PRIMERA PÁGINA
    imagen_fondo = pygame.transform.scale(pygame.image.load('Imagenes/fondo9.jpg'), DIMENSIONES)
    imagen_boton_catalogo = pygame.image.load('Imagenes/BotonCatalogo.png')
    rect_boton_catalogo = imagen_boton_catalogo.get_rect()
    rect_boton_catalogo.topleft = (100, 200)
    imagen_boton_crear = pygame.image.load('Imagenes/BotonCreacion.png')
    rect_boton_crear = imagen_boton_crear.get_rect()
    rect_boton_crear.topleft = (350, 200)

    # BOTONES DE LA PÁGINA INICIAL
    botones = []

    botones.append(
        {'nombre': "BotonCatalogo", 'imagen': imagen_boton_catalogo, 'rect': rect_boton_catalogo, 'on_click': False})
    botones.append({'nombre': "BotonCrear", 'imagen': imagen_boton_crear, 'rect': rect_boton_crear, 'on_click': False})

    while True:

        LabelBienvenido = Fuente.render("Bienvenido", 0, COLOR_TEXTO)
        ventana_bienvenido.blit(imagen_fondo, (0, 0))
        ventana_bienvenido.blit(LabelBienvenido, (200, 100))

        dibujar_botones(botones, ventana_bienvenido)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect(mouse[0], mouse[1], 1, 1)
                    if boton['on_click']:
                        if boton['nombre'] == 'BotonCatalogo':
                            principal()
                        elif boton['nombre'] == 'BotonCrear':
                            pass
                        else:
                            print "ERROR GRAVÍSIMO IMPERDONABLE"

        pygame.display.flip()
        pygame.display.update()


def dibujar_botones(lista_botones, ventana):
    for boton in lista_botones:
        if boton['on_click']:
            ventana.blit(boton['imagen'], boton['rect'])
        else:
            ventana.blit(boton['imagen'], boton['rect'])


if __name__ == "__main__":
    pantalla_bienvenida()
