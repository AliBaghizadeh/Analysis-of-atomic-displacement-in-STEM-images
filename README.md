# Analysis-of-atomic-displacement-in-STEM-images

# Atom Lattice Analysis Project

## Overview
My story with this project started when one of my clients asked me to provide a detailed atomic-scale analysis of the displacement of Ti ions in BaTiO3 thin films. Among the different methods to accomplish this fine analysis, I considered **HyperSpy**, **atomap** and **TopoTEM**, which are very handy and also useful for different purposes, like synthetic microscopy image generation, as you can find in my different repositories.  
What I am presenting in this project is merely my experience with specific samples I was dealing with and of course, the microscope I was using. The best approach is to start with the best image and find some initial parameters which provide the best match for atoms to eventually calculate the displacement of the Ti ions or other atoms in the lattice. <br><br>

This project provides tools for analyzing atom lattice structures in materials using advanced image processing and data science techniques. It supports:
- Loading and preprocessing images of atom lattices.
- Lattice and sublattice analysis.
- Displacement vector analysis.
- Clustering and visualization of atom positions.

The project is modular, with functionality organized into distinct Python classes and scripts, and includes a step-by-step demonstration in a Jupyter notebook.

---

## Features
- **ImageHandler**: Load and manage microscopy images.
- **ImageProcessor**: Perform image operations like rotation, cropping, and super-resolution.
- **AtomLatticeAnalyzer**: Analyze atom lattice and sublattice structures.
- **DisplacementAnalyzer**: Compute displacement vectors and visualize polarization data.
- **ClusterAnalyzer**: Perform clustering on atom displacement data using KMeans, GMM, and more.
- **Jupyter Notebook**: An interactive guide demonstrating how to use these tools.

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

### Install Dependencies
Install all required Python libraries using pip:
```bash
pip install -r requirements.txt










