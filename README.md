# zapping

Consulta el watchlist de [letterboxd](https://www.letterboxd.com) de un usuario y para cada película muestra en qué servicios de streaming está disponible.

## Uso

Ejecutar `pip install -r requirements.txt` para instalar las dependencias del script. Luego, exportar desde letterboxd el watchlist de un usuario. Es un archivo csv, **lo tienen que guardar como `watchlist.csv`**.

El output por defecto (`python3 zapping.py`) es el siguiente:

```bash
Usage: zapping.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  movie      Mostrar resultados agrupados por película.
  streaming  Mostrar resultados agrupados por streaming.
```

Se puede pedir que se muestren los resultados por película:

```bash
➜  zapping git:(main) ✗ python3 zapping.py movie
Cargando películas en la base de datos
Título: Los sonámbulos
Disponible en: ['Amazon Prime Video' 'Movistar Play']
Título: Los siete samuráis
Disponible en: ['QubitTV']
Título: Barrio Chino
Disponible en: ['Apple TV' 'Google Play']
Título: 12 hombres sin piedad
Disponible en: ['Apple TV' 'Google Play' 'QubitTV']
Título: Mundo Fantasma
Disponible en: ['QubitTV']
Título: Juegos salvajes
Disponible en: ['Apple TV' 'Google Play' 'HBO Max']
Título: Annie Hall
Disponible en: ['Apple TV' 'Google Play']
```

O por servicio:
```bash
➜  zapping git:(main) ✗ python3 zapping.py streaming
Cargando películas en la base de datos
Amazon Prime Video
    -> Los sonámbulos
    -> Tiempo de revancha
    -> 007: Casino Royale
Movistar Play
    -> Los sonámbulos
    -> Tiempo de revancha
    -> 007: Casino Royale
QubitTV
    -> Los siete samuráis
    -> 12 hombres sin piedad
    -> Mundo Fantasma
    -> Senderos de gloria
```

## TODO
- [ ] Consultar el watchlist de un usuario mediante la API de letterboxd.
- [ ] Proveer distintos tipos de filtros (sin filtro, por película, por streaming)
- [ ] Probar distintas salidas a pantalla
- [ ] Manejar los errores de todos los pasos anteriores