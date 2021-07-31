import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


class Utils:
    '''
    Class that contains auxiliar methods used by the classifier.
    '''
    @classmethod
    def fromCSVtoArray(cls, dataPath, genre):
        '''
        Convert CSV files to array.
        '''
        x_names = pd.read_csv(dataPath)
        x_names = x_names.dropna(axis=0)
        x_names = x_names['name']
        x_names = np.asarray(x_names)

        return [(name, genre) for name in x_names]

    @classmethod
    def ultimaLetra(cls, nombre):
        '''
        Solo utiliza la ultima letra.
        '''
        atrib = {}
        atrib["ultima_letra"] = nombre[-1].lower()

        return atrib

    @classmethod
    def atributos(cls, nombre):
        '''
        Primera y ultima letra.
        '''
        atrib = {}
        atrib["primera_letra"] = nombre[0].lower()
        atrib["ultima_letra"] = nombre[-1].lower()

        return atrib

    @classmethod
    def atributos1(cls, nombre):
        '''
        Primer y ultima letra, conteo de cuantas letras, y si contiene o no
        una letra.
        '''
        atrib = {}
        atrib["primera_letra"] = nombre[0].lower()
        atrib["ultima_letra"] = nombre[-1].lower()
        for letra in 'abcdefghijklmnopqrstuvwxyz':
            atrib["count({})".format(letra)] = nombre.lower().count(letra)
            atrib["has({})".format(letra)] = (letra in nombre.lower())

        return atrib

    @classmethod
    def atributos2(cls, nombre):
        '''
        Separa los nombres con split(' '), para trabajar con el segundo nombre
        en caso de que lo tenga. Aplica las mismas funciones que atributos1
        pero almacena tanto del segundo como el primer nombre.
        '''
        primerSegundoNombre = nombre.split(' ')

        atrib = {}
        for i in range(len(primerSegundoNombre)):
            atrib["primera_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower()
            atrib["ultima_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower()
            for letra in 'abcdefghijklmnopqrstuvwxyz':
                atrib["count({})_{}".format(letra, i + 1)
                      ] = primerSegundoNombre[i].lower().count(letra)
                atrib["has({})_{}".format(letra, i + 1)
                      ] = (letra in primerSegundoNombre[i].lower())

        return atrib

    @classmethod
    def atributos3(cls, nombre):
        '''
        Utiliza la misma logica que atributos2, solo que en vez de analizar
        todas las letras del abecedario, recorre solamente las vocales.
        '''
        primerSegundoNombre = nombre.split(' ')

        atrib = {}
        for i in range(len(primerSegundoNombre)):
            atrib["primera_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower()
            atrib["ultima_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower()
            for letra in 'aeiou':
                atrib["count({})_{}".format(letra, i + 1)
                      ] = primerSegundoNombre[i].lower().count(letra)
                atrib["has({})_{}".format(letra, i + 1)
                      ] = (letra in primerSegundoNombre[i].lower())
        return atrib

    @classmethod
    def atributos4(cls, nombre):
        '''
        Utiliza la misma logica que atributos3, pero agrega atributos que
        describen si la primera y si la ultima letra es vocal en el primer y
        segundo nombre.
        '''
        primerSegundoNombre = nombre.split(' ')

        atrib = {}
        for i in range(len(primerSegundoNombre)):
            atrib["primera_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower()
            atrib["primera_letra_vocal_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower() in 'aieou'
            atrib["ultima_letra_vocal_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower() in 'aieou'
            atrib["ultima_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower()
            for letra in 'aeiou':
                atrib["count({})_{}".format(letra, i + 1)
                      ] = primerSegundoNombre[i].lower().count(letra)
                atrib["has({})_{}".format(letra, i + 1)
                      ] = (letra in primerSegundoNombre[i].lower())
        return atrib

    @classmethod
    def atributos5(cls, nombre):
        '''
        Utiliza lo mismo que atributos4, solo que indica si tiene un
        segundo nombre.
        '''
        primerSegundoNombre = nombre.split(' ')

        atrib = {}
        atrib["segundo_nombre"] = len(primerSegundoNombre) > 1
        for i in range(len(primerSegundoNombre)):
            atrib["primera_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower()
            atrib["primera_letra_vocal_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower() in 'aieou'
            atrib["ultima_letra_vocal_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower() in 'aieou'
            atrib["ultima_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower()
            for letra in 'aeiou':
                atrib["count({})_{}".format(letra, i + 1)
                      ] = primerSegundoNombre[i].lower().count(letra)
                atrib["has({})_{}".format(letra, i + 1)
                      ] = (letra in primerSegundoNombre[i].lower())
        return atrib

    @classmethod
    def atributos6(cls, nombre):
        '''
        Utiliza lo mismo que atributos4, solo que indica la longitud de
        los nombres.
        '''
        primerSegundoNombre = nombre.split(' ')
        atrib = {}
        for i in range(len(primerSegundoNombre)):
            atrib["longitud_{}.format(i + 1)"] = len(primerSegundoNombre[i])
            atrib["primera_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower()
            atrib["primera_letra_vocal_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower() in 'aieou'
            atrib["ultima_letra_vocal_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower() in 'aieou'
            atrib["ultima_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower()
            for letra in 'aeiou':
                atrib["count({})_{}".format(letra, i + 1)
                      ] = primerSegundoNombre[i].lower().count(letra)
                atrib["has({})_{}".format(letra, i + 1)
                      ] = (letra in primerSegundoNombre[i].lower())
        return atrib

    @classmethod
    def atributos7(cls, nombre):
        '''
        Utiliza la misma informacion que atributos4, pero agrega informacion
        referente a las 4 ultimas letras del primer nombre y del segundo nombre
        '''
        primerSegundoNombre = nombre.split(' ')
        atrib = {}
        for i in range(len(primerSegundoNombre)):
            atrib["ultimas_4_letras_{}".format(
                i + 1)] = primerSegundoNombre[i][-1:-5:-1].lower()
            atrib["primera_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower()
            atrib["primera_letra_vocal_{}".format(
                i + 1)] = primerSegundoNombre[i][0].lower() in 'aieou'
            atrib["ultima_letra_vocal_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower() in 'aieou'
            atrib["ultima_letra_{}".format(
                i + 1)] = primerSegundoNombre[i][-1].lower()
            for letra in 'aeiou':
                atrib["count({})_{}".format(letra, i + 1)
                      ] = primerSegundoNombre[i].lower().count(letra)
                atrib["has({})_{}".format(letra, i + 1)
                      ] = (letra in primerSegundoNombre[i].lower())
        return atrib

    @classmethod
    def dataAugmentation(cls, newData):
        '''
        Increase our data, so the model can have much more training data.
        It goes through the dataset in such a way that if the full name is made
        up of two names, we could have two more data. For example: "Ana
        Patricia", we could have: "Ana", "Patricia" and "Ana Patricia".

        ## Parameters
        newData: array-like of shape (n_samples, n_features)
            Contains the information of male and female names.
        '''
        for (n, g) in newData:
            primerYSegundoNombre = n.split(" ")
            segundoNombre = len(primerYSegundoNombre) > 1

            if segundoNombre:
                newData = np.append(
                    newData, [(primerYSegundoNombre[0], g)], axis=0)
                newData = np.append(
                    newData, [(primerYSegundoNombre[1], g)], axis=0)

        return newData

    @classmethod
    def dataAugmentation2(cls, newData):
        '''
        Increase our data, so the model can have much more training data.
        It performs the same techniques as the previous one, only that it
        alternates the first and second names, in such a way that if you have
        "Ana Patricia", you would have, in addition to the previous ones
        generated by the previous function, you would also have "Patricia Ana"
        with the same label.

        ## Parameters
        newData: array-like of shape (n_samples, n_features)
            Contains the information of male and female names.
        '''
        for (n, g) in newData:
            primerYSegundoNombre = n.split(" ")
            segundoNombre = len(primerYSegundoNombre) > 1

            if segundoNombre:
                if not primerYSegundoNombre[0] in newData[0]:
                    newData = np.append(
                        newData, [(primerYSegundoNombre[0], g)], axis=0)

                if not primerYSegundoNombre[1] in newData[0]:
                    newData = np.append(
                        newData, [(primerYSegundoNombre[1], g)], axis=0)

                if not primerYSegundoNombre[1] + primerYSegundoNombre[0] in newData[0]:
                    newData = np.append(
                        newData, [(primerYSegundoNombre[1] + primerYSegundoNombre[0], g)], axis=0)

        return newData
