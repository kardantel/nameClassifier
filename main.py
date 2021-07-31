"""
Created by kardantel at 9/6/2020
__author__ = 'Carlos Pimentel'
__email__ = 'carlosdpimenteld@gmail.com'
"""

import warnings
import numpy as np
from utils import Utils
from model import NBC
warnings.filterwarnings('ignore')

utils = Utils()


def main():
    '''
    Main function.
    '''
    female = utils.fromCSVtoArray('./in/female_names.csv', 'female')
    male = utils.fromCSVtoArray('./in/male_names.csv', 'male')
    data = female + male
    np.save('./out/names.npy', data)

    data_augmented2 = utils.dataAugmentation2(data)
    np.save('./out/dataAugmented.npy', data_augmented2)
    # print(len(data), len(data_augmented2))

    model = NBC(data_augmented2)
    model.prediction('Carlos Daniel')
    model.prediction('Laura Melisa')


if __name__ == "__main__":
    main()
