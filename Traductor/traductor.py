from translate import Translator

translator = Translator(from_lang='spanish', to_lang='english') ##Variable que llama a Translate para traducir lo que se asigna como parametros, ejemplo: spanish, english

txt= input("que quieres traducir? : ")

res = translator.translate(txt) ##Traducimos el input txt

print(res) ##Mostramos lo traducido.