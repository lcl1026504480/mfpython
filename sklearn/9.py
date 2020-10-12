# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:35:26 2020

@author: lenovouser
"""

from sklearn import datasets
from sklearn import neural_network

mlp = neural_network.MLPClassifier(hidden_layer_sizes=(100,50,10),solver="adam")
iris = datasets.load_iris()
X, y = iris.data, iris.target


mlp.fit(X, y)                         
print (mlp.n_layers_)
print (mlp.n_iter_)
print (mlp.loss_curve_)
