from parcial_turismo.model import Region
from parcial_turismo.model import Zona


regiones = [
        Region(1, "Bocas del Toro",
               "La provincia de Bocas del Toro tiene un área de 4.643,9 kilómetros cuadrados, que comprende el "
               "continente y nueve islas principales. La provincia consiste en el Archipiélago de Bocas del Toro, "
               "Bahía Almirante, Laguna de Chiriquí, y la tierra firme adyacente.",
               [
                   Zona("Archipiélago de Bocas del Toro", 1000,
                        "El archipiélago de Bocas del Toro es un grupo de islas en el mar Caribe el cual se localiza "
                        "al noroeste de la república de Panamá. Este conjunto de islas separa la bahía del Almirante "
                        "y la laguna de Chiriquí, desde la apertura del mar Caribe.",
                        "\u29BF 1 Noche\n"
                        "\u29BF Desayuno\n"
                        "\u29BF Masaje"),
                   Zona("Laguna de Chiriquí", 2000,
                        "La laguna de Chiriquí Grande es una laguna costera del mar Caribe de Panamá; puerto natural "
                        "localizado junto a la frontera sureste de Costa Rica, en la provincia de Bocas del Toro. "
                        "Está flanqueada por las puntas Térraba al noroeste, y Valiente y Chiriquí Grande en la "
                        "península Valiente al sureste.",
                        "\u29BF 3 Noche\n"
                        "\u29BF Desayuno\n"
                        "\u29BF Masaje"),
                   Zona("Isla Colón", 3000,
                        "La isla Colón es la ínsula principal del archipiélago de Bocas del Toro, situado al noroeste "
                        "de Panamá en el mar Caribe. Con una superficie de 61 km², es la isla más grande de la "
                        "provincia de Bocas del Toro y la cuarta más grande del país.",
                        "\u29BF 4 Noche\n"
                        "\u29BF Cena\n"
                        "\u29BF Viaje en barco"
                        ),
                   Zona("Parque nacional Isla Bastimentos", 4000,
                        "El Parque nacional marino Isla Bastimentos se encuentra ubicado en el Archipiélago "
                        "de Bocas del Toro al norte de la provincia del mismo nombre, cerca de la ciudad de Bocas del "
                        "Toro y la aldea indígena Ngäbe-Buglé Salt Creek. Fue creado en 1988 y cuenta "
                        "con una superficie de 13.226 hectáreas, representando el 6.6% del área total del "
                        "archipiélago.",
                        "\u29BF 6 Noche\n"
                        "\u29BF Almuerzo\n"
                        "\u29BF Ver cangrejos"
                        )
               ]),
        Region(1, "Chiriquí",
               "DESCRIPCION DEL PAIS DE CHIRIKI",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Veraguas",
               "DESCRIPCION Veraguas",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Herrera",
               "DESCRIPCION Herrera",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Los Santos",
               "DESCRIPCION Los Santos",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Coclé",
               "DESCRIPCION Coclé",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Colón",
               "DESCRIPCION Colón",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Panamá Oeste",
               "DESCRIPCION Panamá Oeste",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Panamá",
               "DESCRIPCION Panamá",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Darién",
               "DESCRIPCION Darién",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(2, "Ngöbe-Buglé",
               "DESCRIPCION Ngöbe-Buglé",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(2, "Guna Yala",
               "DESCRIPCION Guna Yala",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(2, "Emberá",
               "DESCRIPCION Emberá",
               [
                   Zona("Zona Chiriki #1", 1000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #2", 2000,
                        "DESCIPCION ZONA #2 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #3", 3000,
                        "DESCIPCION ZONA #3 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Zona Chiriki #4", 4000,
                        "DESCIPCION ZONA #4 HACER",
                        "\u0085 6 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ])
    ]


def get_regiones_list():
    return regiones


def get_o_tipo(obj):
    if isinstance(obj, Region):
        return "r"
    elif isinstance(obj, Zona):
        return "z"
    else:
        return "n"
