#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mlflow
from data_loader import DataLoader
from data_preprocessor import DataPreprocessor
from model_trainer import ModelTrainer
from evaluator import Evaluator
from sklearn.linear_model import LogisticRegression

def train_model(algoritmo, colunas_selecionadas, caminho_dados):
    mlflow.set_experiment("Exemplo_SIMPLIFICADO_ML_MODEL")

    data_loader = DataLoader(caminho_dados)
    df = data_loader.load_data()

    preprocessor = DataPreprocessor(df)
    X_train, X_test, y_train, y_test = preprocessor.preprocess_data(colunas_selecionadas)

    if algoritmo == 'LogisticRegression':
        model = LogisticRegression()
    else:
        raise ValueError("Algoritmo não suportado: escolha 'LogisticRegression'")

    model_trainer = ModelTrainer(model)

    with mlflow.start_run():
        model_trainer.train(X_train, y_train)
        y_pred = model_trainer.predict(X_test)

        evaluator = Evaluatory(y_test, y_pred)
        metrics = evaluator.evaluate()

        for metric_name, metric_value in metrics.items():
            mlflow.log_metric(metric_name, metric_value)

    mlflow.end_run()

if __name__ == "__main__":
    train_model('LogisticRegression', ['feature1', 'feature2'], 'caminho_para/arquivo.csv')

