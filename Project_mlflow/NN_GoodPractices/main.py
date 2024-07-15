#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mlflow
from data_loader import DataLoader
from data_preprocessor import DataPreprocessor
from model_trainer import NeuralNetworkTrainer
from evaluator import Evaluator
from utils import plot_confusion_matrix

def treinar_modelo(algoritmo, colunas_selecionadas, caminho_dados, **kwargs):
    mlflow.set_experiment("Exemplo_SOLID_Neural_Network")

    data_loader = DataLoader(caminho_dados)
    df = data_loader.load_data()

    preprocessor = DataPreprocessor(df)
    X_train, X_test, y_train, y_test = preprocessor.preprocess_data(colunas_selecionadas)

    if algoritmo == 'NeuralNetwork':
        input_dim = X_train.shape[1]
        layers = kwargs.get('layers', [64, 64])
        learning_rate = kwargs.get('learning_rate', 0.001)
        epochs = kwargs.get('epochs', 10)
        model_trainer = NeuralNetworkTrainer(input_dim=input_dim, layers=layers, learning_rate=learning_rate)
    else:
        raise ValueError("Algoritmo não suportado: escolha 'NeuralNetwork'")

    with mlflow.start_run():
        model_trainer.train(X_train, y_train, epochs=epochs)
        y_pred = model_trainer.predict(X_test)

        evaluator = Evaluator(y_test, y_pred)
        metrics = evaluator.evaluate()

        for metric_name, metric_value in metrics.items():
            mlflow.log_metric(metric_name, metric_value)

        plot_confusion_matrix(y_test, y_pred, "confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png")

        mlflow.keras.log_model(model_trainer.model, f"{algoritmo}_model")

    mlflow.end_run()

if __name__ == "__main__":
    treinar_modelo('NeuralNetwork', ['col1', 'col2', 'Data_col'], 'caminho_para_dados.csv', layers=[128, 64], learning_rate=0.001, epochs=20)

