## Content Aware Image Resizing
-------------------------------

Project published on PyPI. You can do `pip install pyCAIR` to install the latest version.

### Todo:
---------

- [x] Implement Seam Algorithm
- [x] Generate energy maps and color maps for image
- [x] Display Vertical Seams 
- [x] Display Horizontal Seams 
- [x] Crop Columns 
- [x] Crop Rows 
- [x] Use argparse for Command Line Application 
- [x] Store subsamples in different directories for crop and seam respectively 
- [x] Generate video/gif from sub-samples  
- [ ] Provide a better Readme
- [ ] Generate unittests for each functions
- [ ] Provide examples for all the entry points
- [ ] Provide better project description on PyPI
- [ ] Documentation using Spinx


### Notes:
---------

## ![Notes1](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes1.png)  
## ![Notes2](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes2.png)  
## ![Notes3](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes3.png)  
## ![Notes4](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes4.png)  


### Explanation:
---------------

**File:** [notdoneyet.py](https://github.com/avidLearnerInProgress/pyCAIR/blob/master/notdoneyet.py)

* ***Implemented Seam Carving Algorithm*** 
   * **getEnergy()** \- generated energy map using sobel operators and convolve function.
   * **getMaps()** \- implemented the function to get seams using Dynamic Programming. Also, stored results of minimum seam in seperate list for backtracking.
   * **drawSeam()** \- Plot seams(vertical and horizontal) using red color on image.
   * **carve()** \- reshape and crop image.
* ***Generated grayscale and energy maps using OpenCV.***
   * **generateEnergyMap()** \- utilised OpenCV inbuilt functions for obtaining energies and converting image to grayscale.
   * **generateColorMap() -** utilised OpenCV inbuilt functions to superimpose heatmaps on the given image.
* ***Crop Columns***
   * **cropByColumn()** \- Implements cropping on both axes, i.e. vertical and horizontal.
   * **cropByRow()** \- Rotate image to ignore repeated computations and provide the rotated image as an input to *cropByColumn* function.
* ***Argparse library for user input***
   * **Parameters:**
      * Alignment: Specify on which axis the resizing operation has to be performed.
      * Scale Ratio: Floating point operation between 0 and 1 to scale the output image.
      * Display Seam: If this option isn't selected, the image is only seamed in background. No output for seams is visible.
      * Input Image
      * Generate Sequences: Generate intermediate sequences to form a video after all the operations are performed.
* ***Helpers***
   * **writeImage()** \- stores the images in results directory.
   * **writeImageG()** \- stores intermediate generated sequence of images in sequences directory.
   * **createFolder() -** self explanatory
   * **getFileExtension() -** self explanatory

**File:** [imgtovideos.py](https://github.com/avidLearnerInProgress/pyCAIR/blob/master/imgtovideos.py)

* ***Generate Video***
   * **\_vid()** \- writes each input image to video buffer for creating a complete video
   * **generateVideo()** \- pass each image path to *\_vid()* for video generation
* ***Helpers***
   * **getProcessPaths()** \- returns list of all sub-directories within a base path with certain conditions.
   * **createFolder()** \- self explanatory 


### In Action:
--------------

[![Video1](https://cdn.pbrd.co/images/HqSW5C0.png)](https://youtube.com/watch?v=PXYryvF7moE)  

[![Video2](https://cdn.pbrd.co/images/HqSWjpq.png)](https://www.youtube.com/watch?v=fH21N4MBN3k)  

- [Playlist](https://www.youtube.com/playlist?list=PL7k5xCepzh7o2kF_FMh4P9tZgALoAx48N)  


### Screenshots:
----------------

#### Results for Image 1:

| ![Result0](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig4.png)  | ![Result1](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/gray.png) | ![Result2](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/energy.png) |
|:---:|:---:|:---:|
| Original Image | Grayscale | Energy Map |  

| ![Result3](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap1.png)  | ![Result4](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/colormap2.png) |
|:---:|:---:|
| Color Map Winter | Color Map Hot |  

| ![Result5](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_seams.png)  | ![Result6](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/column_cropped.png) |
|:---:|:---:|
| Seams for Columns | Columns Cropped |  

| ![Result7](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_seams.png)  | ![Result8](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig4/row_cropped.png) |
|:---:|:---:|
| Seams for Rows | Rows Cropped |  

#### Results for Image 2:  

| ![Result0](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/images/fig13.jpg)  | ![Result1](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/gray.jpg) | ![Result2](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/energy.jpg) |
|:---:|:---:|:---:|
| Original Image | Grayscale | Energy Map |  

| ![Result3](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap1.jpg)  | ![Result4](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/colormap2.jpg) |
|:---:|:---:|
| Color Map Winter | Color Map Hot |  

| ![Result5](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_seams.jpg)  |![Result6](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/column_cropped.jpg) |
|:---:|:---:|
| Seams for Columns | Columns Cropped |  

| ![Result7](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_seams.jpg)  | ![Result8](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/0fc66d01/results/fig13/row_cropped.jpg) |
|:---:|:---:|
| Seams for Rows | Rows Cropped |  

### License:
------------

This software is licensed under the [GNU General Public License v3.0](https://github.com/avidLearnerInProgress/pyCAIR/blob/master/LICENSE) license  
