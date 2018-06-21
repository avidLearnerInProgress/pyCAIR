from setuptools import setup

with open('Readme.txt') as file:
    long_description = file.read()

REQUIREMENTS = ['natsort', 'os', 'opencv-python', 'pathlib', 'sys', 'argparse', 'numpy', 'scipy', 'tqdm']

setup(
  name = 'pyCAIR',
  packages = ['pyCAIR'],
  version = '0.1.4',
  description = ' This module provides a simple yet powerful mechanism to resize images using Seam Carving Algorithm.',
  long_description = long_description,
  author = 'Chirag Shah',
  author_email = 'chiragshah9696@gmail.com',
  url = 'https://github.com/avidLearnerInProgress/pyCAIR',
  download_url = 'https://github.com/avidLearnerInProgress/pyCAIR/archive/0.1.tar.gz',
  install_requires = REQUIREMENTS,
  license = 'GPL-3.0',
  keywords = 'python openCV image-processing dynamic-programming',
  classifiers = [],
)