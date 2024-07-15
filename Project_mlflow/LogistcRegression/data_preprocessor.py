#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

class DataPreprocessor:
    def __init__(self, df):
        self.df = df

    def preprocess_data(self, selected_columns):
        X = self.df[selected_columns]
        y = self.df['target']
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

