#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

def plot_confusion_matrix(y_test, y_pred, filename):
    conf_matrix = plot_confusion_matrix(y_test, y_pred)
    disp = ConfunsionMatrixDisplay(confusion_matrix=conf_matrix)
    disp.plot()
    plt.savefig(filename)
    plt.close()

