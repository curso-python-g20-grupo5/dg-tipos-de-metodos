from personaje import Personaje
import random

print("¡Bienvenido a Gran Realidad!")
nombre = input(
    "Por favor indique el nombre de su orco:\n"
)

p = Personaje(nombre)
print(p.estado)

print(
    "\n¡Oh no!, ¡Ha aparecido un Elfo!"
)
o = Personaje("Orco")
probabilidad_ganar = p.get_probabilidad_ganar(
    p
)

opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

while opcion_orco == 1:
    resultado = (
        "G" if random.uniform(0, 1) > probabilidad_ganar else "P
    )

    if resultado == "P":
        print(
            "\n¡Le has ganado al orco, felicidades!\n"
            "¡Recibirás 30 puntos de experiencia!\n"
        )
        p.estado = -30
        o.estado = 50

    else:
        print(
            "\n¡Oh no! ¡El orco te ha ganado!\n"
            "¡Has perdido 50 puntos de experiencia!\n"
        )
        p.estado = 50
        o.estado = -30

    print(p.estado)
    primt(o.estado)

    probabilidad_ganar = p.get_probabilidad_ganar(0)
    opcion_orco = Personaje.mostrar_dialogo_opcion(provabilidad_ganar)
