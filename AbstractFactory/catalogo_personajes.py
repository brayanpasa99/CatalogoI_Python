#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *

from AbstractFactory.FabricaElfos import FabricaElfos
from AbstractFactory.FabricaHumanos import FabricaHumanos
from AbstractFactory.FabricaOrcos import FabricaOrcos
from BuilderPattern.Elfo import Elfo
from BuilderPattern.Humano import Humano
from BuilderPattern.Orco import Orco

DIMENSIONES = (650, 500)
COLOR_TEXTO = (243, 255, 0)


def catalogo_personajes():
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

        __dibujar_botones(botones, ventana)

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

                            ImagenesHumanos = Humano()
                            imagen_arma = ImagenesHumanos.obtenerarma()
                            imagen_armadura = ImagenesHumanos.obtenerarmadura()
                            imagen_cabeza = ImagenesHumanos.obtenercabeza()
                            imagen_personaje = ImagenesHumanos.obtenerpersonaje()
                        elif boton['nombre'] == 'BotonElfos':

                            ImagenesElfos = Elfo()
                            imagen_arma = ImagenesElfos.obtenerarma()
                            imagen_armadura = ImagenesElfos.obtenerarmadura()
                            imagen_cabeza = ImagenesElfos.obtenercabeza()
                            imagen_personaje = ImagenesElfos.obtenerpersonaje()
                        elif boton['nombre'] == 'BotonOrcos':

                            ImagenOrcos = Orco()
                            imagen_arma = ImagenOrcos.obtenerarma()
                            imagen_armadura = ImagenOrcos.obtenerarmadura()
                            imagen_cabeza = ImagenOrcos.obtenercabeza()
                            imagen_personaje = ImagenOrcos.obtenerpersonaje()
                        else:
                            print "ERROR GRAVÍSIMO IMPERDONABLE"
                            sys.exit()

            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False

        pygame.display.flip()
        pygame.display.update()

def __dibujar_botones(lista_botones, ventana):
    for boton in lista_botones:
        if boton['on_click']:
            ventana.blit(boton['imagen'], boton['rect'])
        else:
            ventana.blit(boton['imagen'], boton['rect'])
