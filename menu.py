def opcion(teclas, opcion):
    if (teclas[pygame.K_w] or teclas[pygame.K_UP]) and opcion > 0:
        opcion -= 1
    if (teclas[pygame.K_s] or teclas[pygame.K_DOWN]) and opcion < 3:
        opcion += 1
    return opcion

def boton(screen, fuente, c, texto, x, y, ancho, alto, seleccionado):
    if seleccionado:
        pygame.draw.rect(screen, c["ROJO"], (x, y, ancho, alto))
    else:
        pygame.draw.rect(screen, c["BLANCO"], (x, y, ancho, alto))

    label = fuente.render(texto, True, c["NEGRO"])
    screen.blit(label, (x + ancho//2 - label.get_width()//2,
                        y + alto//2 - label.get_height()//2))


def menu():
    pygame.init()
    screen = pantalla()
    pygame.display.set_caption("Crossy Road")
    clock = pygame.time.Clock()
    seguir = True
    opcion_actual = 3
    c = color()
    fuente = pygame.font.SysFont(None, 40)

    while seguir:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                seguir = False

        tecla = pygame.key.get_pressed()
        opcion_actual = opcion(tecla, opcion_actual)

        # Dibujo de botones
        boton(screen, fuente, c, "JUGAR",    300, 150, 240, 60, opcion_actual == 0)
        boton(screen, fuente, c, "ESTADISTICAS", 300, 250, 240, 60, opcion_actual == 1)
        boton(screen, fuente, c, "CRÉDITOS", 300, 350, 240, 60, opcion_actual == 2)
        boton(screen, fuente, c, "SALIR",    300, 450, 240, 60, opcion_actual == 3)
        if tecla[pygame.K_RETURN]:
            seguir=False

        pygame.display.update()
    
    pygame.quit()
    return opcion_actual
