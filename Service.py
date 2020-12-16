from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing import image
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc


class Train:

    def __init__(self):
        images = []
        labels = []
        # provide the name of the folder containing your dataset
        Dataset = "BrainTumorData"
        print(Dataset)
        count = 1
        '''
        format images into matrices, and create array to store inputs
        create respective label array.
        '''
        for entry in os.listdir(Dataset):
            print("{}: {}".format(count, entry))
            for file in os.listdir(Dataset + '/' + entry):
                i = image.load_img(Dataset + '/' + entry + '/' + file)
                iar = image.img_to_array(i.resize((128, 128)))
                iar = iar / 255
                images.append(iar)
                labels.append(count)  # entry
            count = count + 1
        print("finished")
        # convert from a 3D array to a 2D array
        X = np.stack(images, axis=0)
        print("Image Data Shape", X.data.shape)
        X.shape = (X.data.shape[0], X.data.shape[1] * X.data.shape[2] * X.data.shape[3])
        print("Image Data Shape", X.data.shape)
        # split into training and test data
        self.x_train, x_test, self.y_train, y_test = train_test_split(X, labels, test_size=0.0)
        self.scaler = StandardScaler()
        # Fit on training set only.
        self.scaler.fit(self.x_train)
        # Apply transform to both the training set and the test set.
        self.x_train = self.scaler.transform(self.x_train)
        self.pca = PCA(.85)
        self.pca.fit(self.x_train)
        self.x_train = self.pca.transform(self.x_train)
        print("Finished Splitting Training and Test Data")
        self.Algorithm = LogisticRegression(solver='lbfgs')
        self.Algorithm.fit(self.x_train, self.y_train)
        print("trained")


    def request(self, text):
        # NLP
        text = self.scaler.transform(text)
        result = self.Algorithm.predict(self.pca.transform(text))
        print(result)
        return result