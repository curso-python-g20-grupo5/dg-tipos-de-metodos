# Proyecto Juego Gran Fantasía

Este programa desarrolla la primera escena de su próximo juego “Gran Fantasía”. El prototipo debe desarrollarse utilizando una aplicación de consola escrita en Python, que conste de un script principal que ejecute el juego, y una clase que permita crear personajes, que debe ser importada en el script principal. Las opciones de juego del usuario, así como el nombre de su personaje, se deben solicitar mediante input.
La clase que permite crear personajes debe considerar lo siguiente:

● Cada personaje tiene un nombre, el cual debe ser especificado al momento de crear
un personaje.

● Cada personaje recién creado tiene nivel 1 y experiencia 0 (estos son los únicos valores posibles al momento de crear un personaje).

● A cada personaje es posible consultarle o asignarle un estado. Al solicitar el estado de un personaje, se debe mostrar en pantalla su nombre, su nivel y su experiencia. Al asignar un valor al estado, este valor corresponderá a la experiencia recibida por el personaje. Según la experiencia recibida, se debe modificar la experiencia actual del personaje y su nivel de acuerdo a lo siguiente:

    ○ Los valores posibles de experiencia son entre 0 y 99 inclusive.

    ○ El nivel mínimo es 1 y no hay máximo.

    ○ Cada 100 puntos de experiencia recibidos, el personaje sube 1 nivel (su nivel
    aumenta en 1)

## Archivos del Proyecto

- [`personaje.py`]: Implementa la clase `personaje`, que representa a un usuario en el juego.
- [`juego.py`]: Implementa la lógica principal del juego, donde el usuario se enfrenta al orco.

## Cambios realizados

[`personaje.py`]:

- Cambio en self.expriencia = 0
- Cambio en `@propeerty en EXP: {self.experiencia}`
- Cambio en `def estado(self, exp)`, donde se integran los siguientes cambios:

  ```
          self.nivel += 1
          tmp_exp -= 100

      while tmp_exp < 0 and self.nivel > 1:
          self.nivel -= 1
          tmp_exp += 100

      self.experiencia = max(0, tmp_exp)
  ```

- Cambio en el contenido de `return` del contructor `__lt__`:

  ```
  return self.nivel < other.nivel
  ```

- Cambio en el contenido de `return` del contructor `__gt__`:
  ```
  return self.nivel > other.nivel
  ```
- Cambio en el contenido de `return` del contructor `__eq__`:
  ```
  return self.nivel == other.nivel
  ```
- En el método `get_probabilidad_ganar` se cambian los valores de los return pertenecientes a `if`, `elif`, `else`. Donde se deben retornar los valores 0.66 para if, 0.33 para elif, y 0.5 para else.

- En el método estático de la función `mostrar_dialogo_opcion` se agregaron cambios en el texto que se debe retornar ante las acciones tomadas por el jugador.
  Planteandose de la siguiente manera a nivel de código:

```
def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de perder contra el Orco.\n"
                                "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
                "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n"
                "2. Huir\n"
            )
        )
```

[`juego.py`]:

- Cambio de nombre del input de orco a personaje
- Cambio de nombre en print, de Elfo a Orco
- Se añade " faltante en resultado
- Se cambia condición del if resultado de P a G
- Se actualizan valores de experiencia perdida o ganada
- Se corrige error de tipeo en print
- Se corrige parametro de metodo get_probabilidad_ganar de 0 a o
- Se corrige parametro de metodo mostrar_dialogo_opcion de provabilidad_ganar a probabilidad_ganar
- Se añade print para opcion Huir

## Uso

### Ejecución del Script Principal

Para ejecutar el script principal [`juego.py`], simplemente ejecute el siguiente comando en su terminal:

```bash
python juego.py
```

El script le pedirá que ingrese el nombre de su personaje.

## Ejemplo de Uso

```
¡Bienvenido a Gran Fantasía!
Por favor indique nombre de su personaje:
Evil666
NOMBRE: Evil666 NIVEL: 1 EXP: 0
¡Oh no!, ¡Ha aparecido un Orco!
Con tu nivel actual, tienes 50.0% de probabilidades de ganarle al Orco.
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
¿Qué deseas hacer?
1. Atacar
2. Huir
1
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!
NOMBRE: Evil666 NIVEL: 1 EXP: 50
NOMBRE: Orco NIVEL: 1 EXP: 0
```

## Requisitos

- Python 3.x

## Instalación

1. Clone el repositorio:

```bash
git clone https://github.com/curso-python-g20-grupo5/dg-tipos-de-metodos.git
```

2. Navegue al directorio del proyecto:

```bash
cd dg-tipos-de-metodos
```

3. Ejecute los scripts según las instrucciones en la sección de Uso.

## Contribución

Si desea contribuir a este proyecto, por favor haga un fork del repositorio y envíe un pull request con sus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo `LICENSE` para obtener más detalles.

---

## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)

⌨️ con ❤️ por el Grupo 5 - G20 😊
