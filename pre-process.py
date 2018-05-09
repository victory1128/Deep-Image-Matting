# -*- coding: utf-8 -*-

import zipfile
import os

if __name__ == '__main__':
    if not os.path.exists('Combined_Dataset'):
        zip_file = 'Adobe_Deep_Matting_Dataset.zip'
        print('Extracting {}...'.format(zip_file))

        zip_ref = zipfile.ZipFile(zip_file, 'r')
        zip_ref.extractall('.')
        zip_ref.close()

    if not os.path.exists('train2017'):
        zip_file = 'train2017.zip'
        print('Extracting {}...'.format(zip_file))

        zip_ref = zipfile.ZipFile(zip_file, 'r')
        zip_ref.extractall('.')
        zip_ref.close()

