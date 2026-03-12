from dataclasses import dataclass


@dataclass
class Vehiculo:
    placa: str
    marca: str
    propietario: str
    color: str

    def __post_init__(self):
        # Normaliza entradas para evitar duplicados por espacios/caso
        self.placa = self.placa.strip().upper()
        self.marca = self.marca.strip().title()
        self.propietario = self.propietario.strip().title()
        self.color = self.color.strip().title()
