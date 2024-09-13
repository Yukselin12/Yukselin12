#pgzero

import random

WIDTH, HEIGHT = 600, 300

TITLE = "Minijuegos Yuksel"

FPS = 30

# Actors

FONDO = Actor("background")
play = Actor("play", (300 , 150))
cross = Actor("cross", (580 , 20))
colec = "Coleccion"
rein = Actor("reintentar", (400 , 200))
y = random.randint(20 , 280) # Es necesario que este aqui

# Tabs

tab = Actor("papu",(0 , y))
tab1 = Actor("papu",(0 , y))
tab2 = Actor("papu",(0 , y))

# Gato y Perro

cat = Actor("Idle", (70, 180))
dog = Actor("Idle_perro", (540, 180))

mini = Actor("minijuego1",(90,90))
mini2 = Actor("mini2",(380,120))
FONDOMINI = Actor("fondo mini")
tienda = Actor("tienda", (300 , 205))

# La girafa pro 😎 

giraffe = Actor("giraffe",(310 , 110))

# Cat2 y Dog2 y Dog3

cat2 = Actor("Idle",(480 , 130))
dog2 = Actor("Idle(1)", (161 , 180))
dog3 = Actor("perro_jetpack", (161 , 180))

# Creditos y coleccion

Creditos = Actor("Creditos",(150 , 150))
Coleccion = Actor("coleccion",(450 , 150))

# Variables y listas

players = "1"
inventario = []
arboles = []
tablas = []
count = 0
count_players = 0
mode = "menu"
count_skin_gif = 0

Derecha = False
Izquierda = False

# Corazon Actor

c = Actor("corazon",(30,50))
c1 = Actor("corazon",(80,50))
c2 = Actor("corazon",(130,50))
c3 = Actor("corazon",(180,50))
c4 = Actor("corazon",(30,50))

co = Actor("corazon",(550,280))
co1 = Actor("corazon",(500,280))
co2 = Actor("corazon",(450,280))
co3 = Actor("corazon",(400,280))
co4 = Actor("corazon",(350,280))

# Listas de corazones

corazon = [c,c1,c,c3,c4]
corazon1 = [co,co1,co2,co3]

# Spawnea los arboles de forma aleatoria 

for i in range(20):
    x = random.randint(0, 580)
    arbol = Actor("arbol", (x , 140))
    arboles.append(arbol)

semilla = Actor("semilla", (arbol.x, 210))   # Modificado para que la semilla aparezca en la posición del último árbol creado
tabla = Actor("tabla", (arbol.x, 200))  # Modificado para que la tabla aparezca en la posición del último árbol reado
tabla_dragging = False  # Variable para el arrastre de la tabla
tabla_dragging_index = -1  # Índice de la tabla que se está arrastrando

# DRAW

def draw():
    global mode, players
    
    FONDO.draw()
    if mode == "menu":
       play.draw()
       tienda.draw()
       Creditos.draw()
       Coleccion.draw()
       # Texto 1
       
       screen.draw.text("Minijuegos Yuksel", center=(300, 10), color="white", fontsize=30)
       screen.draw.text("Version 1.0", center=(60, 210), color="white", fontsize=20)
       screen.draw.text("Creator: Yuksel", center=(520, 210), color="white", fontsize=20)
       screen.draw.text(str(count), center=(300, 50), color="white", fontsize=20)
       
    elif mode == "game":
       for arbol in arboles:
           arbol.draw()
           
       for tabla in tablas:  # Dibuja todas las tablas presentes en el inventario
           tabla.draw()
        
       # Texto 2
       
       screen.draw.text(str(count), center=(300, 10), color="white", fontsize=20)
       screen.draw.text("Jugador 1", center=(60,10))
       # Corazon 1
       
       cross.draw()
       
       c.draw()
       c1.draw()
       c2.draw()
       c3.draw()
       
       dog.draw()
       
    # Corazon 2
    
    if players == "2" and mode == "game":
       
        cat.draw()
        
        co.draw()
        co1.draw()
        co2.draw()
        co3.draw()
        screen.draw.text("Jugador 2", center=(520,250))
        
    # MINI
    
    if mode == "mini":
        FONDOMINI.draw()
        cross.draw()
        mini.draw()
        mini2.draw()
        cross.draw()
        screen.draw.text("Supervivence (pacific)",center=(130,20),color="white",fontsize=25)
        screen.draw.text("Press G for two players (sometimes)",center=(300,260),color = "white", fontsize = 30)
        screen.draw.text("Slide (Normal)",center=(380,20))
        
    # Creditos    
        
    if mode == "credits":
        FONDOMINI.draw()
        cross.draw()
        
        # Texto 3
        
        screen.draw.text("Art: OpenGameArt.org and kenny.nl ¡Thanks!", center=(250,150))
        screen.draw.text("Programation and Creation: Andy Yuksel Baris Cumbal", center=(295,180))
    
    # Tienda    
        
    elif mode == "tienda":
        FONDO.draw()
        cross.draw()
        # Texto 4
        
        screen.draw.text("Puntos", center=(50 , 10), color ="white", fontsize=30)
        screen.draw.text(str(count), center=(120,12), color="white", fontsize=25)
        screen.draw.text("Skins",center=(310 , 20), color="white", fontsize=40 )
        screen.draw.text("Precio $15",center=(310 , 200), color="white", fontsize=30)
        screen.draw.text("GRATIS!!!",center=(480 , 200), color="white", fontsize=30)
        
        giraffe.draw()
        cat2.draw()
        
    # Mini 2
        
    if mode == "game1":
        FONDOMINI.draw()
        cross.draw()
        dog3.draw()
        tab.draw()
        tab1.draw()
        tab2.draw()
        screen.draw.text(dog3.y,pos=(500,60))
        
    # Coleccion
        
    if mode == "Coleccion":
        cross.draw()
        screen.draw.text("Coleccion", center=(300 , 15), fontsize = 30)
        
    if mode == "Coleccion" and count_skin_gif >= 1:
        cross.draw()
        screen.draw.text(colec, center=(300 , 15), fontsize = 30)
        giraffe.draw()
    
    # End...
    
    if mode == "end":
        FONDO.draw()
        rein.draw()
        cross.draw()
        
def on_mouse_down(button, pos): # Detecta los clicks
    global mode, count, tabla_dragging, tabla_dragging_index,tabla, cat, count_skin_gif
    
    # Collidepoints
    
    if mode == "mini":
       if mini.collidepoint(pos):
          mode = "game"
       if mini2.collidepoint(pos):
           mode = "game1"
          
    elif mode == "menu":
       if play.collidepoint(pos):
          mode = "mini"
          
    if mode == "menu":
        if tienda.collidepoint(pos):
            mode = "tienda"
            
        if Creditos.collidepoint(pos):
            mode = "credits"
            
        if Coleccion.collidepoint(pos):
            mode = "Coleccion"
            cross.x = -200
            animate(cross, tween="bounce_end", duration = 3, x = 580)
            FONDO.x = -200
            animate(FONDO, tween="bounce_end", duration = 1.5, x = 300)
            giraffe.x = - 200
            animate(giraffe, tween="accelerate", duration = 2, x = 310)
        
    if cross.collidepoint(pos):
        mode = "menu"
        
    if mode == "tienda":
        if cat2.collidepoint(pos):
                cat2.y = 120
                animate(cat2, tween='bounce_end', duration=0.5, y=130)
                cat.image = "Idle"
    
        if count >= 15:
        
            if giraffe.collidepoint(pos):
                    giraffe.y = 110
                    animate(giraffe, tween='bounce_end', duration=0.5, y=120)
                    cat.image = "giraffe"
                    count -= 15
                    count_skin_gif += 1
                    
    if giraffe.collidepoint(pos) and count_skin_gif >= 1 and mode == "Coleccion":
                giraffe.y = 110
                animate(giraffe, tween='bounce_end', duration=0.5, y=120)
                cat.image = "giraffe"
            
            
    if mode == "game":
        if cross.collidepoint(pos):
            mode = "mini"
            
        if button == mouse.LEFT:
            for index, arbol in enumerate(arboles):
                if arbol.collidepoint(cat.pos) or arbol.collidepoint(dog.pos):
                    arboles.remove(arbol)
                    
                    # Generar nueva tabla en la posición del árbol destruido
                    
                    count += 1
                    nueva_tabla = Actor("tabla", pos=arbol.pos)
                    tablas.append(nueva_tabla)
                    break
        if rein.collidepoint(pos):
            tab.x = 0
            tab1.x = 0
            tab2.x = 0
            tab.y = y
            tab1.y = y
            tab2.y = y
            dog3.x = 161
            dog3.y = 180
            mode = "game1"
    
                
            for index, tabla in enumerate(tablas):  # Verifica si se hace clic en alguna tabla en el inventario
                if tabla.collidepoint(pos):
                    tabla_dragging = True  # Comienza el arrastre de la tabla
                    tabla_dragging_index = index  # Guarda el índice de la tabla que se está arrastrando
                    tabla.pos = pos  # Establece la posición inicial de la tabla
                

def on_mouse_up(button, pos):
    global tabla_dragging
    
    if button == mouse.LEFT and tabla_dragging:
        tabla_dragging = False # Detiene el arrastre de la tabla

# UPDATE

def update(dt):
    global mode, tabla_dragging, tabla, players, count_players, count, tab, tab1, tab2, y
    
    if keyboard.G:
        players = "2"
        count_players += 1
        
    if count_players == 5:
        players = "1"
        count_players = 0
        
    if keyboard.Y:
        count += 1
        
    # Movimiento
    
    if mode == "game":
        
        # Movimiento del perro
        
        if keyboard.D and dog.x < 580:
            dog.x += 10
            dog.image = "Idle(1)"
        elif keyboard.A and dog.x > 20:
            dog.x -= 10
            dog.image = "Idle_perro"
            
    if mode == "game1":
        tab.x -= 10
        tab1.x -= 10
        tab2.x -= 10
        
        if tab.x <= -80:
            tab.x = 600
            y = random.randint(20 , 280)
            tab = Actor("tab",(600 , y))
        if dog3.colliderect(tab):
            print("mi mami")
            
        if tab1.x <= -80:
            tab1.x = 600
            y = random.randint(20 , 280)
            tab1 = Actor("tab",(600 , y))
        if dog3.colliderect(tab1):
            print("LOL")
            
        if tab2.x <= -80:
            tab2.x = 600
            y = random.randint(20 , 280)
            tab2 = Actor("tab",(600 , y))
        if dog3.colliderect(tab2):
            print("SUS")
        
        if keyboard.up or keyboard.w:
            dog3.y -= 10
            
        elif keyboard.down or keyboard.s:
            dog3.y += 10
    
    if mode == "game" and players == "2" and cat.image == "Idle" or mode == "game" and players == "2" and cat.image == "idle_right"       : # Con esto puedes poner 2 jugadores
    
        # Movimiento del gato
        
        if keyboard.left and cat.x > 20:
            cat.x -= 10
            cat.image = "idle_right"
            
        elif keyboard.right and cat.x < 580:
            cat.x += 10
            cat.image = "Idle"
            
    if mode == "game" and players == "2" and cat.image == "giraffe":
        
        # Movimiento de la girafa
        
        if keyboard.left and cat.x > 20:
            cat.x -= 10
            
        elif keyboard.right and cat.x < 580:
            cat.x += 10
            
    if tabla_dragging:
        tabla = tablas[tabla_dragging_index]  # Obtiene la tabla que se está arrastrando
        tabla.pos = pygame.mouse.get_pos()  # La posición de la tabla sigue al ratón


