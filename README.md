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
