import pygame
import os
import random


############ INICIO / DEFINICION DE PANTALLA ############
#Inicializa la pantalla
pygame.init()
ANCHO, ALTURA = 1152, 764
ventana = pygame.display.set_mode((ANCHO,ALTURA)) #Tamano de la ventana
pygame.display.set_caption("AHORCADO PRACTICA PISA") #Define un nombre a la ventana





############ CARGA DE IMAGENES ############
#Carga las imagenes
imagenes = []
for i in range(7):
    imagenes.append(pygame.image.load("hangman"+str(i)+".png"))





############ VARIABLES Y CONSTANTES ############
#Variables de juego
hangmanVida = 0
respuestaCorrecta = 42
respuestaIngresada = ''
enviarBotonVisibilidad = True
numPregunta = 0
problemSetValidity = False
numeroCorrectas = 0

#Setup para el loop del juego
FPS = 60
clock = pygame.time.Clock()
run = True
CorrectoValido = 0   

#Constantes del juego / COLORES USADOS
BLANCO = (245,245,220)
NEGRO = (0,0,0)
GRISOSCURO = (70,70,70)
ROJO = (255,0, 0)
ROJOOSCURO = (128,0,0)
CRIMSON = (220,20,60)
VERDE = (0,255,0)
AZUL = (0,0,255)
AZULCLARO = (102,255,255)
TEAL = (0,128,128)
CAFE = (139,69,19)
CAFECLARO = (222,184,135)
HONEYDEW = (240,255,240)
LAVANDER = (230,230,250)

#Fuentes de Texto
tituloPortadaFont = pygame.font.SysFont("trebuchet",48)
equipoPortadaFont = pygame.font.SysFont("times new roman bold",29)
tituloFont = pygame.font.SysFont("trebuchet", 32)
subtitoFont = pygame.font.SysFont("arial", 28)
parrafoFont = pygame.font.SysFont("times new roman", 18)
#parrafoResueltoFont = pygame.font.SysFont()
resueltoFont = pygame.font.SysFont("arial bold", 20)
respuestaResueltoFont = pygame.font.SysFont("arial bold", 24)
enviarLabelFont = pygame.font.SysFont("trebuchet bold", 20)
respuestaFont = pygame.font.SysFont(None,24)
mensajeFinalFont = pygame.font.SysFont("times new Roman", 45)
instruccionFont = pygame.font.SysFont("arial",20)
#resultadosParrafoFont = pygame.font.SysFont("Comics Sans", 38)
resultadosParrafoFont = pygame.font.SysFont("britannic bold", 38)

#Cadenas de los Problemas
cadenaSubtitulo = ""
cadenaProblemaParrafo1 = "What is the answer to life the Universe and Everything?"
cadenaProblemaParrafo2 = ""
cadenaProblemaParrafo3 = ""
cadenaProblemaParrafo4 = ""
cadenaProblemaParrafo5 = ""
cadenaProblemaResueltoParrafo1 = ""
cadenaProblemaResueltoParrafo2 = ""
cadenaProblemaResueltoParrafo3 = ""
cadenaProblemaResueltoParrafo4 = ""
cadenaProblemaRespuestaResuletoParrafo = "ESTA ES LA RESPUESTA CORRECTA:"





############ FUNCIONES ############
### FUNCIONES DONDE SE ENCUENTRAN LOS PROBLEMAS ###
#Funcion para elegir problema
def set_problem(numeroDeProblema):
    n = random.randint(1,6)
    
    if (n == 1):
        Problema_01()
    elif (n == 2):
        Problema_02()
    elif (n == 3):
        Problema_03()
    elif (n == 4):
        Problema_04()
    elif (n == 5):
        Problema_05()
    elif (n == 6):
        Problema_06()
    elif (n == 7):
        Problema_07()
    else:
        pass

#Problema Algebra.01
def Problema_01():
    
    global problemSetValidity

    if (problemSetValidity == False):
        global cadenaSubtitulo
        global cadenaProblemaParrafo1
        global cadenaProblemaParrafo2
        global cadenaProblemaParrafo3
        global cadenaProblemaParrafo4
        global cadenaProblemaParrafo5
        global cadenaProblemaResueltoParrafo1
        global cadenaProblemaResueltoParrafo2
        global cadenaProblemaResueltoParrafo3
        global cadenaProblemaResueltoParrafo4
        global cadenaProblemaRespuestaResuletoParrafo
        global respuestaCorrecta


        n = round(random.randint(1,10))
        zar = 4.2
        ans = zar*n
        ans = round(ans,1)

        cadenaSubtitulo = "ALGEBRA"
        cadenaProblemaParrafo1 = ""
        cadenaProblemaParrafo2 = "El tipo de cambio entre dolar de singapur y el rand sudafricano es de: 1SDG = 4.2 ZAR"
        cadenaProblemaParrafo3 = "Si cambias " + str(n) + " dolares de singapur en rands sudafricanos con este tipo de cambio,"
        cadenaProblemaParrafo4 = "¿Cuanto dinero recibirias en rands sudafricanos?"
        cadenaProblemaParrafo5 = ""
        cadenaProblemaResueltoParrafo1 = ""
        cadenaProblemaResueltoParrafo2 = "Dinero recibido: " + str(zar) + " * " + str(n)
        cadenaProblemaResueltoParrafo3 = "Dinero recibido: " + str(ans)
        cadenaProblemaResueltoParrafo4 = ""
        cadenaProblemaRespuestaResuletoParrafo = "ESTA ES LA RESPUESTA CORRECTA: " + str(ans)

        respuestaCorrecta = ans

        problemSetValidity = True

#Problema Probabilidad.01
def Problema_02():
    global problemSetValidity

    if (problemSetValidity == False):
        global cadenaSubtitulo
        global cadenaProblemaParrafo1
        global cadenaProblemaParrafo2
        global cadenaProblemaParrafo3
        global cadenaProblemaParrafo4
        global cadenaProblemaParrafo5
        global cadenaProblemaResueltoParrafo1
        global cadenaProblemaResueltoParrafo2
        global cadenaProblemaResueltoParrafo3
        global cadenaProblemaResueltoParrafo4
        global cadenaProblemaRespuestaResuletoParrafo
        global respuestaCorrecta

        n = random.randint(1,5)
        factn = 1
        i = 1
        while i <= n:
            factn = factn * i
            i = i + 1
        ans = factn/4
        ans = round(ans,2)

        cadenaSubtitulo = "PROBABILIDAD"
        cadenaProblemaParrafo1 = "En una pizzería se puede elegir una pizza básica con dos ingredientes: queso y tomate."
        cadenaProblemaParrafo2 = "También puedes diseñar tu propia pizza con ingredientes adicionales."
        cadenaProblemaParrafo3 = "Se pueden seleccionar entre " + str(n) + " ingredientes adicionales diferentes: aceitunas, jamón, champiñones y salami."
        cadenaProblemaParrafo4 = "Jaime quiere encargar una pizza con dos ingredientes adicionales diferentes."
        cadenaProblemaParrafo5 = "¿Cuántas combinaciones diferentes podría seleccionar Jaime?"
        cadenaProblemaResueltoParrafo1 = ""
        cadenaProblemaResueltoParrafo2 = "Factorial: " + str(n) + "!"
        cadenaProblemaResueltoParrafo3 = "Numero de combinaciones: " + str(factn) + " / 4"
        cadenaProblemaResueltoParrafo4 = "Numero de combinaciones: " + str(ans)
        cadenaProblemaRespuestaResuletoParrafo = "ESTA ES LA RESPUESTA CORRECTA: " + str(ans)

        respuestaCorrecta = ans

        problemSetValidity = True

#Problema Algebra.02
def Problema_03():
    global problemSetValidity

    if (problemSetValidity == False):
        global cadenaSubtitulo
        global cadenaProblemaParrafo1
        global cadenaProblemaParrafo2
        global cadenaProblemaParrafo3
        global cadenaProblemaParrafo4
        global cadenaProblemaParrafo5
        global cadenaProblemaResueltoParrafo1
        global cadenaProblemaResueltoParrafo2
        global cadenaProblemaResueltoParrafo3
        global cadenaProblemaResueltoParrafo4
        global cadenaProblemaRespuestaResuletoParrafo
        global respuestaCorrecta

        n = random.randint(100,500)
        ans = (n*60/100)
        ans = round(ans,2)

        cadenaSubtitulo = "ALGEBRA"
        cadenaProblemaParrafo1 = ""
        cadenaProblemaParrafo2 = "Estas preparando tu propio aliño para la ensalada. He aquí una receta para 100 mililitros (ml) de aliño:"
        cadenaProblemaParrafo3 = "- Aceite para ensalda: 60 ml - Vinagre: 30 ml - Salsa de soja: 10 ml"
        cadenaProblemaParrafo4 = "¿Cuántos mililitros (ml) de aceite para ensalada necesitas para preparar " + str(n) + " ml de este aliño?"
        cadenaProblemaParrafo5 = " *** Redondea tu resultado a 2 puntos decimales.***"
        cadenaProblemaResueltoParrafo1 = ""
        cadenaProblemaResueltoParrafo2 = "mL requeridos: (" + str(n) + " * 60) / 100"
        cadenaProblemaResueltoParrafo3 = "mL requeridos: " + str(ans)
        cadenaProblemaResueltoParrafo4 = ""
        cadenaProblemaRespuestaResuletoParrafo = "ESTA ES LA RESPUESTA CORRECTA: " + str(ans)

        respuestaCorrecta = ans

        problemSetValidity = True

#Problema Probabilidad.02
def Problema_04():
    global problemSetValidity

    if (problemSetValidity == False):
        global cadenaSubtitulo
        global cadenaProblemaParrafo1
        global cadenaProblemaParrafo2
        global cadenaProblemaParrafo3
        global cadenaProblemaParrafo4
        global cadenaProblemaParrafo5
        global cadenaProblemaResueltoParrafo1
        global cadenaProblemaResueltoParrafo2
        global cadenaProblemaResueltoParrafo3
        global cadenaProblemaResueltoParrafo4
        global cadenaProblemaRespuestaResuletoParrafo
        global respuestaCorrecta

        a=random.randint(3,10)
        b=random.randint(3,10)
        c=random.randint(3,10)
        total= a + b + c

        ans = int((a*100)//total)

        cadenaSubtitulo = "PROBABILIDAD"
        cadenaProblemaParrafo1 = ""
        cadenaProblemaParrafo2 = "La madre de Roberto le deja coger un caramelo de una bolsa. Él no puede ver los caramelos."
        cadenaProblemaParrafo3 = "En la bolsa hay: " + str(a) + " caramelos rojos, " + str(b) + " caramelos azules y " + str(c) + "caramelos verdes"
        cadenaProblemaParrafo4 = "¿Cuál es la probabilidad (porcentaje) de que Roberto extraiga un caramelo rojo? (no utilices decimales)"
        cadenaProblemaParrafo5 = ""
        cadenaProblemaResueltoParrafo1 = "Se toman en cuenta el total de caramenlos y la cantidad de caramelos rojos."
        cadenaProblemaResueltoParrafo2 = "Probabilidad que toque un caramelo rojo: (" + str(a) + " *  100) /" + str(total)
        cadenaProblemaResueltoParrafo3 = "Probabilidad que toque un caramelo rojo: " + str(ans) + "%"
        cadenaProblemaResueltoParrafo4 = ""
        cadenaProblemaRespuestaResuletoParrafo = "ESTA ES LA RESPUESTA CORRECTA: " + str(ans)

        respuestaCorrecta = ans

        problemSetValidity = True

#Problema Geometria.01
def Problema_05():
    global problemSetValidity

    if (problemSetValidity == False):
        global cadenaSubtitulo
        global cadenaProblemaParrafo1
        global cadenaProblemaParrafo2
        global cadenaProblemaParrafo3
        global cadenaProblemaParrafo4
        global cadenaProblemaParrafo5
        global cadenaProblemaResueltoParrafo1
        global cadenaProblemaResueltoParrafo2
        global cadenaProblemaResueltoParrafo3
        global cadenaProblemaResueltoParrafo4
        global cadenaProblemaRespuestaResuletoParrafo
        global respuestaCorrecta

        n1 = random.randint(1,100)
        n2 = random.randint(1,100)
        H2= (n1**2) + (n2**2)
        h = (H2**(1/2))

        ans = round(h,2)

        cadenaSubtitulo = "GEOMETRIA"
        cadenaProblemaParrafo1 = "Calcula el valor de la hipotenusa cuando los catetos tienen valores de " + str(n1) + " y " + str(n2)
        cadenaProblemaParrafo2 = "*** Redondea tu respuesta a 2 decimales ***"
        cadenaProblemaParrafo3 = "*** Si el tercer decimal es 5, redondealo como mayor ***"
        cadenaProblemaParrafo4 = "*** Ejemplo: 82.565 = 82.57 ***"
        cadenaProblemaParrafo5 = ""
        cadenaProblemaResueltoParrafo1 = "FORMULA DE PITAGORAS: (a^2 + b^2)^(1/2)"
        cadenaProblemaResueltoParrafo2 = "Hipotenusa: " + str(n1) + "^2 + " + str(n2) + "^2"
        cadenaProblemaResueltoParrafo3 = "Hipotenusa: " + str(H2) + "^(1/2)"
        cadenaProblemaResueltoParrafo4 = "Hipotenusa: " + str(h)
        cadenaProblemaRespuestaResuletoParrafo = "ESTA ES LA RESPUESTA CORRECTA: " + str(ans)

        respuestaCorrecta = ans

        problemSetValidity = True

#Problema Algebra.03
def Problema_06():
    global problemSetValidity

    if (problemSetValidity == False):
        global cadenaSubtitulo
        global cadenaProblemaParrafo1
        global cadenaProblemaParrafo2
        global cadenaProblemaParrafo3
        global cadenaProblemaParrafo4
        global cadenaProblemaParrafo5
        global cadenaProblemaResueltoParrafo1
        global cadenaProblemaResueltoParrafo2
        global cadenaProblemaResueltoParrafo3
        global cadenaProblemaResueltoParrafo4
        global cadenaProblemaRespuestaResuletoParrafo
        global respuestaCorrecta

        t=random.randint(12,100)
        ans = 0.7*((t-12)**(1/2))
        ans = round(ans,2)

        cadenaSubtitulo = "ALGEBRA"
        cadenaProblemaParrafo1 = "Los líquenes crecen aproximadamente en forma de círculo. La relación entre el diámetro de este círculo y la edad del liquen se puede expresar"
        cadenaProblemaParrafo2 = "aproximadamente mediante la fórmula: d = 0.7 x √t −12 siendo “d” el diámetro del liquen en milímetros,"
        cadenaProblemaParrafo3 = "y “t” el número de años transcurridos desde que el hielo ha desaparecido."
        cadenaProblemaParrafo4 = "Calcula el diámetro que tendrá un liquen " + str(t) + " años después de que el hielo haya desaparecido."
        cadenaProblemaParrafo5 = "*** Redondea tu respuesta a 2 decimales, si el tercer decimal es '5' redondealo a mayor ***"
        cadenaProblemaResueltoParrafo1 = ""
        cadenaProblemaResueltoParrafo2 = "Diametro: 0.7 * ( (" + str(t) + " - 12) ** (1/2) )"
        cadenaProblemaResueltoParrafo3 = "Diametro: " + str(ans)
        cadenaProblemaResueltoParrafo4 = ""
        cadenaProblemaRespuestaResuletoParrafo = "ESTA ES LA RESPUESTA CORRECTA: " + str(ans)

        respuestaCorrecta = ans

        problemSetValidity = True

#Problema Algebra.04
def Problema_07():
    global problemSetValidity

    if (problemSetValidity == False):
        global cadenaSubtitulo
        global cadenaProblemaParrafo1
        global cadenaProblemaParrafo2
        global cadenaProblemaParrafo3
        global cadenaProblemaParrafo4
        global cadenaProblemaParrafo5
        global cadenaProblemaResueltoParrafo1
        global cadenaProblemaResueltoParrafo2
        global cadenaProblemaResueltoParrafo3
        global cadenaProblemaResueltoParrafo4
        global cadenaProblemaRespuestaResuletoParrafo
        global respuestaCorrecta

        t=random.randint(12,100)
        ans = 0.7*((t-12)**(1/2))
        ans = round(ans,2)

        cadenaSubtitulo = "ALGEBRA"
        cadenaProblemaParrafo1 = ""
        cadenaProblemaParrafo2 = "La subida al Monte Fuji sólo está abierta al público desde el 1 de julio hasta el 27 de agosto de cada año."
        cadenaProblemaParrafo3 = "Alrededor de unas 200.000 personas suben al Monte Fuji durante este periodo de tiempo"
        cadenaProblemaParrafo4 = "Como media, ¿alrededor de cuántas personas suben al Monte Fuji cada día?"
        cadenaProblemaParrafo5 = ""
        cadenaProblemaResueltoParrafo1 = ""
        cadenaProblemaResueltoParrafo2 = "Diametro: 0.7 * ( (" + str(t) + " - 12) ** (1/2) )"
        cadenaProblemaResueltoParrafo3 = "Diametro: " + str(ans)
        cadenaProblemaResueltoParrafo4 = ""
        cadenaProblemaRespuestaResuletoParrafo = "ESTA ES LA RESPUESTA CORRECTA: " + str(ans)

        respuestaCorrecta = ans

        problemSetValidity = True

### FUNCIONES DE JUEGO ###
#Funcion de pantalla de inicio / portada
def display_portada():
    
    global numPregunta

    ventana.fill(BLANCO)

    tituloPortadaTexto = tituloPortadaFont.render('AHORCADO CON PROBLEMAS TIPO PRUEBA PISA', True, NEGRO)
    autoresPortadaTexto = equipoPortadaFont.render('HECHO POR:', True, NEGRO)
    autoresPortadaTexto1 = parrafoFont.render("EQUIPO 10", True, NEGRO)
    autoresPortadaTexto2 = parrafoFont.render("Cristina Paola Martinez Berumen - A01177662", True, GRISOSCURO)
    autoresPortadaTexto3 = parrafoFont.render("Corín Vega Félix - A00830612", True, GRISOSCURO)
    autoresPortadaTexto4 = parrafoFont.render("Aldo Celis Cordova - A01423328", True, GRISOSCURO)
    instruccionPortadaTexto = instruccionFont.render("SI DESEAS EMPEZAR PRESIONA CUALQUIER TECLA", True, GRISOSCURO)


    tituloPortadaPosicion = tituloPortadaTexto.get_rect()
    autoresPortadaPosicion = autoresPortadaTexto.get_rect()
    autoresPortadaPosicion1 = autoresPortadaTexto1.get_rect()
    autoresPortadaPosicion2 = autoresPortadaTexto2.get_rect()
    autoresPortadaPosicion3 = autoresPortadaTexto3.get_rect()
    autoresPortadaPosicion4 = autoresPortadaTexto4.get_rect()
    instruccionPortadaPosicion = instruccionPortadaTexto.get_rect()


    tituloPortadaPosicion.center = (ANCHO/2,90)
    autoresPortadaPosicion.center = (ANCHO/2,160)
    autoresPortadaPosicion1.center = (ANCHO/2,200)
    autoresPortadaPosicion2.center = (ANCHO/2,230)
    autoresPortadaPosicion3.center = (ANCHO/2,250)
    autoresPortadaPosicion4.center = (ANCHO/2,270)
    instruccionPortadaPosicion.center = (ANCHO/2,ALTURA-70)


    ventana.blit(tituloPortadaTexto,tituloPortadaPosicion)
    ventana.blit(autoresPortadaTexto, autoresPortadaPosicion)
    ventana.blit(autoresPortadaTexto1,autoresPortadaPosicion1)
    ventana.blit(autoresPortadaTexto2, autoresPortadaPosicion2)
    ventana.blit(autoresPortadaTexto3, autoresPortadaPosicion3)
    ventana.blit(autoresPortadaTexto4, autoresPortadaPosicion4)
    ventana.blit(imagenes[6],(ANCHO/2 - 70,ALTURA/2)) #ALTURA-(ALTURA-200)
    ventana.blit(instruccionPortadaTexto,instruccionPortadaPosicion)


    pygame.display.update()

    continuarValido = True
    while continuarValido:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
                continuarValido = False
                numPregunta += 1
    
    #CorrectoValido = 0

#Funcion que refreshea la pantalla
def display_game_window():
    
    global hangmanVida
    global imagenes

    ventana.fill(BLANCO)

    tituloTexto = tituloFont.render('PROBLEMA DE PRUEBA PISA', True, GRISOSCURO)
    subtitoTexto = subtitoFont.render(cadenaSubtitulo, True, GRISOSCURO)
    parrafoTexto1 = parrafoFont.render(cadenaProblemaParrafo1, True, GRISOSCURO)
    parrafoTexto2 = parrafoFont.render(cadenaProblemaParrafo2, True, GRISOSCURO)
    parrafoTexto3 = parrafoFont.render(cadenaProblemaParrafo3, True, GRISOSCURO)
    parrafoTexto4 = parrafoFont.render(cadenaProblemaParrafo4, True, GRISOSCURO)
    parrafoTexto5 = parrafoFont.render(cadenaProblemaParrafo5, True, GRISOSCURO)
    respuestaTexto = respuestaFont.render(respuestaIngresada, True, ROJO)
    enviarTexto = enviarLabelFont.render("ENVIAR", True, NEGRO)

    tituloPosicion = tituloTexto.get_rect()
    subtitoPosicion = subtitoTexto.get_rect()
    parrafoPosicion1 = parrafoTexto1.get_rect()
    parrafoPosicion2 = parrafoTexto2.get_rect()
    parrafoPosicion3 = parrafoTexto3.get_rect()
    parrafoPosicion4 = parrafoTexto4.get_rect()
    parrafoPosicion5 = parrafoTexto5.get_rect()
    respuestaPosicion = respuestaTexto.get_rect()
    enviarPosicion = enviarTexto.get_rect()

    respuestaRect = pygame.Rect(200,200,180,32)
    enviarRectContorno = pygame.Rect(204,204,180,32)
    enviarRect = pygame.Rect(200,200,180,32)

    tituloPosicion.center = (ANCHO/2,ALTURA-(ALTURA-50))
    subtitoPosicion.center = (ANCHO/2,ALTURA-(ALTURA-80))
    parrafoPosicion1.center = (ANCHO/2,ALTURA-350)
    parrafoPosicion2.center = (ANCHO/2,ALTURA-325)
    parrafoPosicion3.center = (ANCHO/2,ALTURA-300)
    parrafoPosicion4.center = (ANCHO/2,ALTURA-275)
    parrafoPosicion5.center = (ANCHO/2,ALTURA-250)
    respuestaPosicion.center = (ANCHO/2,ALTURA-170)
    respuestaRect.center = (ANCHO/2,ALTURA-170)
    enviarRectContorno.center = (ANCHO/2,ALTURA-90)
    enviarRect.center = (ANCHO/2,ALTURA-90)
    enviarPosicion.center = (ANCHO/2,ALTURA-90)
 
    ventana.blit(tituloTexto,tituloPosicion)
    ventana.blit(subtitoTexto,subtitoPosicion)
    ventana.blit(imagenes[hangmanVida],(ANCHO/2 - 70,ALTURA-(ALTURA-150)))
    ventana.blit(parrafoTexto1,parrafoPosicion1)
    ventana.blit(parrafoTexto2,parrafoPosicion2)
    ventana.blit(parrafoTexto3,parrafoPosicion3)
    ventana.blit(parrafoTexto4,parrafoPosicion4)
    ventana.blit(parrafoTexto5,parrafoPosicion5)
    ventana.blit(respuestaTexto,(respuestaPosicion.x, respuestaPosicion.y))
    pygame.draw.rect(ventana,NEGRO,respuestaRect,2)

    if enviarBotonVisibilidad:
        pygame.draw.rect(ventana,NEGRO,enviarRectContorno,5)
        pygame.draw.rect(ventana, TEAL ,enviarRect)
        ventana.blit(enviarTexto,enviarPosicion)
    
    pygame.display.update()

#Funcion que detecta acciones en la pantalla del juego
def events_game_window():
    
    global hangmanVida
    global respuestaIngresada
    global CorrectoValido
    global numPregunta
    global run
    global numeroCorrectas
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePositionX, mousePositionY = pygame.mouse.get_pos()
            print(mousePositionX, mousePositionY)
            if enviarBotonVisibilidad:
                #Coordenadas del Boton: (486, 658) (664, 658)
                #                       (486, 689) (664, 689)
                if (mousePositionX > 486 and mousePositionX < 664):
                    if (mousePositionY > 658 and mousePositionY < 689):
                        #enviarBotonVisibilidad = False
                        print("Borrar Boton")
                        if (float(respuestaIngresada) == respuestaCorrecta):
                            respuestaIngresada = ''
                            CorrectoValido = 1
                        else:
                            hangmanVida += 1
                            respuestaIngresada = ''
                            CorrectoValido = 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                respuestaIngresada = respuestaIngresada[:-1]
            elif event.key <= 127:
                respuestaIngresada += chr(event.key)
                print(respuestaIngresada)
        
    
    if (CorrectoValido == 1):
        print("CORRECTO!")
        numPregunta += 1
        numeroCorrectas += 1
        print("Numero de pregunta: ",numPregunta)
        print("Numero de vidas: ", 6-hangmanVida)
        print("Numero de preguntas correctas respuesondidas: ", numeroCorrectas)
        display_respuesta_window("CORRECTO!")
        
            
    elif (CorrectoValido == 2):
        print("INCORRECTO :(")
        numPregunta += 1
        print("Numero de pregunta: ",numPregunta)
        print("Numero de vidas: ", 6-hangmanVida)
        print("Numero de preguntas correctas respuesondidas: ", numeroCorrectas)
        display_respuesta_window("INCORRECTO")

#Funcion para cuando enviaste el resultado
def display_respuesta_window(mensaje):
    
    global CorrectoValido
    global problemSetValidity

    ventana.fill(BLANCO)

    tituloRespuestaTexto = mensajeFinalFont.render(mensaje,True,NEGRO)
    subtituloRespuestaTexto = subtitoFont.render("LA SOLUCION DEL PROBLEMA ES LA SIGUIENTE: ", True, GRISOSCURO)
    parrafoTexto1 = parrafoFont.render(cadenaProblemaParrafo1, True, GRISOSCURO)
    parrafoTexto2 = parrafoFont.render(cadenaProblemaParrafo2, True, GRISOSCURO)
    parrafoTexto3 = parrafoFont.render(cadenaProblemaParrafo3, True, GRISOSCURO)
    parrafoTexto4 = parrafoFont.render(cadenaProblemaParrafo4, True, GRISOSCURO)
    parrafoTexto5 = parrafoFont.render(cadenaProblemaParrafo5, True, GRISOSCURO)
    resueltoTexto1 = resueltoFont.render(cadenaProblemaResueltoParrafo1, True, GRISOSCURO)
    resueltoTexto2 = resueltoFont.render(cadenaProblemaResueltoParrafo2, True, GRISOSCURO)
    resueltoTexto3 = resueltoFont.render(cadenaProblemaResueltoParrafo3, True, GRISOSCURO)
    resueltoTexto4 = resueltoFont.render(cadenaProblemaResueltoParrafo4, True, GRISOSCURO)
    respuestaResuletoTexto = respuestaResueltoFont.render(cadenaProblemaRespuestaResuletoParrafo, True, NEGRO)
    instruccionRespuestaTexto = instruccionFont.render("SI DESEAS CONTINUAR PRESIONA CUALQUIER TECLA", True, GRISOSCURO)

    tituloRespuestaPosicion = tituloRespuestaTexto.get_rect()
    subtituloRespuestaPosicion = subtituloRespuestaTexto.get_rect()
    parrafoPosicion1 = parrafoTexto1.get_rect()
    parrafoPosicion2 = parrafoTexto2.get_rect()
    parrafoPosicion3 = parrafoTexto3.get_rect()
    parrafoPosicion4 = parrafoTexto4.get_rect()
    parrafoPosicion5 = parrafoTexto5.get_rect()
    resueltoPosicion1 = resueltoTexto1.get_rect()
    resueltoPosicion2 = resueltoTexto2.get_rect()
    resueltoPosicion3 = resueltoTexto3.get_rect()
    resueltoPosicion4 = resueltoTexto4.get_rect()
    respuestaResuletoPosicion = respuestaResuletoTexto.get_rect()
    instruccionRespuestaPosicion = instruccionRespuestaTexto.get_rect()

    tituloRespuestaPosicion.center = (ANCHO/2,ALTURA-(ALTURA-50))
    subtituloRespuestaPosicion.center = (ANCHO/2, ALTURA-(ALTURA-100))
    parrafoPosicion1.center = (ANCHO/2,150)
    parrafoPosicion2.center = (ANCHO/2,175)
    parrafoPosicion3.center = (ANCHO/2,200)
    parrafoPosicion4.center = (ANCHO/2,225)
    parrafoPosicion5.center = (ANCHO/2,250)
    resueltoPosicion1.center = (ANCHO/2,285)
    resueltoPosicion2.center = (ANCHO/2,310)
    resueltoPosicion3.center = (ANCHO/2,335)
    resueltoPosicion4.center = (ANCHO/2,360)
    respuestaResuletoPosicion.center = (ANCHO/2,425)
    instruccionRespuestaPosicion.center = (ANCHO/2,ALTURA-70)


    ventana.blit(tituloRespuestaTexto,tituloRespuestaPosicion)
    ventana.blit(subtituloRespuestaTexto,subtituloRespuestaPosicion)
    ventana.blit(parrafoTexto1,parrafoPosicion1)
    ventana.blit(parrafoTexto2,parrafoPosicion2)
    ventana.blit(parrafoTexto3,parrafoPosicion3)
    ventana.blit(parrafoTexto4,parrafoPosicion4)
    ventana.blit(parrafoTexto5,parrafoPosicion5)
    ventana.blit(resueltoTexto1,resueltoPosicion1)
    ventana.blit(resueltoTexto2,resueltoPosicion2)
    ventana.blit(resueltoTexto3,resueltoPosicion3)
    ventana.blit(resueltoTexto4,resueltoPosicion4)
    ventana.blit(respuestaResuletoTexto,respuestaResuletoPosicion)
    ventana.blit(imagenes[hangmanVida],(ANCHO/2 - 70,ALTURA-300))
    ventana.blit(instruccionRespuestaTexto,instruccionRespuestaPosicion)

    pygame.display.update()

    continuarValido = True
    while continuarValido:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
                continuarValido = False
                problemSetValidity = False
    
    CorrectoValido = 0

#Funcion de pantalla final
def resultados_game_window():
    
    global run
    global hangmanVida
    global imagenes

    ventana.fill(BLANCO)

    tituloResultadosFinalTexto = mensajeFinalFont.render("TUS RESULTADOS FUERON:", True, NEGRO)
    correctasResultadosFinalTexto = resultadosParrafoFont.render("Numero de respuestas contestadas correctamente:               " + str(numeroCorrectas), True, GRISOSCURO)
    incorrectasResultadosFinalTexto = resultadosParrafoFont.render("Numero de respuestas contestadas incorrectas:                 " + str(6-numeroCorrectas), True, GRISOSCURO)
    promedioResultadosFinalTexto = resultadosParrafoFont.render("Calificacion:              " + str(round(numeroCorrectas*100/6,2)), True, GRISOSCURO)
    instruccionPortadaTexto = instruccionFont.render("PARA SALIR PRESIONA CUALQUIER TECLA", True, GRISOSCURO)

    tituloResultadosFinalPosicion = tituloResultadosFinalTexto.get_rect()
    correctasResultadosFinalPosicion = correctasResultadosFinalTexto.get_rect()
    incorrectasResultadosFinalPosicion = incorrectasResultadosFinalTexto.get_rect()
    promedioResultadosFinalPosicion = promedioResultadosFinalTexto.get_rect()
    instruccionPortadaPosicion = instruccionPortadaTexto.get_rect()

    tituloResultadosFinalPosicion.center = (ANCHO/2,ALTURA-(ALTURA-60))
    correctasResultadosFinalPosicion.center = (ANCHO/2,ALTURA-250)
    incorrectasResultadosFinalPosicion.center = (ANCHO/2,ALTURA-200)
    promedioResultadosFinalPosicion.center = (ANCHO/2,ALTURA-120)
    instruccionPortadaPosicion.center = (ANCHO/2,ALTURA-30)

    ventana.blit(tituloResultadosFinalTexto,tituloResultadosFinalPosicion)
    ventana.blit(imagenes[hangmanVida],(ANCHO/2 - 70,200))
    ventana.blit(correctasResultadosFinalTexto, correctasResultadosFinalPosicion)
    ventana.blit(incorrectasResultadosFinalTexto,incorrectasResultadosFinalPosicion)
    ventana.blit(promedioResultadosFinalTexto,promedioResultadosFinalPosicion)
    ventana.blit(instruccionPortadaTexto,instruccionPortadaPosicion)

    pygame.display.update()

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN or event.type == pygame.QUIT):
            pygame.quit()
            run = False



############ MAIN JUEGO ############
#iniciliza el loop del juego 
while run:
    
    clock.tick(FPS)

    if (numPregunta == 0):
        display_portada()

    elif (numPregunta > 6):
        resultados_game_window()
    
    else:
        set_problem(numPregunta)
        display_game_window()
        events_game_window()

pygame.quit()