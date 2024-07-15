#!/usr/bin/env python
# -*- coding: utf-8 -*-

# main.py
import mlflow
from data_loader import DataLoader
from data_preprocessor import DataPreprocessor
from model_trainer import ModelTrainer
from evaluator import Evaluator
from utils import plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def treinar_modelo(algoritmo, colunas_selecionadas, caminho_dados):
    mlflow.set_experiment("Exemplo_SOLID_ML_Model")

    data_loader = DataLoader(caminho_dados)
    df = data_loader.load_data()

    preprocessor = DataPreprocessor(df)
    X_train, X_test, y_train, y_test = preprocessor.preprocess_data(colunas_selecionadas)

    if algoritmo == 'RandomForest':
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    elif algoritmo == 'LogisticRegression':
        model = LogisticRegression()
    else:
        raise ValueError("Algoritmo não suportado: escolha 'RandomForest' ou 'LogisticRegression'")

    model_trainer = ModelTrainer(model)

    with mlflow.start_run():
        model_trainer.train(X_train, y_train)
        y_pred = model_trainer.predict(X_test)

        evaluator = Evaluator(y_test, y_pred)
        metrics = evaluator.evaluate()

        for metric_name, metric_value in metrics.items():
            mlflow.log_metric(metric_name, metric_value)

        plot_confusion_matrix(y_test, y_pred, "confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png")

        mlflow.sklearn.log_model(model, f"{algoritmo}_model")

    mlflow.end_run()

if __name__ == "__main__":
    treinar_modelo('RandomForest', ['col1', 'col2', 'Data_col'], 'caminho_para_dados.csv')

