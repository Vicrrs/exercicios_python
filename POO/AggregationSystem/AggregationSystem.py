from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import avg, count, sum
from abc import ABC, abstractmethod

# Inicialização da sessão Spark
spark = SparkSession.builder.appName("AggregationSystem").getOrCreate()

# SRP: Classe responsável por carregar dados
class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> DataFrame:
        # Carrega dados de um arquivo CSV
        df = spark.read.csv(self.file_path, header=True, inferSchema=True)
        return df

# SRP: Classe responsável por limpar dados
class DataCleaner:
    def __init__(self, df: DataFrame):
        self.df = df

    def drop_duplicates(self) -> DataFrame:
        # Remove duplicatas
        return self.df.dropDuplicates()

    def fill_missing_values(self, fill_value: dict) -> DataFrame:
        # Preenche valores nulos
        return self.df.fillna(fill_value)

# OCP: Classe responsável por realizar agregações nos dados
class DataAggregator(ABC):
    def __init__(self, df: DataFrame):
        self.df = df

    @abstractmethod
    def aggregate(self) -> DataFrame:
        pass

class AverageAggregator(DataAggregator):
    def __init__(self, df: DataFrame, group_by_col: str, agg_col: str):
        super().__init__(df)
        self.group_by_col = group_by_col
        self.agg_col = agg_col

    def aggregate(self) -> DataFrame:
        # Agrega calculando a média
        return self.df.groupBy(self.group_by_col).agg(avg(self.agg_col).alias(f"avg_{self.agg_col}"))

class SumAggregator(DataAggregator):
    def __init__(self, df: DataFrame, group_by_col: str, agg_col: str):
        super().__init__(df)
        self.group_by_col = group_by_col
        self.agg_col = agg_col

    def aggregate(self) -> DataFrame:
        # Agrega calculando a soma
        return self.df.groupBy(self.group_by_col).agg(sum(self.agg_col).alias(f"sum_{self.agg_col}"))

# SRP: Classe responsável por salvar dados
class DataSaver:
    def __init__(self, df: DataFrame, output_path: str):
        self.df = df
        self.output_path = output_path

    def save_data(self):
        # Salva dados em um arquivo CSV
        self.df.write.csv(self.output_path, header=True, mode='overwrite')

# ISP: Interface específica para gerenciar a pipeline de dados
class DataPipelineManager(ABC):
    @abstractmethod
    def run_pipeline(self):
        pass

# DIP: Implementação concreta do gerenciador de pipeline de dados
class AggregationPipelineManager(DataPipelineManager):
    def __init__(self, loader: DataLoader, cleaner: DataCleaner, aggregators: list[DataAggregator], saver: DataSaver):
        self.loader = loader
        self.cleaner = cleaner
        self.aggregators = aggregators
        self.saver = saver

    def run_pipeline(self):
        # Carrega os dados
        df = self.loader.load_data()
        
        # Limpa os dados
        df = self.cleaner.drop_duplicates()
        df = self.cleaner.fill_missing_values({"column_name": "default_value"})  # Preencher com valores adequados

        # Aplica agregações
        for aggregator in self.aggregators:
            df = aggregator.aggregate()

        # Salva os dados processados
        self.saver.save_data()

# Exemplo de uso do sistema
if __name__ == "__main__":
    # Carregar dados de um arquivo CSV
    loader = DataLoader("input_data.csv")

    # Inicializar DataCleaner com DataFrame carregado
    cleaner = DataCleaner(loader.load_data())

    # Inicializar agregadores com DataFrame limpo
    aggregators = [
        AverageAggregator(cleaner.df, "group_column", "agg_column"),
        SumAggregator(cleaner.df, "group_column", "agg_column")
    ]

    # Inicializar DataSaver com DataFrame agregado
    saver = DataSaver(aggregators[-1].aggregate(), "output_data.csv")

    # Gerenciar e executar a pipeline de dados
    pipeline_manager = AggregationPipelineManager(loader, cleaner, aggregators, saver)
    pipeline_manager.run_pipeline()
