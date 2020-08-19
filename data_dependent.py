#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='data_dependent')
parser.add_argument('-f', '--file_path',
                    help="file_path",
                    default=None,
                    type=str, 
                    required=True)

args = parser.parse_args()
file_path = args.file_path

print(f'file_path: {file_path}')

df = pd.read_csv(file_path, names = ['id', 'text', 'emotion'])

print(f'unique emotions: {df.emotion.unique()}')