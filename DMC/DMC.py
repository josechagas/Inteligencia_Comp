from math import sqrt
import numpy as np



__centroids = {}
__choosedParams = {}

def default_dataFormat():
    return {"param_one":"value","param_two":"value","classification":"value"}


def calcCentroidsOf(data,classifications,params):
    __choosedParams["params"] = params
    for classif in classifications:
        centroid ={}
        #variancias = {}

        dataForClassif = None
        for row in data:
            if row["classification"] == classif:
                if dataForClassif is None:
                    dataForClassif = np.array([row])
                else:
                    dataForClassif = np.append(dataForClassif,[row])
                for param in params:
                    try:
                        centroid[param] += row[param]
                    except Exception, e:
                        centroid[param] = row[param]

        for param in params:
            centroid[param] /= len(dataForClassif) #media



        # for classifRow in dataForClassif:
        #     for param in params:
        #         try:
        #             variancias[param] += (classifRow[param] - centroid[param])**2
        #         except Exception, e:
        #             variancias[param] = (classifRow[param] - centroid[param])**2
        #
        # for param in params:
        #     variancias[param] /= len(dataForClassif)

        #__centroids[classif] = {"centroid":centroid,"variancias":variancias}
        __centroids[classif] = {"centroid":centroid}



def classificate(item):
    dists = {}

    belongsTo = ""
    for classif in __centroids:
        #variancia =  __centroids[classif]["variancias"]
        centroid = __centroids[classif]["centroid"]

        distTo = 0
        for param in  __choosedParams["params"]:
            distTo += (item[param] - centroid[param])**2

        dists[classif] = sqrt(distTo)

        try:
            if dists[classif] < dists[belongsTo]:
                belongsTo = classif
        except Exception, e:
            belongsTo = classif


    return belongsTo
    #print(__choosedParams)



