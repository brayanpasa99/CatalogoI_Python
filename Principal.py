#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from AbstractFactory import catalogo_personajes

DIMENSIONES = (650, 500)
COLOR_TEXTO = (243, 255, 0)


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

        __dibujar_botones(botones, ventana_bienvenido)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect(mouse[0], mouse[1], 1, 1)
                    if boton['on_click']:
                        if boton['nombre'] == 'BotonCatalogo':
                            catalogo_personajes.catalogo_personajes()
                        elif boton['nombre'] == 'BotonCrear':
                            pass
                        else:
                            print "ERROR GRAVÍSIMO IMPERDONABLE"

        pygame.display.flip()
        pygame.display.update()


def __dibujar_botones(lista_botones, ventana):
    for boton in lista_botones:
        if boton['on_click']:
            ventana.blit(boton['imagen'], boton['rect'])
        else:
            ventana.blit(boton['imagen'], boton['rect'])


if __name__ == "__main__":
    pantalla_bienvenida()
