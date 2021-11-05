
import sys,time
import pandas
import sklearn


### Function to read data and labels
def loadDatasetsFromFiles (DataFileName, LabelsFileName, Path="./", Separator=" ", Header=None):

    print("Loading datasets from files in %s: " % Path, end=""); sys.stdout.flush()
    itime = time.time()

    # Load raw data and convert to numpy.array
    pathData = Path + DataFileName
    print(" %s" % DataFileName, end=""); sys.stdout.flush()
    dfData = pandas.read_csv(pathData,sep=Separator+"+",header=Header,engine='python')
    Data = dfData.values.astype(float)

    # Load labels and convert to numpy.array
    pathLabels= Path + LabelsFileName
    print(" %s" % LabelsFileName, end=""); sys.stdout.flush()
    dfLabels = pandas.read_csv(pathLabels,sep=Separator+"+",header=Header,engine='python')
    Labels = dfLabels.values.astype(float)

    print("  took %.1fs" % (time.time()-itime))
    return Data, Labels


### Function to convert labels to 1-of-C (one-hot) labels
def convertLabels_1ofC_Scheme (vLabels):
    from sklearn.preprocessing import OneHotEncoder
    Encoder = OneHotEncoder()
    ### Assumes that in vLabels we have at least one label of each class
    Encoder.fit(vLabels.reshape(-1,1))
    Labels = Encoder.transform(vLabels.reshape(-1,1)).toarray()

    return Labels


### Function to scale the data to mean 0 and stddev 1
def scaleDataMean0Dev1Scaler (Data):
    ### StandardScaler from sklearn
    from sklearn.preprocessing import StandardScaler
    Scaler = StandardScaler()
    Scaler.fit(Data)
    scaledData = Scaler.transform(Data)
    return scaledData, Scaler


### Function to scale the data in FeatureRange
def scaleDataMinMaxScaler (Data, FeatureRange=(0,1)):
    ### MinMaxScaler from sklearn
    from sklearn.preprocessing import MinMaxScaler
    Scaler = MinMaxScaler(feature_range=FeatureRange)
    Scaler.fit(Data)
    scaledData = Scaler.transform(Data)
    return scaledData, Scaler
