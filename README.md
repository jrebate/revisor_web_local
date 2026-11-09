# Revisor de web local

Pega la web de un negocio local y obtén una ficha de una página (vista en móvil, velocidad, botón de llamar, legibilidad y lo que ve Google) con la API de Google PageSpeed Insights. Herramienta de CentaurUX.

- HTML estático, sin dependencias. Se publica con GitHub Actions (Settings > Pages > Source: GitHub Actions).
- La clave de PageSpeed Insights va en el secreto de Actions PSI_KEY; la Action la mete en index.html al publicar. Está limitada por referer a https://jrebate.github.io/* y solo a la API de PageSpeed Insights.
- Medición con GoatCounter (jrebate): eventos con prefijo web-.

Resultados orientativos: no es una auditoría ni certifica nada.

Creado por Jorge Rebate Serrano · Licencia CC BY 4.0.
