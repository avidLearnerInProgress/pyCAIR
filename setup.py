from distutils.core import setup
import setuptools

with open('README.rst') as file:
    long_description = file.read()

python_requires = '>3.4'
    
setup(
  name = 'pyCAIR',
  packages = ['pyCAIR'],
  version = '0.1.11',
  description = ' This module provides a simple yet powerful mechanism to resize images using Seam Carving Algorithm.',
  long_description = long_description,
  long_description_content_type="text/markdown",
  author = 'Chirag Shah',
  author_email = 'chiragshah9696@gmail.com',
  url = 'https://github.com/avidLearnerInProgress/pyCAIR',
  download_url = 'https://github.com/avidLearnerInProgress/pyCAIR/archive/0.1.tar.gz',
  license = 'GPL-3.0',
  keywords = ['python', 'openCV', 'image-processing', 'dynamic-programming', 'seam-carving'],
  classifiers = [],
)