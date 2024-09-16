import pandas as pd

temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 21}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 24}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 22}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 24}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 27}
        ]
    ]
]

# Diccionario para almacenar los promedios por ciudad y semana
promedios = {}

# Bucle para calcular el promedio por ciudad y semana
for ciudad_index, ciudad in enumerate(temperaturas):
    ciudad_nombre = f"Ciudad {ciudad_index + 1}"
    promedios[ciudad_nombre] = []

    for semana_index, semana in enumerate(ciudad):
        suma_temperaturas = sum(dia["temp"] for dia in semana)
        promedio_semana = suma_temperaturas / len(semana)

        # Guardar el promedio de la semana
        promedios[ciudad_nombre].append(promedio_semana)

# Crear un DataFrame con los promedios
df_promedios = pd.DataFrame(promedios, index=[f"Semana {i + 1}" for i in range(len(temperaturas[0]))])

# Mostrar los resultados
print(df_promedios)