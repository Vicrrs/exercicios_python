#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransform
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

class DataPreprocessor:
    def __init__(self, df):


