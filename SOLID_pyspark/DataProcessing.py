#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml import Pipeline

class DataReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_data(self):
        spark = SparkSession.builder.appName("DataProcessing").getOrCreate()
        return spark.read.csv(self.file_path, header=True, inferSchema=True)

class DataCleaner:
    def __init__(self, data):
        self.data = data

    def clead_data(self):
        # Removend valores nulos
        self.data = self.data.dropna()
        return self.data

class DataTransformer:
    def __init__(self, data):
        self.data = data

    def transform_data(self, feature_columns, target_column):
        assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
        self.data = assembler.transform(self.data)
        self.data = self.data.select(col("features"), col(target_column).alias("label"))
        return self.data

class DataNormalizer:
    def __init__(self, data):
        self.data = data

    def normalize_data(self):
        scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures", withStd=True, withMean=False)
        self.data = scaler.fit(self.data).transform(self.data)
        return self.data

class DataSplitter:
    def __init__(self, data):
        self.data = data

    def split_data(self, train_ratio=0.8):
        train_data, test_data = self.data.randomSplit([train_ratio, 1 - train_ratio])
        return train_data, test_data

# Princípio aberto/fechado: as classes estão abertas para extensão, mas fechadas para modificação.
class DataProcessor:
    def __init__(self, file_path, feature_columns, target_column):
        self.file_path = file_path
        self.feature_columns = feature_columns
        self.target_column = target_column

    def process_data(self):
        reader = DataReader(self.file_path)
        data = reader.read_data()

        cleaner = DataCleaner(data)
        data = cleaner.clean_data()

        transform = DataTransformer(data)
        data = transform.transform_data(self.feature_columns, self.target_column)

        normalizer = DataNormalizer(data)
        data = normalizer.normalize_data()

        splitter = DataSplitter(data)
        train_data, test_data = splitter.split_data()

        return train_data, test_data

# Princípio da substituição de Liskov: as subclasses devem ser substituíveis por suas superclasses.
# Princípio da segregação de interfaces: as interfaces devem ser específicas para o cliente.
# Princípio da inversão de dependência: as dependências devem ser abstrações, não implementações.

# Exemplo de uso:
if __name__ == "__main__":
    file_path = "data.csv"
    feature_columns = ["feature1", "feature2", "feature3"]
    target_column = "target"

    processor = DataProcessor(file_path, feature_columns, target_column)
    train_data, test_data = processor.process_data()

    train_data.show()
    test_data.show()

