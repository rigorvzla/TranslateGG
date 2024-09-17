from googletrans import Translator
import sys

def Traduccion(texto):
        translator = Translator()
        return translator.translate(texto, dest='es').text

print(Traduccion(sys.argv[1]))