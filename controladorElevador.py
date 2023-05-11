from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException


class ControladorElevador(AbstractControladorElevador):
    def __init__(self, capacidade, total_andares, andar_atual, total_pessoas):
        self.__capacidade = capacidade
        self.__total_andares = total_andares
        self.__andar_atual = andar_atual
        self.__total_pessoas = total_pessoas
