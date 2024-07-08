#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col
from abc import ABC, abstractmethod

# Inicializacao da sessao Spark
spark = SparkSession.builder.appName("DataManagementSystem").getOrCreate()

# SRP: Classe responsavel por carregar os dados
class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> DataFrame:
        # Carregar dados de um arquivo csv
        df = spark.read.csv(self.file_path, header = True, inferschema = True)
        return df

# SRP: Classe responsavel por limpar os dados
class DataCleaner:
    def __init__(self, df: DataFrame):
        self.df = df

    def drop_duplicates(self) -> DataFrame:
        # Remove as duplicadas
        return self.df.dropDuplicates()
    
    def fill_missing_values(self, fill_value: dict) -> DataFrame:
        # Remove valores nulos
        return self.df.fillna(fill_value)

# OCP: Classe responsavel por realizar transformacoes especificas nos dados
class DataTransformer(ABC):
    def __init__(self, df: DataFrame):
        self.df = df

    @abstractmethod
    def transform(self) -> DataFrame:
        pass


class ColumnRenamer(DataTransformer):
    def __init__(self, df: DataFrame, old_name: str, new_name:str):
        super().__init__(df)
        self.old_name = old_name
        self.new_name = new_name

    def transform(self) -> DataFrame:
        # Renomeia uma coluna
        return self.df.withColumnRenamed(self.old_name, self.new_name)


class ColumnSelector(DataTransformer):
    def __init__(self, df: DataFrame, columns: list):
        super().__init__(df)
        self.columns = columns

    def transform(self) -> DataFrame:
        # Seleciona colunas especificas
        return self.df.select(*self.columns)


# SRP: Classe responsavel por salvar os dados
class DataSaver(self):
    def __inti__(self, df: DataFrame, output_path: str):
        self.df = df
        self.output_path = output_path

    def save_data(self):
        # Salvando os dados em um arquivo CSV
        self.df.write.csv(self.output_path, header = True, mode = 'overwrite')


# ISP: Interface especifica pra pipeline de dados
class DataPipelineManager(ABC):
    @abstractmethod
    def run_pipeline(self):
        return

# DIP: Implementacao do gerenciamento da pipeline de dados
class SimpleDataPipelineManager(DaraPipelineManager):
    def __init__(self, loader: DataLoader, cleaner: DataCleaner, transformers: list[DataTransformer], saver: DataSaver):
        self.loader = loader
        self.cleaner = cleaner
        self.transformers = transformers
        self.saver = saver

    def run_pipeline(self):
        # Carregar os dados
        df = self.loader.load_data()

        # Limpa os dados
        df = self.cleaner.drop_duplicates()
        df = self.cleaner.fill_missing_values({"column_name": "default_value"})

        # Aplica transformacoes
        for transform in self.transformers:
            df = transformer.transform()

        # Salva os dados processados
        self.saver.save_data()


# Exemplo de uso do sistema
if __name__ == "__main__":
    # Carregar dados de um arquivo CSV
    loader = DataLoader("input_data.csv")

    # Inicializar DataCleaner com DataFrame carregado
    cleaner = DataCleaner(loader.load_data())

    # Inicializar transformadores com DataFrame limpo
    transformers = [
        ColumnRenamer(cleaner.df, "old_column_name", "new_column_name"),
        ColumnSelector(cleaner.df, ["column1", "column2", "new_column_name"])
    ]

    # Inicializa DataSaver com DataFrame transformado
    saver = DataSaver(transformers[-1].transform(), "output_data.csv")

    # Gerenciar e executar a pipeline de dados
    pipeline_manager = SimpleDataPipelineManager(loader, cleaner, transformers, saver)
    pipeline_manager.run_pipeline()

