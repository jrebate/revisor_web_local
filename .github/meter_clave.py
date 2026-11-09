"""Mete la clave de PageSpeed Insights (variable de entorno PSI_KEY) en la página que se publica."""
import os
import sys

ruta = sys.argv[1]
clave = os.environ["PSI_KEY"].strip()
texto = open(ruta, encoding="utf-8").read()
marca = 'var PSI_KEY = "";'
if texto.count(marca) != 1:
    sys.exit("No encuentro la línea de PSI_KEY en " + ruta)
open(ruta, "w", encoding="utf-8").write(texto.replace(marca, 'var PSI_KEY = "%s";' % clave))
