from autocorrect import Speller

corrector = Speller(lang='es')

def correct_text(text):
    # Dividir el texto en palabras y aplicar el corrector ortográfico a cada palabra
    palabras = text.split()
    texto_corregido = [corrector(palabra) for palabra in palabras]
    return ' '.join(texto_corregido)

texto_usuario = input("Por favor, ingrese un texto: ")
texto_corregido = correct_text(texto_usuario)

print("Texto original:", texto_usuario)
print("Texto corregido:", texto_corregido)