from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException

class Elevador(AbstractElevador):
    def __init__(self, capacidade, total_pessoas, total_andares_predio, andar_atual):
        self.__capacidade = capacidade
        self.__total_pessoas= total_pessoas       
        self.__total_andares_predio = total_andares_predio
        self.__andar_atual = andar_atual
    
    @property
    def capacidade(self) -> int:
    	return self.__capacidade

    @property
    def total_pessoas(self) -> int:
        return self.__total_pessoas
    
    @property
    def total_andares_predio(self) -> int:
    	return self.__total_andares_predio
    
    @property
    def andar_atual(self) -> int:
    	return self.__andar_atual
    
    @total_andares_predio.setter
    def total_andares_predio(self, total_andares_predio: int):
    	self.__total_andares_predio = total_andares_predio
	
    def subir(self):
	    if self.__andar_atual == self.__total_andares_predio:
		    raise ElevadorJahNoUltimoAndarException
	def descer(self):
	    if self.__andar_atual == 0:
		    raise ElevadorJahNoTerreoException
	def entra_pessoa(self):
	    if self.__capacidade <= self.__total_pessoas:
		    raise ElevadorCheioException
	def sai_pessoa(self):
	    if self.__total_pessoas == 0:
		    raise ElevadorJahVazioException