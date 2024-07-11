import mlflow
import mlflow.spark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline as SparkPipeline
from pyspark.sql.types import StringType

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.spark = SparkSession.builder.appName("HeartDiseasePrediction").getOrCreate()

    def load_data(self):
        df = self.spark.read.csv(self.file_path, header=True, inferSchema=True)
        print(f"Data loaded with {df.count()} rows and {len(df.columns)} columns")
        return df

class DataCleaner:
    def clean_data(self, df):
        # Substituir valores nulos por valores padrão
        df_filled = df.fillna({
            'age': 0, 'sex': 0, 'cp': 0, 'trestbps': 0, 'chol': 0, 'fbs': 0,
            'restecg': 0, 'thalch': 0, 'exang': 0, 'oldpeak': 0, 'slope': 0,
            'ca': 0, 'thal': 0, 'num': 0  # Ajustado de 'target' para 'num'
        })

        # Remover linhas que ainda possam conter valores nulos
        df_cleaned = df_filled.dropna()

        # Consertar tipos de dados
        df_cleaned = df_cleaned.withColumn("sex", col("sex").cast("integer"))
        df_cleaned = df_cleaned.withColumn("cp", col("cp").cast("integer"))
        df_cleaned = df_cleaned.withColumn("fbs", col("fbs").cast("integer"))
        df_cleaned = df_cleaned.withColumn("restecg", col("restecg").cast("integer"))
        df_cleaned = df_cleaned.withColumn("exang", col("exang").cast("integer"))
        df_cleaned = df_cleaned.withColumn("slope", col("slope").cast("integer"))
        df_cleaned = df_cleaned.withColumn("ca", col("ca").cast("integer"))
        df_cleaned = df_cleaned.withColumn("thal", col("thal").cast("integer"))

        # Verificar a quantidade de linhas após a limpeza
        print(f"Data cleaned with {df_cleaned.count()} rows remaining")

        return df_cleaned

class FeatureEngineer:
    def __init__(self, feature_columns, label_column):
        self.feature_columns = feature_columns
        self.label_column = label_column

    def transform(self, df):
        # Verificar as colunas presentes
        print("Colunas disponíveis no DataFrame:", df.columns)

        # Codificar variáveis categóricas
        indexers = [StringIndexer(inputCol=column, outputCol=column + "_index").fit(df)
                    for column in self.feature_columns if df.schema[column].dataType == StringType()]

        # Vector Assembler
        assembled_cols = [col + "_index" if col + "_index" in df.columns else col for col in self.feature_columns]
        assembler = VectorAssembler(inputCols=assembled_cols, outputCol="features")

        # Padronizar os dados
        scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")

        pipeline_stages = indexers + [assembler, scaler]
        pipeline = SparkPipeline(stages=pipeline_stages)

        df_transformed = pipeline.fit(df).transform(df)
        print(f"Data transformed with {df_transformed.count()} rows")

        return df_transformed.select("scaledFeatures", self.label_column)

class ModelTrainer:
    def __init__(self, model):
        self.model = model

    def train(self, df):
        print("Training model...")
        return self.model.fit(df)

class Pipeline:
    def __init__(self, data_loader, data_cleaner, feature_engineer, model_trainer):
        self.data_loader = data_loader
        self.data_cleaner = data_cleaner
        self.feature_engineer = feature_engineer
        self.model_trainer = model_trainer

    def run(self):
        mlflow.start_run()

        # Step 1: Load Data
        data = self.data_loader.load_data()

        # Step 2: Clean Data
        cleaned_data = self.data_cleaner.clean_data(data)

        # Step 3: Feature Engineering
        feature_data = self.feature_engineer.transform(cleaned_data)
        if feature_data.count() == 0:
            raise ValueError("No data available after feature engineering.")

        # Step 4: Train Model
        model = self.model_trainer.train(feature_data)

        # Log the model
        mlflow.spark.log_model(model, "model")

        mlflow.end_run()

        return model

if __name__ == "__main__":
    file_path = "/home/vicrrs/Projetos_github/exercicios_python/UCIHeartDiseaseData/data/heart_disease_uci.csv"
    feature_columns = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalch",  # Ajustado de 'thalach' para 'thalch'
        "exang", "oldpeak", "slope", "ca", "thal"
    ]
    label_column = "num"  # Ajustado de 'target' para 'num'

    data_loader = DataLoader(file_path)
    data_cleaner = DataCleaner()
    feature_engineer = FeatureEngineer(feature_columns, label_column)
    logistic_regression = LogisticRegression(labelCol=label_column, featuresCol="scaledFeatures")
    model_trainer = ModelTrainer(logistic_regression)

    pipeline = Pipeline(data_loader, data_cleaner, feature_engineer, model_trainer)
    trained_model = pipeline.run()

    print("Model trained and logged successfully with MLflow!")
