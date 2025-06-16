# Analysis-of-atomic-displacement-in-STEM-images

# Atom Lattice Analysis Project

## Overview

My story with this project started when one of my clients asked me to provide a detailed atomic-scale analysis of the displacement of Ti ions in BaTiO₃ thin films. To tackle this challenge, I evaluated multiple open-source microscopy toolkits—including HyperSpy, Atomap, and TopoTEM—which are also featured in other repositories of mine focused on synthetic STEM image generation and lattice analysis.

What I am presenting here is the result of hands-on work with real materials and real microscopes, focused on a practical need: extracting quantitative atomic displacement fields from high-resolution STEM images. The process begins by selecting the best-quality images and fine-tuning parameters for lattice detection and fitting. From there, the goal is to accurately calculate local shifts of Ti ions or other atomic species in the lattice—information that directly relates to strain, defect structures, and functional behavior in oxide materials.

This project showcases a progressive workflow that starts with open-source scientific image analysis libraries widely used in the microscopy and materials research community, such as **HyperSpy**, **atomap**, and **TopoTEM**, to perform lattice fitting, atom position detection, and sublattice decomposition from atomic-resolution STEM images. These foundational steps are essential for converting raw images into structured data that can be quantitatively analyzed.

Once the atom positions and displacement vectors are extracted, the project transitions into the data science domain. Using scikit-learn, it applies Principal Component Analysis (PCA) for dimensionality reduction and clustering algorithms (like KMeans and DBSCAN) to reveal hidden patterns in atomic shifts—such as domain boundaries, strain distributions, or correlated defect behavior. This allows users not only to visualize displacement fields but also to segment and interpret nanostructural variations quantitatively.

By combining materials-specific expertise with reproducible, scriptable Python workflows, this project bridges the gap between traditional microscopy analysis and modern data-driven materials research. It is particularly valuable for researchers aiming to scale up atomic-scale studies, automate workflows, or integrate machine learning into defect and strain analysis pipelines.<br><br>

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









