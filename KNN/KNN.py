from math import sqrt
import numpy as np

Hamming_Distance = 1
Euclidian_Distance = 2




def default_dataFormat():
    return {"param_one":"value","param_two":"value","classification":"value"}

def default_dataToTestFormat():
    return {"param_one":"value","param_two":"value"}

def euclidianDistanceOf(one,two):
    return sqrt((one[0]-two[0])**2) + ((one[1]-two[1])**2)


def __distanceOf(one,two):
    return euclidianDistanceOf(one, two)

def __sort(nearest):

    for l in range(0,len(nearest)-1, 1):
        l_near = nearest[l].copy()
        for r in range(l+1,len(nearest), 1):
            r_near = nearest[r].copy()
            if l_near["distance"] > r_near["distance"]:
                nearest[l], nearest[r] = nearest[r], nearest[l]
                l_near = nearest[l].copy()

    return nearest



def classificate(item,data,k,param_one_key='param_one',param_two_key='param_two'
                 ,classification_key='classification'):
    distances = None #{distance:value,classification:value}
    classificByQuant = {}#None #[{"classification":name,"quant":value}]

    currentClassification = None
    for row in data:
        distance =  __distanceOf((item[param_one_key],item[param_two_key]),
                                 (row[param_one_key],row[param_two_key]))
        if distances is None:
            distances = np.array([{"distance": distance, "classification": row[classification_key]}])
            classificByQuant[row[classification_key]] = 1
        else:
            if len(distances) < k:
                distances = np.append(distances, [{"distance": distance, "classification": row[classification_key]}])
                try:
                    classificByQuant[row[classification_key]] += 1
                except Exception, e:
                    classificByQuant[row[classification_key]] = 1

            else:
                distances = __sort(distances)
                last = distances[k - 1]
                if last["distance"] > distance:
                    classificByQuant[last["classification"]] -= 1
                    distances = np.delete(distances,k - 1)
                    distances = np.insert(distances,k - 1,[{"distance": distance, "classification": row[classification_key]}])
                    try:
                        classificByQuant[row[classification_key]] += 1
                    except Exception, e:
                        classificByQuant[row[classification_key]] = 1


        if currentClassification is None:
            currentClassification = row[classification_key]
        else:
            try:
                if classificByQuant[row[classification_key]] > classificByQuant[currentClassification]:
                    currentClassification = row[classification_key]
            except Exception, e:
                continue


    distances = __sort(distances)

    return {"k-nearests":distances,"item-classification":currentClassification}

