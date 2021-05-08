import numpy as np


class Matrix:
    def __init__(self, m_size, fillness=1):
        self.n, self.m = m_size
        self.fillness = fillness
        self.createNullMatrix()

    def setPixelSize(self, pixel_size):
        self.__pixel_size = pixel_size

    def prettyPrint(self):
        for row in self.__background:
            print(row)

    def createNullMatrix(self):
        self.__background = np.zeros((self.m, self.n), dtype='int')

    def getBackground(self):
        return self.__background

    def setPointByXY(self, x, y):
        corrected_n, corrected_m = x-1, y-1
        if corrected_n < self.n or corrected_m < self.m:
            self.__background[corrected_m][corrected_n] = self.fillness

    def getPixel(self):
        pixels = list()
        for m, row in enumerate(self.__background):
            for n, element in enumerate(row):
                if element == 1:
                    pixels.append((n+1, m+1))
        return pixels

if __name__ == '__main__':
    matrix = Matrix((3, 3), 1)
    matrix.prettyPrint()
    print('........')
    matrix.setPointByXY(2, 2)
    matrix.prettyPrint()
    print(matrix.getPixel())
    matrix.setPointByXY(1, 1)
    matrix.prettyPrint()
    print(matrix.getPixel())