from typing import List

from modelos.vehiculo import Vehiculo


class GarajeServicio:
    """Maneja la coleccion de vehiculos del garaje."""

    def __init__(self) -> None:
        self._vehiculos: List[Vehiculo] = []  # almacenamiento en memoria

    def agregar_vehiculo(self, vehiculo: Vehiculo) -> None:
        """Anade un vehiculo si la placa no existe aun."""
        if any(v.placa == vehiculo.placa for v in self._vehiculos):
            raise ValueError(f"La placa {vehiculo.placa} ya esta registrada.")
        self._vehiculos.append(vehiculo)

    def obtener_vehiculos(self) -> List[Vehiculo]:
        """Devuelve los vehiculos registrados en orden de ingreso."""
        return list(self._vehiculos)
