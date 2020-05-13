import webbrowser #lo vamos a usar para abrir el navegador
import os #leer y escribir archivos
from time import sleep
import sys #usaremos sys.exit()
from form.logo import LogoTwo, LogoCero, LogoOne #importamos nuestro logo.py
from tqdm import tqdm
from colorama import Back, Fore, init
init()

#Antes de imprimir cualquier texto, es necesario inicializar colorama.
#con init()

facebook = ("https://facebook.com/search/")

def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def Carga():
    loop = tqdm(total=50000, position=0, leave=False)
    for k in range(50000):
        loop.set_description("Loading .....".format(k))
        loop.update(1)
    loop.close()

def MenuInicial():
    os.system('clear')
    LogoCero()
    sleep(0.7)
    limpiar()
    sleep(0.3)
    LogoCero()
    sleep(0.3)
    limpiar()
    sleep(0.3)
    LogoOne()
    sleep(0.3)
    limpiar()
    sleep(0.3)
    LogoCero()
    sleep(1.5)
    sleep(0.60)
    Carga()
    print(Fore.GREEN + "\t\tBienvenido a Stalker Face\t\t")
    print("\t\t__________________________\t\t")
    print("\t\t MENU \t\t")
    print(Fore.YELLOW + "1- Acceder al Script por Opciones Separadas")
    print("2- Acceder al Script a Todas las Opciones")
    print("3- Salir del Script")




def MenuSecundario():
    LogoOne()
    print("\t\t Bienvenido a InFo-FaSe Facebook OpErs \t\t")
    print("\t\t ____________________ \t\t")
    Carga()
    print("\t\t\t Menu")
    print(Fore.BLUE + "___________________________")
    print("***PERFIL***")
    print("___________________________")
    print(Fore.WHITE + "0 - Publicaciones Propias")
    print("1 - Fotos Propias")
    print("2 - Videos Propios")
    print("3 - Grupos")
    print("4 - Eventos que asistira")
    sleep(1)
    print(Fore.BLUE + "___________________________")
    print("***ETIQUETAS***")
    print("___________________________")
    print(Fore.WHITE + "5 - Fotos etiquetadas")
    print("6 - Videos etiquetados")
    print("7 - Publicaciones etiquetadas")
    sleep(1)
    print(Fore.BLUE + "___________________________")
    print("***Comentarios realizados***")
    print("___________________________")
    print(Fore.WHITE + "8 - Fotos comentadas")
    print("9 - Videos comentados")
    print("10 - Publicaciones comentadas")
    print(Fore.BLUE + "___________________________")
    print("*** Likes***")
    print("___________________________")
    print(Fore.WHITE + "11 - LIKES en fotos")
    print("12 - LIKES en videos")
    print("13 - LIKES en publicaciones")
    print("14 - LIKES (paginas) ")
    sleep(1)
    print(Fore.BLUE + "___________________________")
    print("***LUGARES***")
    print("___________________________")
    print(Fore.WHITE + "15 - Lugares visitados")
    print("16 - friends")
    print("17 - salir")

def main():
    try:
        MenuInicial()
        inicial = int(input(Fore.CYAN + "Elige una opcion\n [ Opers Linux ] > "))

        print("Usted ha escogido la opcion", inicial)
        if inicial == 1:
            LogoOne()
            print(Fore.RESET + "Has accedido a los Stalker por separado")
            try:
                txt = open("funciones.txt", "r")
                MenuSecundario()
                opcion = int(input(Fore.BLUE + "Elige Una opcion\n [ Opers Linux ] > "))
                #print(opcion)
                for i,linea in enumerate (txt):
                    if i == opcion:
                        #print("La linea seleccionada es", linea)
                        #print("El numero es",i)
                        IdVictima = int(input(Fore.MAGENTA + "Coloca el ID DE TU VICTIMA\n [ Opers Linux ] > "))
                        url = (facebook + str(IdVictima) + linea)
                        #print(url)
                        webbrowser.open(url, new=2, autoraise=True)

                        break

                txt.close()



            except:
                LogoTwo()
                print(Fore.RED + "Algo salio mal")



        elif inicial == 2:
            LogoOne()
            print(Fore.RESET + "Has accedido a todos los Stalker")
            IdVictima = int(input(Fore.MAGENTA + "Coloca el ID DE TU VICTIMA\n [ Opers Linux ] > "))
            #print(IdVictima)
            print("Comenzando proceso en ")
            #print(3)
            #sleep(1)
            #print(2)
            #sleep(1)
            #print(1)
            print("Las siguientes Funciones se ejecutaran")
            Carga()
            try:
                txt = open("funciones.txt", "r")
                for funciones in txt:

                    #print(Fore.WHITE + funciones)
                    sleep(1)
                    url = (facebook + str(IdVictima) + funciones)
                    print(Fore.WHITE + url)
                    webbrowser.open(url, new=2, autoraise=True)
                    LogoTwo()

                txt.close()


            except:
                print("Hubo un error con el Archivo")
                LogoTwo()



        elif inicial == 3:
            LogoTwo()
            print(Fore.RED + "Saliendo del sistema")
        else:
            LogoTwo()
            print(Fore.RED + "Saliendo del sistema")












    except NameError:
        print(Fore.RED + "[Error] " + Fore.BLUE + "Opcion incorrecta debe colocar un numero entero")
        print(Fore.RED + "[Error] " + Fore.BLUE + "Espere Iniciando de nuevo el sistema")
        sleep(2)
        body()
    except SyntaxError:
        print(Fore.RED + "[Error] " + Fore.BLUE + "Opcion incorrecta debe colocar un numero entero")
        print(Fore.RED + "[Error] " + Fore.BLUE + "Espere Iniciando de nuevo el sistema")
        sleep(2)
        body()




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
