"""
Created by kardantel at 9/6/2020
__author__ = 'Carlos Pimentel'
__email__ = 'carlosdpimenteld@gmail.com'
"""

import warnings
from utils import Utils
from model import NBC
warnings.filterwarnings('ignore')

utils = Utils()


def main():
    '''
    Main function.
    '''
    print("Training the model...")
    female = utils.fromCSVtoArray('./in/female_names.csv', 'female')
    male = utils.fromCSVtoArray('./in/male_names.csv', 'male')
    data = female + male
    # To save, uncomment the following line:
    # np.save('./out/names.npy', data)

    data_augmented2 = utils.dataAugmentation2(data)
    # To save, uncomment the following line:
    # np.save('./out/dataAugmented.npy', data_augmented2)

    model = NBC(data_augmented2)

    while True:
        opcion = str(input('''
      What do you want to do?

        [P]redict name
        [e]xit
        '''))

        if opcion == 'P':
            name = str(input("Enter the name: "))
            model.prediction(name)
        elif opcion == 'e':
            print('Thanks and goodbye.')
            break
        else:
            print('Command not found!')


if __name__ == "__main__":
    main()
