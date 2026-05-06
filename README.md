# CS3 by Angad Brar | Code and Results from KALz - Project 3 by Angad Brar, Kendall Freese, Lily Spyredes

## Repository Map

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
├── case_study/
│   ├── Angad_CS3_Hook.pdf
│   ├── Angad_CS3_Rubric.pdf
│   └── materials_and_references.md
├── .gitignore
├── LICENSE.md
├── README.md
└── requirements.txt
```

> [!NOTE]
> The `data/` folder and model checkpoint files are large. They are not meant to be recreated manually file-by-file in Google Drive. Keep the dataset as a single zip in Google Drive, copy that one zip into Colab local storage, unzip locally, and save outputs back to Google Drive.

## CS3 Case Study Package

The `case_study/` folder contains the CS3 package for turning this project into a case study:

- `Angad_CS3_Hook.pdf`: hook document with background information.
- `Angad_CS3_Rubric.pdf`: student-facing rubric source with info on materials / task.

## Final Model Results

Both models exceeded the project goal of 80% test accuracy and surpassed the 92.98% baseline reported by Bird and Lotfi.

| Model | Test Accuracy | Precision | Recall | F1 | Test Size |
|---|---:|---:|---:|---:|---:|
| ResNet-50 | 0.9692 | 0.9693 | 0.9692 | 0.9692 | 20,000 |
| DenseNet-121 | 0.9697 | 0.9700 | 0.9697 | 0.9697 | 20,000 |

DenseNet-121 was the best model by test accuracy, but only by 0.05 percentage points, so both pretrained CNN architectures performed similarly well on CIFAKE.

## References

[1] C. Vaccari and A. Chadwick, "Deepfakes and disinformation: Exploring the impact of synthetic political video on deception, uncertainty, and trust in news," Social Media + Society, vol. 6, no. pp. 1-13, 2020, doi: 10.1177/2056305120903408.

[2] G. Kourounis, A. Elmahmudi, B. Thomson, J. Hunter, H. Ugail, and C. Wilson, "Computer image analysis with artificial intelligence: a practical introduction to convolutional neural networks for medical professionals," Postgraduate Medical Journal, Oct. 2023, doi: https://doi.org/10.1093/postmj/qgad095.

[3] J. J. Bird and A. Lotfi, "CIFAKE: Image classification and explainable identification of AI-generated synthetic images," IEEE Access, vol. 12, pp. 15642-15650, 2024, doi: 10.1109/ACCESS.2024.3356122.

[4] A. Krizhevsky and G. Hinton, "Learning multiple layers of features from tiny images," University of Toronto, Toronto, ON, Canada, Tech. Rep., 2009.

[5] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, "High-resolution image synthesis with latent diffusion models," in Proc. IEEE/CVF Conf. Comput. Vision and Pattern Recognition (CVPR), New Orleans, LA, USA, 2022, pp. 10674-10685.

[6] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 2016, pp. 770-778.

[7] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, "Densely connected convolutional networks," in Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR), Honolulu, HI, USA, 2017, pp. 2261-2269.

[8] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, "Grad-CAM: Visual explanations from deep networks via gradient-based localization," in Proc. IEEE Int. Conf. Comput. Vision (ICCV), Venice, Italy, 2017, pp. 618-626.