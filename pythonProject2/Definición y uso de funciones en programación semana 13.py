def calcular_promedio_ciudades(temperaturas):
    promedios = {}

    # Bucle para calcular el promedio por ciudad
    for ciudad_index, ciudad in enumerate(temperaturas):
        suma_temperaturas = 0
        total_dias = 0

        # Recorrer cada semana de la ciudad
        for semana in ciudad:
            # Sumar todas las temperaturas diarias de la semana
            for dia in semana:
                suma_temperaturas += dia["temp"]
                total_dias += 1

        # Calcular el promedio de la ciudad
        promedio_ciudad = suma_temperaturas / total_dias
        promedios[f"Ciudad {ciudad_index + 1}"] = promedio_ciudad

    return promedios


# Datos de temperaturas para 4 semanas con valores entre 18 y 34 grados Celsius
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 34}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 34}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 33}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ]
    ]
]

# Llamamos a la función para calcular el promedio de temperaturas
promedios = calcular_promedio_ciudades(temperaturas)

# Imprimir los resultados
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f}°C")