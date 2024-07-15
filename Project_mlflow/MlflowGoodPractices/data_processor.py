#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

class DataPreprocessor:
    def __init__(self, df):
        self.df = df

    def preprocess_data(self, selected_columns):
        self.df = self.transform_dates(selected_columns)

        x = self.df[selected_columns]
        y = self.df['target'].apply(lambda x: 1 if == 'positive' else 0)

        categorical_features = [col for col in selected_columns if self.df[col].dtype == 'object']
        numeric_features = [col for col in selected_columns if col not in categorical_features]

        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        X_processed = preprocessor.fit_transform(X)

        return train_test_split(X_processed, y, test_size=0.2, random_state=42)

    def transform_dates(self, selected_columns):
        date_columns = [col for col in selected_columns if 'date' in col]
        for col in date_columns:
            selfdf[col] = pd.to_datetime(self.df[col])
            self.df[f'{col}_year'] = self.df[col].dt.year
            self.df[f'{col}_month'] = self.df[col].dt.month
            self.df[f'{col}_day'] = self.df[col].day
        return self.df

