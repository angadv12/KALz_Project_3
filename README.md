# KALz Project 3

## 1. Software and Platform

- **Python 3**
- **Google Colab GPU runtime** for model training and evaluation
- Local development was done on macOS and Windows
- Python packages are listed in `requirements.txt`; the Colab notebooks also install missing packages when needed

## 2. Repository Map

```text
[Project Folder]/
├── data/
│   ├── train/
│   │   ├── FAKE/
│   │   └── REAL/
│   └── test/
│       ├── FAKE/
│       └── REAL/
├── output/
│   ├── densenet121_training_history.csv
│   ├── preprocess_config.json
│   ├── resnet50_training_history.csv
│   ├── training_curves.png
│   ├── training_history_all.csv
│   ├── evaluation/
│   │   ├── densenet121_classification_report.txt
│   │   ├── densenet121_confusion_matrix.png
│   │   ├── densenet121_test_predictions.csv
│   │   ├── final_results_summary.txt
│   │   ├── metrics_summary.csv
│   │   ├── resnet50_classification_report.txt
│   │   ├── resnet50_confusion_matrix.png
│   │   └── resnet50_test_predictions.csv
│   ├── gradcam/
│   │   ├── densenet121_gradcam_examples.png
│   │   └── resnet50_gradcam_examples.png
│   └── models/
│       ├── densenet121_best.pt
│       └── resnet50_best.pt
├── scripts/
│   ├── 01_EDA.py
│   ├── 02_03_04_preprocess_training.ipynb
│   └── 05_06_07_eval_gradcam_report.ipynb
├── .gitignore
├── LICENSE.md
├── README.md
└── requirements.txt
```

> [!NOTE]
> The `data/` folder and model checkpoint files are large. They are not meant to be recreated manually file-by-file in Google Drive. Keep the dataset as a single zip in Google Drive, copy that one zip into Colab local storage, unzip locally, and save outputs back to Google Drive.

## 3. Where to Put Google Drive Outputs Locally

After running the Colab notebooks, download or copy the generated Google Drive folder:

```text
/content/drive/MyDrive/proj3/output
```

Place it at the root of this local repository as:

```text
output/
```

The final local paths should include:

```text
output/preprocess_config.json
output/training_history_all.csv
output/resnet50_training_history.csv
output/densenet121_training_history.csv
output/training_curves.png
output/evaluation/metrics_summary.csv
output/evaluation/final_results_summary.txt
output/evaluation/resnet50_confusion_matrix.png
output/evaluation/densenet121_confusion_matrix.png
output/gradcam/resnet50_gradcam_examples.png
output/gradcam/densenet121_gradcam_examples.png
```

The checkpoint files should be placed here if they are needed for rerunning evaluation:

```text
output/models/resnet50_best.pt
output/models/densenet121_best.pt
```

If GitHub or the submission system rejects large files, keep the `.pt` checkpoint files in Google Drive and include the metrics/plots/reports in `output/` locally.

## 4. How to Reproduce the Results

### Local Setup for EDA

Run these commands from the project root:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scripts/01_EDA.py
```

On Windows PowerShell, activate the environment with:

```bash
venv\\Scripts\\Activate.ps1
```

The local `data/` folder must contain this structure before running EDA:

```text
data/train/REAL
data/train/FAKE
data/test/REAL
data/test/FAKE
```

### Colab Setup for Training and Evaluation

1. Upload the project folder or notebooks to Google Drive under:

```text
MyDrive/proj3
```

2. Put the CIFAKE dataset zip at this Google Drive path:

```text
MyDrive/proj3/cifake.zip
```

3. Open Colab and choose a GPU runtime:

```text
Runtime > Change runtime type > GPU
```

Use an H100 or A100 if available. L4 and T4 also work.
> [!NOTE]
> If you are a student, you can claim Google Colab Pro with .edu email.

### Run Steps 2-4: Preprocessing, Model Setup, and Training

Open and run:

```text
scripts/02_03_04_preprocess_training.ipynb
```

This notebook:

- mounts Google Drive
- copies the single dataset zip from Drive to `/content/proj3_runtime`
- unzips the dataset locally in Colab
- creates train, validation, and test dataloaders
- resizes images to `224x224`
- normalizes images with ImageNet mean and standard deviation
- trains ResNet-50 and DenseNet-121
- saves model checkpoints and training outputs to Google Drive

The main outputs are saved to:

```text
/content/drive/MyDrive/proj3/output/preprocess_config.json
/content/drive/MyDrive/proj3/output/resnet50_training_history.csv
/content/drive/MyDrive/proj3/output/densenet121_training_history.csv
/content/drive/MyDrive/proj3/output/training_history_all.csv
/content/drive/MyDrive/proj3/output/training_curves.png
/content/drive/MyDrive/proj3/output/models/resnet50_best.pt
/content/drive/MyDrive/proj3/output/models/densenet121_best.pt
```

### Run Steps 5-7: Evaluation, Grad-CAM, and Reporting

After training finishes, open and run:

```text
scripts/05_06_07_eval_gradcam_report.ipynb
```

This notebook:

- loads the saved model checkpoints from Google Drive
- rebuilds the test dataloader
- evaluates both models on the 20,000-image test set
- saves classification reports and confusion matrices
- generates Grad-CAM examples
- writes a final summary text file

The main outputs are saved to:

```text
/content/drive/MyDrive/proj3/output/evaluation/metrics_summary.csv
/content/drive/MyDrive/proj3/output/evaluation/final_results_summary.txt
/content/drive/MyDrive/proj3/output/evaluation/resnet50_confusion_matrix.png
/content/drive/MyDrive/proj3/output/evaluation/densenet121_confusion_matrix.png
/content/drive/MyDrive/proj3/output/gradcam/resnet50_gradcam_examples.png
/content/drive/MyDrive/proj3/output/gradcam/densenet121_gradcam_examples.png
```

## 5. Final Model Results

Both models exceeded the project goal of 80% test accuracy and surpassed the 92.98% baseline reported by Bird and Lotfi.

| Model | Test Accuracy | Precision | Recall | F1 | Test Size |
|---|---:|---:|---:|---:|---:|
| ResNet-50 | 0.9692 | 0.9693 | 0.9692 | 0.9692 | 20,000 |
| DenseNet-121 | 0.9697 | 0.9700 | 0.9697 | 0.9697 | 20,000 |

DenseNet-121 was the best model by test accuracy, but only by 0.05 percentage points, so both pretrained CNN architectures performed similarly well on CIFAKE.

## 6. References

[1] C. Vaccari and A. Chadwick, "Deepfakes and disinformation: Exploring the impact of synthetic political video on deception, uncertainty, and trust in news," Social Media + Society, vol. 6, no. pp. 1-13, 2020, doi: 10.1177/2056305120903408.

[2] G. Kourounis, A. Elmahmudi, B. Thomson, J. Hunter, H. Ugail, and C. Wilson, "Computer image analysis with artificial intelligence: a practical introduction to convolutional neural networks for medical professionals," Postgraduate Medical Journal, Oct. 2023, doi: https://doi.org/10.1093/postmj/qgad095.

[3] J. J. Bird and A. Lotfi, "CIFAKE: Image classification and explainable identification of AI-generated synthetic images," IEEE Access, vol. 12, pp. 15642-15650, 2024, doi: 10.1109/ACCESS.2024.3356122.

[4] A. Krizhevsky and G. Hinton, "Learning multiple layers of features from tiny images," University of Toronto, Toronto, ON, Canada, Tech. Rep., 2009.

[5] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, "High-resolution image synthesis with latent diffusion models," in Proc. IEEE/CVF Conf. Comput. Vision and Pattern Recognition (CVPR), New Orleans, LA, USA, 2022, pp. 10674-10685.

[6] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 2016, pp. 770-778.

[7] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, "Densely connected convolutional networks," in Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR), Honolulu, HI, USA, 2017, pp. 2261-2269.

[8] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, "Grad-CAM: Visual explanations from deep networks via gradient-based localization," in Proc. IEEE Int. Conf. Comput. Vision (ICCV), Venice, Italy, 2017, pp. 618-626.
