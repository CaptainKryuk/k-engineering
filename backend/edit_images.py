import pathlib
import os
import subprocess


def edit():
  """
  бежим по файлам
  если длина > 6, то 
  название делим на 2, после _ часть
  оставляем и делаем mv results/old_name results/new_name
  """
  for address, dirs, files in os.walk('results2'):
    for file in files:
      try:
        new_name = file.split('.')[0] + '.' + file.split('.')[2]
      except:
        new_name = ''

      if new_name:
        subprocess.call(f'mv results2/{file} results2/{new_name}', shell=True)


edit()