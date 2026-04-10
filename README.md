# KALz Project 3

## 1. Software and Platform
- **Python 3**: packages listed in `requirements.txt` (run `pip install -r requirements.txt`)
- Used Mac & Windows during development

## 2. Repository Map
```
[Project Folder]/
├── data/
│   ├── 
│   └── 
├── output/
│   ├── 
│   ├── 
│   └── 
├── scripts/
│   ├── MI2_EDA.py                      # Python EDA script for MI2
│   └── 
├── Data Appendix.pdf                   # Data appendix describing variables and sources
├── venv/                               # Python virtual environment (git ignored)
├── .gitignore
├── LICENSE.md
├── README.md
└── requirements.txt                    # Python package dependencies
```
> [!NOTE]
> The venv/ directory was git ignored due to size; create it using directions below.
> You can delete everything in output/ and recreate using the scripts if you would like.

## 3. How to reproduce our results
> [!NOTE]
> Ensure Python and R are set up on your system.
> Run ALL terminal commands from the project root directory.
> Use `python3` instead of `python` or `pip3` instead of `pip` if commands aren't running.

### Create a virtual environment and install Python packages
Virtual environments isolate your packages to your current environment.
In your terminal:
- Create environment: `python -m venv venv`
- Activate it:
	- On macOS: `source venv/bin/activate`
	- On Windows: `source venv/Scripts/activate`
- Install packages: `pip install -r requirements.txt`

### Run the EDA using Python
In your terminal:
- `python scripts/MI2_EDA.py`
- This generates [SPECIFY WHICH FIGURES] in `output/`.

### ADD MORE

## 4. References
References: \
[1]		C. Vaccari and A. Chadwick, "Deepfakes and disinformation: Exploring the impact of synthetic \
		political video on deception, uncertainty, and trust in news," Social Media + Society, vol. 6, no. \
		pp. 1-13, 2020, doi: 10.1177/2056305120903408. \
[2] 	G. Kourounis, A. Elmahmudi, B. Thomson, J. Hunter, H. Ugail, and C. Wilson, "Computer image \
		analysis with artificial intelligence: a practical introduction to convolutional neural networks \
		for medical professionals," Postgraduate Medical Journal, Oct. 2023, doi: \
		https://doi.org/10.1093/postmj/qgad095. \
[3] 	J. J. Bird and A. Lotfi, "CIFAKE: Image classification and explainable identification of \
		AI-generated synthetic images," IEEE Access, vol. 12, pp. 15642-15650, 2024, doi: \
		10.1109/ACCESS.2024.3356122. \
[4] 	A. Krizhevsky and G. Hinton, "Learning multiple layers of features from tiny images," University \
		of Toronto, Toronto, ON, Canada, Tech. Rep., 2009. \
[5] 	R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, "High-resolution image synthesis \
		with latent diffusion models," in Proc. IEEE/CVF Conf. Comput. Vision and Pattern Recognition \
		(CVPR), New Orleans, LA, USA, 2022, pp. 10674-10685. \
[6] 	K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. \
		IEEE Conf. Comput. Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 2016, pp. 770-778. \
[7] 	G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, "Densely connected convolutional \
		networks," in Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR), Honolulu, HI, \
		USA, 2017, pp. 2261-2269. \
[8] 	R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, "Grad-CAM: Visual \
		explanations from deep networks via gradient-based localization," in Proc. IEEE Int. Conf. \
		Comput. Vision (ICCV), Venice, Italy, 2017, pp. 618-626.
