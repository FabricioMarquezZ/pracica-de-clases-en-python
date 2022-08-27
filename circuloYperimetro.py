# creacion clase para ciruclo
class circulo:
    # metodo para captura de radio
    def capturaRad(self):
        self.capturaRad = int(input("Ingrese el radio del circulo: "))

    # metodo para calcular perimetro
    def calculoPer(self):
        self.calculoPer = 2*3.14 * self.capturaRad

    # metodo para calcular area
    def calculoArea(self):
        self.calculoArea = 3.14*(self.capturaRad*self.capturaRad)

    # metodo para mostrar los resultados
    def resultados(self):
        print(f"Perimetro= {self.calculoPer}")
        print(f"Area= {self.calculoArea}")


# creacion de clase para paralelogramo
class paralelogramo:
    # creacion de metodo para capturar base
    def captura_Base(self):
        self.captura_Base = int(input("Ingrese base: "))

    # creacion de metodo para calcular altura
    def captura_Alt(self):
        self.captura_Alt = int(input("Ingrese altura: "))

    # creacion de metodo para realizar calculos correspondientes
    def calculos(self):
        area = self.captura_Base*self.captura_Alt
        perimetro = 2*(self.captura_Alt+self.captura_Base)
        print(f"Area= {area}")
        print(f"Perimetro= {perimetro}")


# instancia y ejecucion de metodos de clase circulo
print("//////////////////////////////////////////////////////")
print("//////CALCULO DE AREA Y PERIMETRO DE UN CIRCULO///////")
print("//////////////////////////////////////////////////////")
INST_circulo = circulo()
INST_circulo.capturaRad()
INST_circulo.calculoArea()
INST_circulo.calculoPer()
INST_circulo.resultados()

# instancia y ejecucion de metodos de clase paralelogramo
print("//////////////////////////////////////////////////////////////")
print("////////CALCULO DE AREA Y PERIMETRO DE UN PARALELOGRAMO///////")
print("//////////////////////////////////////////////////////////////")
INST_paralelogramo = paralelogramo()
INST_paralelogramo.captura_Alt()
INST_paralelogramo.captura_Base()
INST_paralelogramo.calculos()
