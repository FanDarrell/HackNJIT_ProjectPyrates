# This code trains a model and uses it to predict risk of piracy

import os
import torch
import torchvision as tv
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch.autograd import Variable
from sklearn.preprocessing import LabelEncoder as le
import seaborn as sns
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")


class Model:

    def __init__(self):

        traind = pd.read_csv("C:\\Users\\Dan\\fallhack2023\\pirate_attacks.csv")
        targets_df = pd.DataFrame(data=traind)

        longi = targets_df['longitude'].to_numpy()
        latti = targets_df['latitude'].to_numpy()
        targets_df['Attack_type'] = le().fit_transform(targets_df['attack_type'])


        longload = torch.from_numpy(longi)
        lattload = torch.from_numpy(latti) 
        piracload = torch.from_numpy(targets_df['Attack_type'].to_numpy()) 


        Xdat = targets_df[['longitude', 'latitude', 'shore_distance', 'shore_latitude', 'shore_longitude']].to_numpy()

        Ydat = targets_df['Attack_type'].to_numpy()


        self.reg_model = linear_model.LinearRegression()
        self.reg_model = LinearRegression().fit(Xdat, Ydat)

        

        


    def predpiracy(self, long, lat):
        
        d = {'longitude': [long], 'latitude': [lat], 'shore_distance': [100], 'shore_latitude': [50], 'shore_longitude': [50]}
        dfwork = pd.DataFrame(data=d)

        pirates = self.reg_model.predict(dfwork)

        return pirates
