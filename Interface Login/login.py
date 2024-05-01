##Libreria descargable
##tkinter sirve para hacer interfaces en python
import customtkinter 

##Apariencia:
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')


root = customtkinter.CTk()  ##Se crea la ventana principal
root.title("Login By Ivan-404-")  ## Definir el título de la ventana
root.geometry('500x500')  ##Dimension para la interface grafica

def login(): ##Funcion de logeo
    print('Bienvenido') ##Mensaje luego de logearse


##See crea un marco('frame') dentro de la ventana('root'): 
frame = customtkinter.CTkFrame(master=root)  ##Utilizando la clase CTkFrame de customtkinter


##Marco dentro de la ventana Principal con relleno de 20px en ejeY, 60px ejeX, y se expandepara llenar cuaquier espacio disponible con(expand = true)
frame.pack(pady=20, padx=60, fill='both', expand = True)


##Se crea una etiqueta (label) con el texto "Login" y se coloca dentro del marco:
label= customtkinter.CTkLabel(master=frame, text='Login') ##(creando una etiqueta al marco)
label.pack(pady=12, padx=10) ##pixeles del label (login)

##Agregar campos de entrada para el nombre de usuario y la contraseña:
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username') ##Se aplican etiquetas de marcador de posición para indicar el propósito de cada campo (placeholder_text). 
entry1.pack(pady=12, padx=10)         

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*') ##El campo de contraseña muestra asteriscos (*) en lugar de los caracteres ingresados.
entry2.pack(pady=12, padx=10)


##Se crea el boton de login y se le asigna la funcion'login()', con el 'command=login. Tambien se le puede pasar parametros a la funcion.
button = customtkinter.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)


##Iniciar el bucle principal de la interfaz de usuario:
root.mainloop() ##Esto permite que se abra la interface y que el usuario pueda interactuar.