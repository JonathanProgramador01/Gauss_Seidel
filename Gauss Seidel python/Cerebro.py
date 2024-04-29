
class Brain:
    def __init__(self,lista):
        self.lista = lista
        self.flag = 0
        self.iteraciones = {
            "X": [0],
            "Y": [0],
            "Z": [0]

        }

    def acomodar(self):
        def swap(num):
            for i in range(0, 3):
                if abs(self.lista[num][num]) < abs(self.lista[i][num]):
                    temp = self.lista[i]
                    self.lista[i] = self.lista[num]
                    self.lista[num] = temp
                    self.flag += 1
        swap(0)
        swap(1)
        print(self.lista)
        return self.flag


    def obtener_iteraciones(self,numdeiteraciones):

        for i in range(numdeiteraciones):
            x = ((self.lista[0][3]) + (self.lista[0][1] * -1 * self.iteraciones["Y"][i]) +
                 (self.lista[0][2] * -1 * self.iteraciones["Z"][i])) / \
                self.lista[0][0]

            y = ((self.lista[1][3]) + (self.lista[1][0] * -1 * self.iteraciones["X"][i]) +
                 (self.lista[1][2] * -1 *self.iteraciones["Z"][i])) / \
                self.lista[1][1]

            z = ((self.lista[2][3]) + (self.lista[2][0] * -1 * self.iteraciones["X"][i]) +
                 (self.lista[2][1] * -1 * self.iteraciones["Y"][i])) / \
                self.lista[2][2]

            self.iteraciones["X"].append(x)
            self.iteraciones["Y"].append(y)
            self.iteraciones["Z"].append(z)
        return self.iteraciones


