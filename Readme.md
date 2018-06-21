## Content Aware Image Resizing
-------------------------------

Working and explanation details to be updated soon.  

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
- [ ] Organise code for production
- [ ] Deploy as module

### Notes:
---------

## ![Notes1](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes1.png)  
## ![Notes2](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes2.png)  
## ![Notes3](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes3.png)  
## ![Notes4](https://cdn.rawgit.com/avidLearnerInProgress/pyCAIR/06ce7c6e/notes/notes4.png)  

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

