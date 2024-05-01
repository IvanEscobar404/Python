import pygame, sys, time, random

pygame.init()

play_surface = pygame.display.set_mode((500, 500))  ## El alto y el ancho de nuestro programa.

font = pygame.font.Font(None, 30)  ##creamos la puntuacion en la pantalla del juego

fps = pygame.time.Clock()  ##creamos la variable de los Frames Por Segundos


def food():
    random_pos = random.randint(0,49)*10
    food_pos = [random_pos, random_pos]
    return food_pos


def main():

    snake_pos = [100, 50]  
    snake_body = [[100,50],[90,50],[80,50]]  
    change = "RIGHT"
    run = True
    food_pos = food()
    score = 0

    while run:

        for event in pygame.event.get():  ##Este for obtiene todos los eventos que ocurren en la pantalla del juego en event
            if event.type == pygame.QUIT:   ##Si presionamos en la X en la pantalla del juego, se cerrara el juego.
                run = False   ##False para cerrar el juego.
            if event.type == pygame.KEYDOWN: ##el keydown es para las actividades de las teclas para la movilidad
                if event.key == pygame.K_RIGHT: ##si es la flechha hacia la derecha
                    change = "RIGHT"            ##se movera a la derecha.
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
        if change == "RIGHT":
            snake_pos[0] += 10  ##Lo que hacemos al mover las flechas es sumar o restar pixeles, (es un efecto optico, osea que no se mueve la serpiente, sino que se le agregan o restan pixeles y eso hace el supuesto "movimiento").
        if change == "LEFT":
            snake_pos[0] -= 10
        if change == "UP":
            snake_pos[1] -= 10
        if change == "DOWN":
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos))

        if snake_pos == food_pos:  ##Cuando la serpiente coma la comida
            food_pos = food()       ##llamamos el metodo de food nuevamente para que se cambie de posicion totalmente random.
            score += 1
            print(score)
        else:   ##si no come la comida, seguira con el mismo tamaÃ±o y se usara el pop para que se mantenga con los mismos px.
            snake_body.pop()  ##Elimina el array de la ultima posicion, osea los pixeles de la serpiente. esto permite que la serpiente no sea infinitamente larga
        
        head = snake_body[-1]
        for i in range(len(snake_body) - 1): 
            part = snake_body[i]
            if head[0] == part[0] and head[1] == part[1]:
                run = False
                print("PERDISTE BESTIA")

        play_surface.fill((0,0,0))  ##ponemos la pantalla en negra, en propiedar rgb, 0,0,0.

        for pos in snake_body: ## este for va a recorrer pos en el cuerpo de la serpiente
            pygame.draw.rect(play_surface,(0,255,0), pygame.Rect(pos[0], pos[1], 10, 10)) ##L e pedimos que dibuje un rectangulo con draw, con el playsurface le damos el color ver a la serpiente.
        
        pygame.draw.rect(play_surface,(169,6,6), pygame.Rect(food_pos[0], food_pos[1], 10, 10))  ##dibujamos la fruta de color rojo
        
        text = font.render(str(score),0,(200,60,80))  ##la puntuacion la pasamos a string, con el color medio rojizo
        play_surface.blit(text, (480,20)) ##Implementamos la puntuacuion en la pos 480px en el eje X, y 20 en el eje Y

        if score < 10:  ##Si la puntuacion es menos de 10, tendremos 15 fps
            fps.tick(10) ##10 fps
        if score >= 10: ##si llegamos a mas de 10, aumentara los fps a 20
            fps.tick(20)
    
        if snake_pos[0] <= 0 or snake_pos[0] >= 500: ##si la serpiente choca con la pared que es de 500px, el juego se cierra. Osea, si supera los pixeles limitados de los ejes, este eje es el X.
            run = False
            print("PERDISTE BESTIA")
        if snake_pos[1] <= 0 or snake_pos[1] >= 500: ##lo mismo para la posicion del eje Y
            run = False
            print("PERDISTE BESTIA")

        pygame.display.flip()

main()  ##EJECUTAMOS EL MAIN, funcion PRINCIPAL

pygame.quit()  ##el pygame.quit, es para que se cierre el programa al terminar el juego/terminar el bucle.