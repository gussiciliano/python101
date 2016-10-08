import time
import webbrowser
from time import sleep

#URL de un video de musica de youtube
url = "https://www.youtube.com/watch?v=IBH97ma9YiI"
#cantidad de minutos que tienen que transcurrir para que se abra el navegador
minutos = 1
#variable en la que se almacena el tiempo de espera final
timeout = minutos * 60

sleep(timeout)
webbrowser.open_new(url)
