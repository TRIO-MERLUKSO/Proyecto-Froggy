def movimiento(jugador,velocidad):
    teclas = pygame.key.get_pressed()
    x=jugador.x
    y=jugador.y
    if teclas[pygame.K_w]:
        y -= velocidad  # arriba
    if teclas[pygame.K_s]:
        y += velocidad  # abajo
    if teclas[pygame.K_a]:
        x -= velocidad  # izquierda
    if teclas[pygame.K_d]:
        x += velocidad  # derecha
    if jugador.x<15:
        x +=velocidad
    if jugador.x>=735:
        x -=velocidad
    if jugador.y<=15:
        y+=velocidad
    if jugador.y>=735:
        y-=velocidad
    return x,y
