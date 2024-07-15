#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

class Evaluator:
    def __init__(self, y_test, y_pred):
        self.y_test = y_test
        self.y_pred = y_pred

    def evaluate(self):
        metrics = {
            'accuracy': accuracy_score(self.y_test, self.y_pred),
            'precision': precision_score(self.y_test, self.y_pred),
            'recall': recall_score(self.y_test, self.y_pred),
            'f1_score': f1_score(self.y_test, self.y_pred),
            'roc_auc': roc_auc_score(self.y_test, self.y_pred)
        }
        return metrics


