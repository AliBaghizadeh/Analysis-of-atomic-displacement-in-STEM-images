# Analysis-of-atomic-displacement-in-STEM-images

# Atom Lattice Analysis Project

## Overview
My story with this project started when one of my clients asked me to provide a detailed atomic-scale analysis of the displacement of Ti ions in BaTiO3 thin films. Among the different methods to accomplish this fine analysis, I considered **HyperSpy**, **atomap**, and **TopoTEM**, which are very handy and also useful for different purposes, like synthetic microscopy image generation, as you can find in my different repositories.  
What I am presenting in this project is merely my experience with specific samples I was dealing with and of course, the microscope I was using. The best approach is to start with the best image and find some initial parameters that provide the best match for atoms to eventually calculate the displacement of the Ti ions or other atoms in the lattice. <br><br>

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
cd Analysis-of-atomic-displacement-in-STEM-images
```
### Install Dependencies
Install all required Python libraries using pip:
```bash
pip install -r requirements.txt
```

## Usage
1. Place your raw images in the `images/` directory.
2. Use the provided Python scripts or the Jupyter notebook to perform the analysis.
3. Processed results will be saved in the `results/` directory.

## Repository Structure
```
AtomLatticeAnalysis/
├── images/                          # Raw image files
├── results/                         # Processed results (e.g., plots, data)
├── src/                             # Source code
│   ├── __init__.py                  # Makes src a package
│   ├── image_handler.py             # ImageHandler class
│   ├── image_processor.py           # ImageProcessor class
│   ├── atom_lattice_analyzer.py     # AtomLatticeAnalyzer class
│   ├── displacement_analyzer.py     # DisplacementAnalyzer class
│   ├── clustering.py                # ClusterAnalyzer and related functions
├── notebooks/                       # Jupyter notebooks for demonstrations
│   ├── analysis_demo.ipynb          # Interactive guide
├── requirements.txt                 # Python dependencies
├── setup.py                         # For packaging the project
├── README.md                        # Project overview
├── LICENSE                          # License file
└── .gitignore                       # Ignored files and folders
```
## Running the Jupyter Notebook
The Jupyter notebook analysis_demo.ipynb demonstrates all major functionalities. You can use it as a reference to apply the tools to your own data.

To run the notebook:
1. Install Jupyter:
```bash
pip install notebook
```
2. Start the Jupyter server:
```bash
jupyter notebook
```
3. Open the notebooks/analysis_demo.ipynb file and follow the step-by-step guide.

## License
This project is licensed under the MIT License.









