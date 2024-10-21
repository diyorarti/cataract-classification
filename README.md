# Cataract Classification Project
## Project Overview: 
The Cataract Classification project is a deep learning application designed to classify cataract images using a Convolutional Neural Network (CNN). The project pipeline automates the process from data ingestion to model training and evaluation, deploying a pre-trained VGG16 model to expedite the process. The application is developed in Python, utilizing various libraries like TensorFlow and Flask for model development and deployment.

This project follows a modular structure that allows data ingestion, model preparation, training, and evaluation to be handled separately, ensuring flexibility and scalability for future improvements. Additionally, this project is integrated with DVC (Data Version Control) to track the various stages of the pipeline and model evolution over time.

## Project Folder Structure:
```bash
.
├── .dvc/
├── .github/workflows/
├── .gitignore
├── artifacts/
│   ├── data_ingestion/
│   │   ├── data.zip
│   │   ├── train/
│   │   ├── immature/
│   │   └── mature/
│   ├── prepare_base_model/
│   │   ├── base_model.h5
│   │   └── base_model_updated.h5
├── config/
│   ├── config.yaml
├── research/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_prepare_base_model.ipynb
│   ├── 03_prepare_callbacks.ipynb
│   ├── 04_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── trials.ipynb
├── src/
│   ├── CataractClassifier/
│   │   ├── components/
│   │   │   ├── data_ingestion.py
│   │   │   ├── evaluation.py
│   │   │   ├── prepare_base_model.py
│   │   │   ├── prepare_callbacks.py
│   │   │   └── training.py
│   │   ├── config/
│   │   │   └── configuration.py
│   │   ├── constants/
│   │   │   └── __init__.py
│   │   ├── entity/
│   │   │   └── config_entity.py
│   │   ├── pipeline/
│   │   │   ├── predict.py
│   │   │   ├── stage_01_data_ingestion.py
│   │   │   ├── stage_02_prepare_base_model.py
│   │   │   ├── stage_03_training.py
│   │   │   └── stage_04_evaluation.py
│   │   ├── utils/
│   │   │   ├── common.py
│   │   └── templates/
│   │       └── index.html
├── .dvcignore
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── dvc.yaml
├── inputImage.jpg
├── main.py
├── params.yaml
├── requirements.txt
├── scores.json
└── setup.py
```
## Key Features:

1. **Data Ingestion**: Automates the process of downloading and unzipping the dataset, which is sourced from a URL.
2. **Model Preparation**: Utilizes a pre-trained VGG16 model for transfer learning. The base model is modified to adapt to the specific number of classes for cataract classification.
3. **Training**: Trains the model using image augmentation and handles checkpointing with TensorBoard integration for logging metrics.
4. **Evaluation**: Evaluates the trained model and logs metrics such as accuracy and loss.
5. **Prediction API**: A Flask-based API is built to allow real-time predictions via a web interface.
