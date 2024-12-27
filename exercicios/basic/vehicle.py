class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def info(self):
        print(f"O veiculo eh da {self.marca} e seu modelo eh {self.modelo}")


class Carro(Veiculo): # heranca
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
    
    def info(self): # polimorfismo <- metodos com mesmo nome
        print(f"Carro: {self.marca} {self.modelo}, possui {self.portas} portas")


veiculo = Veiculo("Chevrolet", "Corsa")
veiculo.info()

carro =  Carro("Toyota", "Hilux", 4)
carro.info()