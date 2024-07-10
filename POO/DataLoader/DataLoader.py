#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline as SparkPipeline

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.spark = SparkSession.builder.appName("DataLoader").getOrCreate()

    def load_data(self):
        return self.spark.read.csv(self.file_path, header=True, inferSchema=True)

class DataCleaner:
    def clean_data(self, df):
        df_cleaned = df.dropna()
        return df_cleaned

class FeatureEngineer:
    def __init__(self, feature_columns, label_column):
        self.feature_columns = feature_columns
        self.label_column = label_column

    def transform(self, df):
        assembler = VectorAssembler(inputCols=self.feature_columns, outputCol="features")
        df_transformed = assembler.transform(df).select("features", self.label_column)
        return df_transformed

class ModelTrainer:
    def __init__(self, model):
        self.model = model

    def train(self, df):
        return self.model.fit(df)

class Pipeline:
    def __init__(self, data_loader, data_cleaner, feature_engineer, model_trainer):
        self.data_loader = data_loader
        self.data_cleaner = data_cleaner
        self.feature_engineer = feature_engineer
        self.model_trainer = model_trainer

    def run(self):
        # Load data
        data = self.data_loader.load_data()

        # Clean data
        cleaned_data = self.feature_engineer.transform(clean_data)

        # Train Model
        model = self.model_trainer.train(feature_data)

        return model

if __name__ == "__main__":
    file_path = "path/to/your/data.csv"
    feature_columns = ["feature1", "feature2", "feature3"]  # Replace with your actual feature columns
    label_column = "label"  # Replace with your actual label column

    data_loader = DataLoader(file_path)
    data_cleaner = DataCleaner()
    feature_engineer = FeatureEngineer(feature_columns, label_column)
    logistic_regression = LogisticRegression(labelCol=label_column, featuresCol="features")
    model_trainer = ModelTrainer(logistic_regression)
    
    pipeline = Pipeline(data_loader, data_cleaner, feature_engineer, model_trainer)
    trained_model = pipeline.run()
    
    print("Model trained successfully!")

