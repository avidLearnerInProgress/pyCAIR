from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

python_requires = '>3.4'
    
setup(
  name = 'pyCAIR',
  packages = ['pyCAIR'],
  version = '0.1.13',
  description = ' This module provides a simple yet powerful mechanism to resize images using Seam Carving Algorithm.',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Chirag Shah',
  author_email = 'chiragshah9696@gmail.com',
  url = 'https://github.com/avidLearnerInProgress/pyCAIR',
  download_url = 'https://github.com/avidLearnerInProgress/pyCAIR/archive/0.1.tar.gz',
  license = 'GPL-3.0',
  keywords = ['python', 'openCV', 'image-processing', 'dynamic-programming', 'seam-carving'],
  classifiers = [],
)