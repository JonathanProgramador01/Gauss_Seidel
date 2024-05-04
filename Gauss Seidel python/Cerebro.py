
class Brain:
    def __init__(self, lista):
        self.lista = lista
        self.flag = 0

    def acomodar(self):
        for j in range(0, 2):
            for i in range(j + 0, 3):
                if abs(self.lista[j][j]) < abs(self.lista[i][j]):
                    temp = self.lista[i]
                    self.lista[i] = self.lista[j]
                    self.lista[j] = temp
                    print(i)
                    print(self.lista)
                    self.flag += 1
        return self.flag

    def obtener_iteraciones_de_jacobi(self, numdeiteraciones):

        iteraciones_jakobi = {
            "X": [0],
            "Y": [0],
            "Z": [0]
        }
        for i in range(numdeiteraciones):
            x = ((self.lista[0][3]) + (self.lista[0][1] * -1 * iteraciones_jakobi["Y"][i]) +
                 (self.lista[0][2] * -1 * iteraciones_jakobi["Z"][i])) / \
                self.lista[0][0]

            y = ((self.lista[1][3]) + (self.lista[1][0] * -1 * iteraciones_jakobi["X"][i]) +
                 (self.lista[1][2] * -1 * iteraciones_jakobi["Z"][i])) / \
                self.lista[1][1]

            z = ((self.lista[2][3]) + (self.lista[2][0] * -1 * iteraciones_jakobi["X"][i]) +
                 (self.lista[2][1] * -1 * iteraciones_jakobi["Y"][i])) / \
                self.lista[2][2]

            iteraciones_jakobi["X"].append(x)
            iteraciones_jakobi["Y"].append(y)
            iteraciones_jakobi["Z"].append(z)

        return iteraciones_jakobi

    def obtener_iteraciones_de_guass_seidel(self,numdeiteraciones):
        iteraciones_gauss = {
            "X":[0],
            "Y":[0],
            "Z":[0]
        }



        for i in range(numdeiteraciones):
            x = ((self.lista[0][3]) + (self.lista[0][1] * -1 * iteraciones_gauss["Y"][i]) +
                 (self.lista[0][2] * -1 * iteraciones_gauss["Z"][i])) / \
                self.lista[0][0]
            iteraciones_gauss["X"].append(x)

            y = ((self.lista[1][3]) + (self.lista[1][0] * -1 * iteraciones_gauss["X"][i+1]) +
                 (self.lista[1][2] * -1 * iteraciones_gauss["Z"][i])) / \
                self.lista[1][1]
            iteraciones_gauss["Y"].append(y)
            z = ((self.lista[2][3]) + (self.lista[2][0] * -1 * iteraciones_gauss["X"][i+1]) +
                 (self.lista[2][1] * -1 * iteraciones_gauss["Y"][i+1])) / \
                self.lista[2][2]
            iteraciones_gauss["Z"].append(z)

        return iteraciones_gauss
