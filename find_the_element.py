#Sasha Safonova
'''
Narrows down the list of possible elements by cross-checking it with calibrated experimental data.
Accompanied by a csv file of spectral wavelengths in Angstroms.
'''
#Last updated on 03.01.16 at 21.12

import pandas as pd
import numpy as np

#--------get data--------------------
pandas=pd.read_csv('allemissionlines.csv', sep=",",header=None)
emissions=pandas.as_matrix()
#[0] = wavelength, [1] = intensity, [2] = element


#------set of experimental wavelengths----------------
unknownA = [6022.746, 5611.302, 5573.898, 5499.09, 5461.686, 5274.666, 5237.262, 5199.858, 5087.646, 4975.434, 4788.414, 4601.394]

#-----error margin in your wavelength estimation------
epsilon=7

possibilities=np.array([])
final=[]
start=False

for lamb in unknownA:
    tempemiss = emissions[(emissions[:,0]>(lamb-epsilon)) & (emissions[:,0]<(lamb+epsilon))& (emissions[:,1]>10)]
    elements = tempemiss[:,2].tolist()
    temp=tempemiss.tolist()
    if start:
        for a in elements:
            a=str(a)
            if a in possibilities:
                temp.append(a)
        possibilities=temp
        temp=[]
    start=True
possibilities=np.asarray(possibilities).T.tolist()

#-------list of elements that could be found in spectral tubes-------
gasses=['H', 'BR', 'HE', 'N', 'S', 'F', 'CL', 'I', 'O', 'SE', 'P', 'C', 'NA', 'XE', 'KR', 'AR']
for element in possibilities[2]:
    if element in gasses:
        final.append(element)
s=set(final)
print sorted(s)
