# Analysis-of-atomic-displacement-in-STEM-images

### Introduction
My story with this project started when one of my clients asked me to provide a detailed atomic scale analysis of the displacement of Ti ions in BaTiO3 thin films. Among the different methods to accomplish this fine analysis, I considered **atomap** and **temul-toolkit**, very handy and also useful for different purposes like synthetic microscopy image generation, as you can find in my different repositories.  
What makes the atomic displacement analysis difficult is first, acquiring a nice image most likely with probe corrected microscope, as it resolves atoms much better compared to the non-corrected microscope. In fact, even for a lattice like BaTiO3 which does not demand sub-Angstrom resolution, to better define the distance or the border between two atoms, I do recommend using probe corrected microscope. <br>
The second challenge is applying different algorithms and their hyperparameter tuning to find the best match between real atomic positions in an image and the ones that the algorithm finds. The tutorial part of the respective packages I have already mentioned provides readers with a bunch of examples to learn the packages deeply. <br>
So what I am presenting in this project is merely my experience with specific samples I was dealing with and of course, the microscope I was using. The best approach is to start with the best image and find some initial parameters which provide the best match for atoms to eventually calculate the displacement of the Ti ions or other atoms in the lattice. <br><br>
### Denoising the atomic displacement maps
Since the displacement of the Ti ions is in the order of a few tens of pm, one might expect a noisy map of the atomic displacements. In my opinion, what is important is the collective movement of the atomic displacements. As a common practice in microscopy and spectroscopy, principal component analysis is a powerful tool to reduce the noise in images. There are different varieties of the pca analysis, and the best is to understand each variant and apply it to your image. Most likely, images with less noise or defect might require specific pca, and the ones with defects or more noise, might require another variant of pca. <br>
By the end, I have applied both supervised and unsupervised learning to categorize the displacement direction across the image. In this notebook, I have just shown the unsupervised approach to find out the regions with different polarization in an image. <br>
### Hardware and Software
The computer I used for this project is equipped with a 13th Gen Intel(R) Core(TM) i9-13900KF processor with 64 GB RAM, and NVIDIA GForce 4080 (Compute Capability 8.9) with 16 GB RAM. I did not try this notebook in google colab, but it should be quite fast to proceed with image processing. <br><br>
I have used the following packages in preparing the notebook:<br><br>
1- scikit-learn    version 1.2.1  <br>
2- Python          version 3.10.8 <br>
3- hyperspy        version 1.7.3  <br>
