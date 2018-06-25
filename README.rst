.. raw:: html

   <h1 align="center">

.. raw:: html

   </h1>

pyCAIR is a content-aware image resizing(CAIR)
`library <https://pypi.org/project/pyCAIR/>`__ based on `Seam Carving
for Content-Aware Image
Resizing <http://http://graphics.cs.cmu.edu/courses/15-463/2012_fall/hw/proj3-seamcarving/imret.pdf>`__
paper.

|PyPI version| |License: GPL v3|

Table of Contents
=================

1. `How CAIR works <#how-does-it-work>`__
2. `Understanding the research
   paper <#intutive-explanation-of-research-paper>`__
3. `Project structure and
   explanation <#project-structure-and-explanation>`__
4. `Installation <#installation>`__
5. `Usage <#usage>`__
6. `Demo <#in-action>`__
7. `Screenshots <#screenshots>`__
8. `Todo <#todo>`__

How does it work
================

-  An energy map and a grayscale format of image is generated from the
   provided image.

-  Seam Carving algorithm tries to find the not so useful regions in
   image by picking up the lowest energy values from energy map.

-  With the help of Dynamic Programming coupled with backtracking, seam
   carving algorithm generates individual seams over the image using
   top-down approach or left-right approach.(depending on vertical or
   horizontal resizing)

-  By traversing the image matrix row-wise, the cumulative minimum
   energy is computed for all possible connected seams for each entry.
   The minimum energy level is calculated by summing up the current
   pixel with the lowest value of the neighboring pixels from the
   previous row.

-  Find the lowest cost seam from the energy matrix starting from the
   last row and remove it.

-  Repeat the process iteratively until the image is resized depending
   on user specified ratio.

+-----------+----------------------------------+
| |Result7| | |Result8|                        |
+===========+==================================+
| DP Matrix | Backtracking with minimum energy |
+-----------+----------------------------------+

Intutive explanation of research paper
======================================

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes1.png
       :alt: Notes1

       Notes1

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes2.png
       :alt: Notes2

       Notes2

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes3.png
       :alt: Notes3

       Notes3

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes4.png
       :alt: Notes4

       Notes4

Project structure and explanation
=================================

**Directory structure:**

| **pyCAIR** (root directory)
|   \| - images/
|   \| - results /
|   \| - sequences/ (zipped in repository)
|   \| - videos/
|   \| -
  `notdoneyet.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/notdoneyet.py>`__
|   \| -
  `imgtovideos.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/imgtovideos.py>`__
|   \| -
  `opencv_generators.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/opencv_generators.py>`__
|   \| -
  `seam_carve.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/seam_carve.py>`__
|   \| -
  `helpers.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/helpers.py>`__

**File:**
`notdoneyet.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/notdoneyet.py>`__

-  **user_input()** -
   Parameters:

   -  Alignment: Specify on which axis the resizing operation has to be
      performed.
   -  Scale Ratio: Floating point operation between 0 and 1 to scale the
      output image.
   -  Display Seam: If this option isn’t selected, the image is only
      seamed in background.
   -  Input Image
   -  Generate Sequences: Generate intermediate sequences to form a
      video after all the operations are performed.

**File:**
`imgtovideos.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/imgtovideos.py>`__

-  **generateVideo()** - pass each image path to **vid()** for video
   generation.

-  **vid()**- writes each input image to video buffer for creating a
   complete video.

**File:**
`opencv_generators.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/opencv_generators.py>`__

-  **generateEnergyMap()** - utilised OpenCV inbuilt functions for
   obtaining energies and converting image to grayscale.

-  **generateColorMap()** - utilised OpenCV inbuilt functions to
   superimpose heatmaps on the given image.

**File:**
`seam_carve.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/seam_carve.py>`__

-  **getEnergy()** - generated energy map using sobel operators and
   convolve function.

-  **getMaps()** - implemented the function to get seams using Dynamic
   Programming. Also, stored results of minimum seam in seperate list
   for backtracking.

-  **drawSeam()** - Plot seams(vertical and horizontal) using red color
   on image.

-  **carve()** - reshape and crop image.

-  **cropByColumn()** - Implements cropping on both axes, i.e. vertical
   and horizontal.

-  **cropByRow()** - Rotate image to ignore repeated computations and
   provide the rotated image as an input to *cropByColumn* function.

**File:**
`helpers.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/helpers.py>`__

-  **writeImage()** - stores the images in results directory.

-  **writeImageG()** - stores intermediate generated sequence of images
   in sequences directory.

-  **createFolder()** - self explanatory

-  **getFileExtension()** - self explanatory

**Other folders:**

-  **images/** - stores the input images for testing.

-  **videos/** - stores the videos generated from the intermediate
   sequences.

-  **results/** - stores the final results.

-  **sequences/** - stores the intermediate sequences generated.

Installation
============

-  Simply run ``pip install pyCAIR``

-  `Direct download
   option <https://github.com/avidLearnerInProgress/pyCAIR/archive/0.1.tar.gz>`__

Usage
=====

.. code:: python

    '''
    It runs the entire code and returns final results
    '''
    from pyCAIR import user_input
    user_input(alignment, scale, seam, input_image, generate_sequences)

    '''
    It generates the energy map
    '''
    from pyCAIR import generateEnergyMap
    generateEnergyMap(image_name, file_extension, file_name)

    '''
    It generates color maps
    '''
    from pyCAIR import generateColorMap
    generateColorMap(image_name, file_extension, file_name)

    '''
    It converts sequence of images generated to video
    '''
    from pyCAIR import generateVideo
    generateVideo()

    '''
    It returns all the paths where images are present for generating video
    '''
    from pyCAIR import getToProcessPaths
    getToProcessPaths()

    '''
    It returns seams, cropped image for an image
    '''
    from pyCAIR import cropByColumn
    seam_img, crop_img = cropByColumn(image, display_seams, generate, lsit, scale_c, fromRow)

    '''
    It returns seams, cropped image for an image
    '''
    from pyCAIR import cropByRow
    seam_img, crop_img = cropByRow(image, display_seams, generate, lsit, scale_c)

    '''
    It returns created folder
    '''
    from pyCAIR import createFolder
    f = createFolder(folder_name)

    '''
    It returns extension of file
    '''
    from pyCAIR import getFileExtension
    f = getFileExtension(file_name)

    '''
    It writes image to specified folder
    '''
    from pyCAIR import writeImage
    f = writeImage(image, args)

In Action
=========

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/5eb764fd/others/fig13_col-wise_seamseq.gif
       :alt: Gif1

       Gif1

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/5eb764fd/others/fig4_col-wise_seamseq.gif
       :alt: Gif2

       Gif2

..

    `Video
    Playlist <https://www.youtube.com/playlist?list=PL7k5xCepzh7o2kF_FMh4P9tZgALoAx48N>`__

Screenshots
===========

Results for Image 1:
--------------------

+----------------+-----------+------------+
| |Result0|      | |Result1| | |Result2|  |
+================+===========+============+
| Original Image | Grayscale | Energy Map |
+----------------+-----------+------------+

+------------------+---------------+
| |Result3|        | |Result4|     |
+==================+===============+
| Color Map Winter | Color Map Hot |
+------------------+---------------+

+-------------------+-----------------+
| |Result5|         | |Result6|       |
+===================+=================+
| Seams for Columns | Columns Cropped |
+-------------------+-----------------+

+----------------+--------------+
| |Result7|      | |Result8|    |
+================+==============+
| Seams for Rows | Rows Cropped |
+----------------+--------------+

Results for Image 2:
--------------------

+----------------+-----------+------------+
| |Result0|      | |Result1| | |Result2|  |
+================+===========+============+
| Original Image | Grayscale | Energy Map |
+----------------+-----------+------------+

+------------------+---------------+
| |Result3|        | |Result4|     |
+==================+===============+
| Color Map Winter | Color Map Hot |
+------------------+---------------+

+-------------------+-----------------+
| |Result5|         | |Result6|       |
+===================+=================+
| Seams for Columns | Columns Cropped |
+-------------------+-----------------+

+----------------+--------------+
| |Result7|      | |Result8|    |
+================+==============+
| Seams for Rows | Rows Cropped |
+----------------+--------------+

Todo
====

-  [x] Implement Seam Algorithm
-  [x] Generate energy maps and color maps for image
-  [x] Display Vertical Seams
-  [x] Display Horizontal Seams
-  [x] Crop Columns
-  [x] Crop Rows
-  [x] Use argparse for Command Line Application
-  [x] Store subsamples in different directories for crop and seam
   respectively
-  [x] Generate video/gif from sub-samples
-  [x] Provide a better Readme
-  [x] Provide examples for usage
-  [ ] Add badges
-  [ ] Provide better project description on PyPI
-  [ ] Documentation using Spinx
-  [ ] Integrate object detection using YOLOv2
-  [ ] Identify most important object (using probability of predicted
   object)
-  [ ] Invert energy values of most important object
-  [ ] Re-apply Seam Carve and compare results

License
=======

This software is licensed under the `GNU General Public License
v3.0 <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/LICENSE>`__
© `Chirag Shah <https://github.com/avidLearnerInProgress>`__

.. |PyPI version| image:: https://badge.fury.io/py/pyCAIR.svg
   :target: https://badge.fury.io/py/pyCAIR
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/c4692303/others/algorithm.png
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/c4692303/others/backtracking.png
.. |Result0| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig4.png
.. |Result1| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/gray.png
.. |Result2| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/energy.png
.. |Result3| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap1.png
.. |Result4| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap2.png
.. |Result5| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_seams.png
.. |Result6| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_cropped.png
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_seams.png
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_cropped.png
.. |Result0| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig13.jpg
.. |Result1| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/gray.jpg
.. |Result2| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/energy.jpg
.. |Result3| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap1.jpg
.. |Result4| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap2.jpg
.. |Result5| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_seams.jpg
.. |Result6| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_cropped.jpg
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_seams.jpg
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_cropped.jpg

README937258 (Click to Expand/Collapse)

.. raw:: html

   <h1 align="center">

.. raw:: html

   </h1>

pyCAIR is a content-aware image resizing(CAIR)
`library <https://pypi.org/project/pyCAIR/>`__ based on `Seam Carving
for Content-Aware Image
Resizing <http://http://graphics.cs.cmu.edu/courses/15-463/2012_fall/hw/proj3-seamcarving/imret.pdf>`__
paper.

|PyPI version| |License: GPL v3|

Table of Contents
=================

1. `How CAIR works <#how-does-it-work>`__
2. `Understanding the research
   paper <#intutive-explanation-of-research-paper>`__
3. `Project structure and
   explanation <#project-structure-and-explanation>`__
4. `Installation <#installation>`__
5. `Usage <#usage>`__
6. `Demo <#in-action>`__
7. `Screenshots <#screenshots>`__
8. `Todo <#todo>`__

How does it work
================

-  An energy map and a grayscale format of image is generated from the
   provided image.

-  Seam Carving algorithm tries to find the not so useful regions in
   image by picking up the lowest energy values from energy map.

-  With the help of Dynamic Programming coupled with backtracking, seam
   carving algorithm generates individual seams over the image using
   top-down approach or left-right approach.(depending on vertical or
   horizontal resizing)

-  By traversing the image matrix row-wise, the cumulative minimum
   energy is computed for all possible connected seams for each entry.
   The minimum energy level is calculated by summing up the current
   pixel with the lowest value of the neighboring pixels from the
   previous row.

-  Find the lowest cost seam from the energy matrix starting from the
   last row and remove it.

-  Repeat the process iteratively until the image is resized depending
   on user specified ratio.

+-----------+----------------------------------+
| |Result7| | |Result8|                        |
+===========+==================================+
| DP Matrix | Backtracking with minimum energy |
+-----------+----------------------------------+

Intutive explanation of research paper
======================================

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes1.png
       :alt: Notes1

       Notes1

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes2.png
       :alt: Notes2

       Notes2

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes3.png
       :alt: Notes3

       Notes3

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes4.png
       :alt: Notes4

       Notes4

Project structure and explanation
=================================

**Directory structure:**

| **pyCAIR** (root directory)
|   \| - images/
|   \| - results /
|   \| - sequences/ (zipped in repository)
|   \| - videos/
|   \| -
  `notdoneyet.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/notdoneyet.py>`__
|   \| -
  `imgtovideos.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/imgtovideos.py>`__
|   \| -
  `opencv_generators.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/opencv_generators.py>`__
|   \| -
  `seam_carve.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/seam_carve.py>`__
|   \| -
  `helpers.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/helpers.py>`__

**File:**
`notdoneyet.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/notdoneyet.py>`__

-  **user_input()** -
   Parameters:

   -  Alignment: Specify on which axis the resizing operation has to be
      performed.
   -  Scale Ratio: Floating point operation between 0 and 1 to scale the
      output image.
   -  Display Seam: If this option isn’t selected, the image is only
      seamed in background.
   -  Input Image
   -  Generate Sequences: Generate intermediate sequences to form a
      video after all the operations are performed.

**File:**
`imgtovideos.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/imgtovideos.py>`__

-  **generateVideo()** - pass each image path to **vid()** for video
   generation.

-  **vid()**- writes each input image to video buffer for creating a
   complete video.

**File:**
`opencv_generators.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/opencv_generators.py>`__

-  **generateEnergyMap()** - utilised OpenCV inbuilt functions for
   obtaining energies and converting image to grayscale.

-  **generateColorMap()** - utilised OpenCV inbuilt functions to
   superimpose heatmaps on the given image.

**File:**
`seam_carve.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/seam_carve.py>`__

-  **getEnergy()** - generated energy map using sobel operators and
   convolve function.

-  **getMaps()** - implemented the function to get seams using Dynamic
   Programming. Also, stored results of minimum seam in seperate list
   for backtracking.

-  **drawSeam()** - Plot seams(vertical and horizontal) using red color
   on image.

-  **carve()** - reshape and crop image.

-  **cropByColumn()** - Implements cropping on both axes, i.e. vertical
   and horizontal.

-  **cropByRow()** - Rotate image to ignore repeated computations and
   provide the rotated image as an input to *cropByColumn* function.

**File:**
`helpers.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/helpers.py>`__

-  **writeImage()** - stores the images in results directory.

-  **writeImageG()** - stores intermediate generated sequence of images
   in sequences directory.

-  **createFolder()** - self explanatory

-  **getFileExtension()** - self explanatory

**Other folders:**

-  **images/** - stores the input images for testing.

-  **videos/** - stores the videos generated from the intermediate
   sequences.

-  **results/** - stores the final results.

-  **sequences/** - stores the intermediate sequences generated.

Installation
============

-  Simply run ``pip install pyCAIR``

-  `Direct download
   option <https://github.com/avidLearnerInProgress/pyCAIR/archive/0.1.tar.gz>`__

Usage
=====

.. code:: python

    '''
    It runs the entire code and returns final results
    '''
    from pyCAIR import user_input
    user_input(alignment, scale, seam, input_image, generate_sequences)

    '''
    It generates the energy map
    '''
    from pyCAIR import generateEnergyMap
    generateEnergyMap(image_name, file_extension, file_name)

    '''
    It generates color maps
    '''
    from pyCAIR import generateColorMap
    generateColorMap(image_name, file_extension, file_name)

    '''
    It converts sequence of images generated to video
    '''
    from pyCAIR import generateVideo
    generateVideo()

    '''
    It returns all the paths where images are present for generating video
    '''
    from pyCAIR import getToProcessPaths
    getToProcessPaths()

    '''
    It returns seams, cropped image for an image
    '''
    from pyCAIR import cropByColumn
    seam_img, crop_img = cropByColumn(image, display_seams, generate, lsit, scale_c, fromRow)

    '''
    It returns seams, cropped image for an image
    '''
    from pyCAIR import cropByRow
    seam_img, crop_img = cropByRow(image, display_seams, generate, lsit, scale_c)

    '''
    It returns created folder
    '''
    from pyCAIR import createFolder
    f = createFolder(folder_name)

    '''
    It returns extension of file
    '''
    from pyCAIR import getFileExtension
    f = getFileExtension(file_name)

    '''
    It writes image to specified folder
    '''
    from pyCAIR import writeImage
    f = writeImage(image, args)

In Action
=========

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/5eb764fd/others/fig13_col-wise_seamseq.gif
       :alt: Gif1

       Gif1

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/5eb764fd/others/fig4_col-wise_seamseq.gif
       :alt: Gif2

       Gif2

..

    `Video
    Playlist <https://www.youtube.com/playlist?list=PL7k5xCepzh7o2kF_FMh4P9tZgALoAx48N>`__

Screenshots
===========

Results for Image 1:
--------------------

+----------------+-----------+------------+
| |Result0|      | |Result1| | |Result2|  |
+================+===========+============+
| Original Image | Grayscale | Energy Map |
+----------------+-----------+------------+

+------------------+---------------+
| |Result3|        | |Result4|     |
+==================+===============+
| Color Map Winter | Color Map Hot |
+------------------+---------------+

+-------------------+-----------------+
| |Result5|         | |Result6|       |
+===================+=================+
| Seams for Columns | Columns Cropped |
+-------------------+-----------------+

+----------------+--------------+
| |Result7|      | |Result8|    |
+================+==============+
| Seams for Rows | Rows Cropped |
+----------------+--------------+

Results for Image 2:
--------------------

+----------------+-----------+------------+
| |Result0|      | |Result1| | |Result2|  |
+================+===========+============+
| Original Image | Grayscale | Energy Map |
+----------------+-----------+------------+

+------------------+---------------+
| |Result3|        | |Result4|     |
+==================+===============+
| Color Map Winter | Color Map Hot |
+------------------+---------------+

+-------------------+-----------------+
| |Result5|         | |Result6|       |
+===================+=================+
| Seams for Columns | Columns Cropped |
+-------------------+-----------------+

+----------------+--------------+
| |Result7|      | |Result8|    |
+================+==============+
| Seams for Rows | Rows Cropped |
+----------------+--------------+

Todo
====

-  [x] Implement Seam Algorithm
-  [x] Generate energy maps and color maps for image
-  [x] Display Vertical Seams
-  [x] Display Horizontal Seams
-  [x] Crop Columns
-  [x] Crop Rows
-  [x] Use argparse for Command Line Application
-  [x] Store subsamples in different directories for crop and seam
   respectively
-  [x] Generate video/gif from sub-samples
-  [x] Provide a better Readme
-  [x] Provide examples for usage
-  [ ] Add badges
-  [ ] Provide better project description on PyPI
-  [ ] Documentation using Spinx
-  [ ] Integrate object detection using YOLOv2
-  [ ] Identify most important object (using probability of predicted
   object)
-  [ ] Invert energy values of most important object
-  [ ] Re-apply Seam Carve and compare results

License
=======

This software is licensed under the `GNU General Public License
v3.0 <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/LICENSE>`__
© `Chirag Shah <https://github.com/avidLearnerInProgress>`__

.. |PyPI version| image:: https://badge.fury.io/py/pyCAIR.svg
   :target: https://badge.fury.io/py/pyCAIR
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/c4692303/others/algorithm.png
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/c4692303/others/backtracking.png
.. |Result0| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig4.png
.. |Result1| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/gray.png
.. |Result2| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/energy.png
.. |Result3| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap1.png
.. |Result4| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap2.png
.. |Result5| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_seams.png
.. |Result6| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_cropped.png
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_seams.png
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_cropped.png
.. |Result0| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig13.jpg
.. |Result1| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/gray.jpg
.. |Result2| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/energy.jpg
.. |Result3| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap1.jpg
.. |Result4| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap2.jpg
.. |Result5| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_seams.jpg
.. |Result6| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_cropped.jpg
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_seams.jpg
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_cropped.jpg

README707802 (Click to Expand/Collapse)

.. raw:: html

   <h1 align="center">

.. raw:: html

   </h1>

pyCAIR is a content-aware image resizing(CAIR)
`library <https://pypi.org/project/pyCAIR/>`__ based on `Seam Carving
for Content-Aware Image
Resizing <http://http://graphics.cs.cmu.edu/courses/15-463/2012_fall/hw/proj3-seamcarving/imret.pdf>`__
paper.

|PyPI version| |License: GPL v3|

Table of Contents
=================

1. `How CAIR works <#how-does-it-work>`__
2. `Understanding the research
   paper <#intutive-explanation-of-research-paper>`__
3. `Project structure and
   explanation <#project-structure-and-explanation>`__
4. `Installation <#installation>`__
5. `Usage <#usage>`__
6. `Demo <#in-action>`__
7. `Screenshots <#screenshots>`__
8. `Todo <#todo>`__

How does it work
================

-  An energy map and a grayscale format of image is generated from the
   provided image.

-  Seam Carving algorithm tries to find the not so useful regions in
   image by picking up the lowest energy values from energy map.

-  With the help of Dynamic Programming coupled with backtracking, seam
   carving algorithm generates individual seams over the image using
   top-down approach or left-right approach.(depending on vertical or
   horizontal resizing)

-  By traversing the image matrix row-wise, the cumulative minimum
   energy is computed for all possible connected seams for each entry.
   The minimum energy level is calculated by summing up the current
   pixel with the lowest value of the neighboring pixels from the
   previous row.

-  Find the lowest cost seam from the energy matrix starting from the
   last row and remove it.

-  Repeat the process iteratively until the image is resized depending
   on user specified ratio.

+-----------+----------------------------------+
| |Result7| | |Result8|                        |
+===========+==================================+
| DP Matrix | Backtracking with minimum energy |
+-----------+----------------------------------+

Intutive explanation of research paper
======================================

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes1.png
       :alt: Notes1

       Notes1

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes2.png
       :alt: Notes2

       Notes2

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes3.png
       :alt: Notes3

       Notes3

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes4.png
       :alt: Notes4

       Notes4

Project structure and explanation
=================================

**Directory structure:**

| **pyCAIR** (root directory)
|   \| - images/
|   \| - results /
|   \| - sequences/ (zipped in repository)
|   \| - videos/
|   \| -
  `notdoneyet.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/notdoneyet.py>`__
|   \| -
  `imgtovideos.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/imgtovideos.py>`__
|   \| -
  `opencv_generators.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/opencv_generators.py>`__
|   \| -
  `seam_carve.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/seam_carve.py>`__
|   \| -
  `helpers.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/helpers.py>`__

**File:**
`notdoneyet.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/notdoneyet.py>`__

-  **user_input()** -
   Parameters:

   -  Alignment: Specify on which axis the resizing operation has to be
      performed.
   -  Scale Ratio: Floating point operation between 0 and 1 to scale the
      output image.
   -  Display Seam: If this option isn’t selected, the image is only
      seamed in background.
   -  Input Image
   -  Generate Sequences: Generate intermediate sequences to form a
      video after all the operations are performed.

**File:**
`imgtovideos.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/imgtovideos.py>`__

-  **generateVideo()** - pass each image path to **vid()** for video
   generation.

-  **vid()**- writes each input image to video buffer for creating a
   complete video.

**File:**
`opencv_generators.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/opencv_generators.py>`__

-  **generateEnergyMap()** - utilised OpenCV inbuilt functions for
   obtaining energies and converting image to grayscale.

-  **generateColorMap()** - utilised OpenCV inbuilt functions to
   superimpose heatmaps on the given image.

**File:**
`seam_carve.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/seam_carve.py>`__

-  **getEnergy()** - generated energy map using sobel operators and
   convolve function.

-  **getMaps()** - implemented the function to get seams using Dynamic
   Programming. Also, stored results of minimum seam in seperate list
   for backtracking.

-  **drawSeam()** - Plot seams(vertical and horizontal) using red color
   on image.

-  **carve()** - reshape and crop image.

-  **cropByColumn()** - Implements cropping on both axes, i.e. vertical
   and horizontal.

-  **cropByRow()** - Rotate image to ignore repeated computations and
   provide the rotated image as an input to *cropByColumn* function.

**File:**
`helpers.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/helpers.py>`__

-  **writeImage()** - stores the images in results directory.

-  **writeImageG()** - stores intermediate generated sequence of images
   in sequences directory.

-  **createFolder()** - self explanatory

-  **getFileExtension()** - self explanatory

**Other folders:**

-  **images/** - stores the input images for testing.

-  **videos/** - stores the videos generated from the intermediate
   sequences.

-  **results/** - stores the final results.

-  **sequences/** - stores the intermediate sequences generated.

Installation
============

-  Simply run ``pip install pyCAIR``

-  `Direct download
   option <https://github.com/avidLearnerInProgress/pyCAIR/archive/0.1.tar.gz>`__

Usage
=====

.. code:: python

    '''
    It runs the entire code and returns final results
    '''
    from pyCAIR import user_input
    user_input(alignment, scale, seam, input_image, generate_sequences)

    '''
    It generates the energy map
    '''
    from pyCAIR import generateEnergyMap
    generateEnergyMap(image_name, file_extension, file_name)

    '''
    It generates color maps
    '''
    from pyCAIR import generateColorMap
    generateColorMap(image_name, file_extension, file_name)

    '''
    It converts sequence of images generated to video
    '''
    from pyCAIR import generateVideo
    generateVideo()

    '''
    It returns all the paths where images are present for generating video
    '''
    from pyCAIR import getToProcessPaths
    getToProcessPaths()

    '''
    It returns seams, cropped image for an image
    '''
    from pyCAIR import cropByColumn
    seam_img, crop_img = cropByColumn(image, display_seams, generate, lsit, scale_c, fromRow)

    '''
    It returns seams, cropped image for an image
    '''
    from pyCAIR import cropByRow
    seam_img, crop_img = cropByRow(image, display_seams, generate, lsit, scale_c)

    '''
    It returns created folder
    '''
    from pyCAIR import createFolder
    f = createFolder(folder_name)

    '''
    It returns extension of file
    '''
    from pyCAIR import getFileExtension
    f = getFileExtension(file_name)

    '''
    It writes image to specified folder
    '''
    from pyCAIR import writeImage
    f = writeImage(image, args)

In Action
=========

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/5eb764fd/others/fig13_col-wise_seamseq.gif
       :alt: Gif1

       Gif1

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/5eb764fd/others/fig4_col-wise_seamseq.gif
       :alt: Gif2

       Gif2

..

    `Video
    Playlist <https://www.youtube.com/playlist?list=PL7k5xCepzh7o2kF_FMh4P9tZgALoAx48N>`__

Screenshots
===========

Results for Image 1:
--------------------

+----------------+-----------+------------+
| |Result0|      | |Result1| | |Result2|  |
+================+===========+============+
| Original Image | Grayscale | Energy Map |
+----------------+-----------+------------+

+------------------+---------------+
| |Result3|        | |Result4|     |
+==================+===============+
| Color Map Winter | Color Map Hot |
+------------------+---------------+

+-------------------+-----------------+
| |Result5|         | |Result6|       |
+===================+=================+
| Seams for Columns | Columns Cropped |
+-------------------+-----------------+

+----------------+--------------+
| |Result7|      | |Result8|    |
+================+==============+
| Seams for Rows | Rows Cropped |
+----------------+--------------+

Results for Image 2:
--------------------

+----------------+-----------+------------+
| |Result0|      | |Result1| | |Result2|  |
+================+===========+============+
| Original Image | Grayscale | Energy Map |
+----------------+-----------+------------+

+------------------+---------------+
| |Result3|        | |Result4|     |
+==================+===============+
| Color Map Winter | Color Map Hot |
+------------------+---------------+

+-------------------+-----------------+
| |Result5|         | |Result6|       |
+===================+=================+
| Seams for Columns | Columns Cropped |
+-------------------+-----------------+

+----------------+--------------+
| |Result7|      | |Result8|    |
+================+==============+
| Seams for Rows | Rows Cropped |
+----------------+--------------+

Todo
====

-  [x] Implement Seam Algorithm
-  [x] Generate energy maps and color maps for image
-  [x] Display Vertical Seams
-  [x] Display Horizontal Seams
-  [x] Crop Columns
-  [x] Crop Rows
-  [x] Use argparse for Command Line Application
-  [x] Store subsamples in different directories for crop and seam
   respectively
-  [x] Generate video/gif from sub-samples
-  [x] Provide a better Readme
-  [x] Provide examples for usage
-  [ ] Add badges
-  [ ] Provide better project description on PyPI
-  [ ] Documentation using Spinx
-  [ ] Integrate object detection using YOLOv2
-  [ ] Identify most important object (using probability of predicted
   object)
-  [ ] Invert energy values of most important object
-  [ ] Re-apply Seam Carve and compare results

License
=======

This software is licensed under the `GNU General Public License
v3.0 <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/LICENSE>`__
© `Chirag Shah <https://github.com/avidLearnerInProgress>`__

.. |PyPI version| image:: https://badge.fury.io/py/pyCAIR.svg
   :target: https://badge.fury.io/py/pyCAIR
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/c4692303/others/algorithm.png
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/c4692303/others/backtracking.png
.. |Result0| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig4.png
.. |Result1| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/gray.png
.. |Result2| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/energy.png
.. |Result3| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap1.png
.. |Result4| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap2.png
.. |Result5| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_seams.png
.. |Result6| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_cropped.png
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_seams.png
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_cropped.png
.. |Result0| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig13.jpg
.. |Result1| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/gray.jpg
.. |Result2| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/energy.jpg
.. |Result3| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap1.jpg
.. |Result4| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap2.jpg
.. |Result5| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_seams.jpg
.. |Result6| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_cropped.jpg
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_seams.jpg
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_cropped.jpg

README2888 (Click to Expand/Collapse)

.. raw:: html

   <h1 align="center">

.. raw:: html

   </h1>

pyCAIR is a content-aware image resizing(CAIR)
`library <https://pypi.org/project/pyCAIR/>`__ based on `Seam Carving
for Content-Aware Image
Resizing <http://http://graphics.cs.cmu.edu/courses/15-463/2012_fall/hw/proj3-seamcarving/imret.pdf>`__
paper.

|PyPI version| |License: GPL v3|

Table of Contents
=================

1. `How CAIR works <#how-does-it-work>`__
2. `Understanding the research
   paper <#intutive-explanation-of-research-paper>`__
3. `Project structure and
   explanation <#project-structure-and-explanation>`__
4. `Installation <#installation>`__
5. `Usage <#usage>`__
6. `Demo <#in-action>`__
7. `Screenshots <#screenshots>`__
8. `Todo <#todo>`__

How does it work
================

-  An energy map and a grayscale format of image is generated from the
   provided image.

-  Seam Carving algorithm tries to find the not so useful regions in
   image by picking up the lowest energy values from energy map.

-  With the help of Dynamic Programming coupled with backtracking, seam
   carving algorithm generates individual seams over the image using
   top-down approach or left-right approach.(depending on vertical or
   horizontal resizing)

-  By traversing the image matrix row-wise, the cumulative minimum
   energy is computed for all possible connected seams for each entry.
   The minimum energy level is calculated by summing up the current
   pixel with the lowest value of the neighboring pixels from the
   previous row.

-  Find the lowest cost seam from the energy matrix starting from the
   last row and remove it.

-  Repeat the process iteratively until the image is resized depending
   on user specified ratio.

+-----------+----------------------------------+
| |Result7| | |Result8|                        |
+===========+==================================+
| DP Matrix | Backtracking with minimum energy |
+-----------+----------------------------------+

Intutive explanation of research paper
======================================

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes1.png
       :alt: Notes1

       Notes1

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes2.png
       :alt: Notes2

       Notes2

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes3.png
       :alt: Notes3

       Notes3

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes4.png
       :alt: Notes4

       Notes4

Project structure and explanation
=================================

**Directory structure:**

| **pyCAIR** (root directory)
|   \| - images/
|   \| - results /
|   \| - sequences/ (zipped in repository)
|   \| - videos/
|   \| -
  `notdoneyet.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/notdoneyet.py>`__
|   \| -
  `imgtovideos.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/imgtovideos.py>`__
|   \| -
  `opencv_generators.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/opencv_generators.py>`__
|   \| -
  `seam_carve.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/seam_carve.py>`__
|   \| -
  `helpers.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/helpers.py>`__

**File:**
`notdoneyet.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/notdoneyet.py>`__

-  **user_input()** -
   Parameters:

   -  Alignment: Specify on which axis the resizing operation has to be
      performed.
   -  Scale Ratio: Floating point operation between 0 and 1 to scale the
      output image.
   -  Display Seam: If this option isn’t selected, the image is only
      seamed in background.
   -  Input Image
   -  Generate Sequences: Generate intermediate sequences to form a
      video after all the operations are performed.

**File:**
`imgtovideos.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/imgtovideos.py>`__

-  **generateVideo()** - pass each image path to **vid()** for video
   generation.

-  **vid()**- writes each input image to video buffer for creating a
   complete video.

**File:**
`opencv_generators.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/opencv_generators.py>`__

-  **generateEnergyMap()** - utilised OpenCV inbuilt functions for
   obtaining energies and converting image to grayscale.

-  **generateColorMap()** - utilised OpenCV inbuilt functions to
   superimpose heatmaps on the given image.

**File:**
`seam_carve.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/pyCAIR/seam_carve.py>`__

-  **getEnergy()** - generated energy map using sobel operators and
   convolve function.

-  **getMaps()** - implemented the function to get seams using Dynamic
   Programming. Also, stored results of minimum seam in seperate list
   for backtracking.

-  **drawSeam()** - Plot seams(vertical and horizontal) using red color
   on image.

-  **carve()** - reshape and crop image.

-  **cropByColumn()** - Implements cropping on both axes, i.e. vertical
   and horizontal.

-  **cropByRow()** - Rotate image to ignore repeated computations and
   provide the rotated image as an input to *cropByColumn* function.

**File:**
`helpers.py <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/helpers.py>`__

-  **writeImage()** - stores the images in results directory.

-  **writeImageG()** - stores intermediate generated sequence of images
   in sequences directory.

-  **createFolder()** - self explanatory

-  **getFileExtension()** - self explanatory

**Other folders:**

-  **images/** - stores the input images for testing.

-  **videos/** - stores the videos generated from the intermediate
   sequences.

-  **results/** - stores the final results.

-  **sequences/** - stores the intermediate sequences generated.

Installation
============

-  Simply run ``pip install pyCAIR``

-  `Direct download
   option <https://github.com/avidLearnerInProgress/pyCAIR/archive/0.1.tar.gz>`__

Usage
=====

.. code:: python

    '''
    It runs the entire code and returns final results
    '''
    from pyCAIR import user_input
    user_input(alignment, scale, seam, input_image, generate_sequences)

    '''
    It generates the energy map
    '''
    from pyCAIR import generateEnergyMap
    generateEnergyMap(image_name, file_extension, file_name)

    '''
    It generates color maps
    '''
    from pyCAIR import generateColorMap
    generateColorMap(image_name, file_extension, file_name)

    '''
    It converts sequence of images generated to video
    '''
    from pyCAIR import generateVideo
    generateVideo()

    '''
    It returns all the paths where images are present for generating video
    '''
    from pyCAIR import getToProcessPaths
    getToProcessPaths()

    '''
    It returns seams, cropped image for an image
    '''
    from pyCAIR import cropByColumn
    seam_img, crop_img = cropByColumn(image, display_seams, generate, lsit, scale_c, fromRow)

    '''
    It returns seams, cropped image for an image
    '''
    from pyCAIR import cropByRow
    seam_img, crop_img = cropByRow(image, display_seams, generate, lsit, scale_c)

    '''
    It returns created folder
    '''
    from pyCAIR import createFolder
    f = createFolder(folder_name)

    '''
    It returns extension of file
    '''
    from pyCAIR import getFileExtension
    f = getFileExtension(file_name)

    '''
    It writes image to specified folder
    '''
    from pyCAIR import writeImage
    f = writeImage(image, args)

In Action
=========

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/5eb764fd/others/fig13_col-wise_seamseq.gif
       :alt: Gif1

       Gif1

..

    .. figure:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/5eb764fd/others/fig4_col-wise_seamseq.gif
       :alt: Gif2

       Gif2

..

    `Video
    Playlist <https://www.youtube.com/playlist?list=PL7k5xCepzh7o2kF_FMh4P9tZgALoAx48N>`__

Screenshots
===========

Results for Image 1:
--------------------

+----------------+-----------+------------+
| |Result0|      | |Result1| | |Result2|  |
+================+===========+============+
| Original Image | Grayscale | Energy Map |
+----------------+-----------+------------+

+------------------+---------------+
| |Result3|        | |Result4|     |
+==================+===============+
| Color Map Winter | Color Map Hot |
+------------------+---------------+

+-------------------+-----------------+
| |Result5|         | |Result6|       |
+===================+=================+
| Seams for Columns | Columns Cropped |
+-------------------+-----------------+

+----------------+--------------+
| |Result7|      | |Result8|    |
+================+==============+
| Seams for Rows | Rows Cropped |
+----------------+--------------+

Results for Image 2:
--------------------

+----------------+-----------+------------+
| |Result0|      | |Result1| | |Result2|  |
+================+===========+============+
| Original Image | Grayscale | Energy Map |
+----------------+-----------+------------+

+------------------+---------------+
| |Result3|        | |Result4|     |
+==================+===============+
| Color Map Winter | Color Map Hot |
+------------------+---------------+

+-------------------+-----------------+
| |Result5|         | |Result6|       |
+===================+=================+
| Seams for Columns | Columns Cropped |
+-------------------+-----------------+

+----------------+--------------+
| |Result7|      | |Result8|    |
+================+==============+
| Seams for Rows | Rows Cropped |
+----------------+--------------+

Todo
====

-  [x] Implement Seam Algorithm
-  [x] Generate energy maps and color maps for image
-  [x] Display Vertical Seams
-  [x] Display Horizontal Seams
-  [x] Crop Columns
-  [x] Crop Rows
-  [x] Use argparse for Command Line Application
-  [x] Store subsamples in different directories for crop and seam
   respectively
-  [x] Generate video/gif from sub-samples
-  [x] Provide a better Readme
-  [x] Provide examples for usage
-  [ ] Add badges
-  [ ] Provide better project description on PyPI
-  [ ] Documentation using Spinx
-  [ ] Integrate object detection using YOLOv2
-  [ ] Identify most important object (using probability of predicted
   object)
-  [ ] Invert energy values of most important object
-  [ ] Re-apply Seam Carve and compare results

License
=======

This software is licensed under the `GNU General Public License
v3.0 <https://github.com/avidLearnerInProgress/pyCAIR/blob/master/LICENSE>`__
© `Chirag Shah <https://github.com/avidLearnerInProgress>`__

.. |PyPI version| image:: https://badge.fury.io/py/pyCAIR.svg
   :target: https://badge.fury.io/py/pyCAIR
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/c4692303/others/algorithm.png
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/c4692303/others/backtracking.png
.. |Result0| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig4.png
.. |Result1| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/gray.png
.. |Result2| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/energy.png
.. |Result3| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap1.png
.. |Result4| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap2.png
.. |Result5| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_seams.png
.. |Result6| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_cropped.png
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_seams.png
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_cropped.png
.. |Result0| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig13.jpg
.. |Result1| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/gray.jpg
.. |Result2| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/energy.jpg
.. |Result3| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap1.jpg
.. |Result4| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap2.jpg
.. |Result5| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_seams.jpg
.. |Result6| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_cropped.jpg
.. |Result7| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_seams.jpg
.. |Result8| image:: https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_cropped.jpg
