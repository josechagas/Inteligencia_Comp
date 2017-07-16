import DMC as dmc
import numpy as np


# You can find this data set at https://archive.ics.uci.edu/ml/datasets/Iris


sepal_length='sepal_length'
sepal_width='sepal_width'
petal_length='petal_length'
petal_width='petal_width'
classification='classification'

training_file = 'iris.data(training).txt'
dataset_file = 'iris.data.txt'
examples_file = 'Examples(From Original Data).txt'

def get_and_formate_Data(fileName):
    training = f = open(fileName, 'r')
    data = None#np.array()#np.empty(1)
    for line in training:
        rowArray = line.replace('\n','').split(',')
        if len(rowArray) == 5:
            if data is None:
                data = np.array([{sepal_length: float(rowArray[0]), sepal_width: float(rowArray[1]),
                                         petal_length: float(rowArray[2]), petal_width: float(rowArray[3]),
                                         classification: rowArray[4]}])
            else:
                data = np.append(data, [{sepal_length: float(rowArray[0]), sepal_width: float(rowArray[1]),
                                     petal_length: float(rowArray[2]), petal_width: float(rowArray[3]),
                                     classification: rowArray[4]}])

    #print(data)
    return data



def main():
    #print(dmc.default_dataFormat())
    #print(dmc.default_dataToTestFormat())

    param_one = petal_width
    param_two = petal_length

    training_data = get_and_formate_Data(training_file)

    examples_data = get_and_formate_Data(examples_file)

    dmc.calcCentroidsOf(training_data,["Iris-setosa","Iris-versicolor","Iris-virginica"],[petal_length,petal_width])

    item = examples_data[16]

    print(item)

    print(dmc.classificate(item))

main()