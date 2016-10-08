import time
import webbrowser

navegador = webbrowser.get('google-chrome')
espera = input("Ingrese tiempo de espera(segundos): ")
while(True):
	time.sleep(espera)
	navegador.open_new("https://www.youtube.com/watch?v=4JkIs37a2JE")
