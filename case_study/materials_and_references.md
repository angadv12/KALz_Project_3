# Materials and References

## Repository Materials

- README.md: setup path, repository map, Colab workflow, final metrics, and references.
- scripts/01_EDA.py: local EDA for class balance, samples, image size, brightness, and pixel variance.
- scripts/02_03_04_preprocess_training.ipynb: preprocessing, ResNet-50 training, DenseNet-121 training, and checkpoint saving.
- scripts/05_06_07_eval_gradcam_report.ipynb: test evaluation, confusion matrices, Grad-CAM, and summary reporting.
- output/evaluation/: classification reports, prediction files, confusion matrices, and metrics_summary.csv.
- output/gradcam/: model-specific Grad-CAM example figures.

## Suggested Hard-Copy Sources

- Explainer: Google DeepMind, Identifying AI-generated images with SynthID. This gives students a readable entry point into AI image identification and watermarking.
- Technical article: Bird and Lotfi, CIFAKE: Image Classification and Explainable Identification of AI-Generated Synthetic Images. This explains the dataset and baseline that the project uses.

## References

- Bird, J. J., and Lotfi, A. (2024). CIFAKE: Image Classification and Explainable Identification of AI-Generated Synthetic Images. IEEE Access. https://doi.org/10.1109/ACCESS.2024.3356122
- CIFAKE dataset. https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images
- Google DeepMind. Identifying AI-generated images with SynthID. https://deepmind.google/discover/blog/identifying-ai-generated-images-with-synthid/
- Vaccari, C., and Chadwick, A. (2020). Deepfakes and Disinformation. Social Media + Society. https://doi.org/10.1177/2056305120903408
- Kourounis, G., Elmahmudi, A., Thomson, B., Hunter, J., Ugail, H., and Wilson, C. (2023). Computer image analysis with artificial intelligence. Postgraduate Medical Journal. https://doi.org/10.1093/postmj/qgad095
- He, K., Zhang, X., Ren, S., and Sun, J. (2016). Deep Residual Learning for Image Recognition. CVPR. https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html
- Huang, G., Liu, Z., van der Maaten, L., and Weinberger, K. Q. (2017). Densely Connected Convolutional Networks. CVPR. https://openaccess.thecvf.com/content_cvpr_2017/html/Huang_Densely_Connected_Convolutional_CVPR_2017_paper.html
- Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., and Batra, D. (2017). Grad-CAM. ICCV. https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html

## Print Packet Checklist

- Place the one-page hook document on the left front of the manila folder.
- Place the student rubric behind the hook document.
- Print the SynthID explainer and the CIFAKE article or article landing page for the right side.
- Submit the GitHub repository link on Canvas. The physical folder still needs to go to SDS room 436.
