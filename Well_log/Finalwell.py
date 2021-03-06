# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:58:54 2020

@author: Kipu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:42:57 2020

@author: Kipu
"""


import lasio as ls
import pandas as pd
import matplotlib.pyplot as plt

log = ls.read('F:/Pip/python/2020/1051325649.las')
logs = log.df()

print(logs.columns)
logs = logs[['NPHI', 'CALI', 'GR', 'RHOB','SP', 'RT10', 'RT30', 'RT90']]


logs = logs.reset_index()
logs =logs.rename(columns=({'M__DEPTH':'DEPT'}))
logs=logs.rename(columns=({'DT':'DTC'})) 

logs = logs.dropna()
logs.isnull().any()

print(logs.head())

def plot(logs):
    logs = logs.sort_values(by='DEPT')
    ltop = logs.DEPT.min()
    lbot = logs.DEPT.max()
    
    plt.style.use('default')
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(9,40), sharey=True)
    fig.suptitle("Well log", fontsize=30)
    fig.subplots_adjust(top = 0.80, wspace=0.1)
    
    ax[0].grid()
    ax[1].grid()
    ax[2].grid()
    ax[0].invert_yaxis()
    
    #track 1
    ax01 = ax[0].twiny()
    #ax01.invert_yaxis()
    ax01.plot(logs.GR, logs.DEPT, color='g', linestyle='-')
    ax01.set_xlim(0,180)
    ax01.set_xlabel('GR', color='black')
    ax01.tick_params(axis='x', color='black')
    ax01.spines['top'].set_position(('outward',1))
    ax01.legend(['GR'], loc=(0,1.1))
    
    ax11 = ax[0].twiny()
    #ax11.invert_yaxis()
    ax11.plot(logs.CALI, logs.DEPT, color='black', linestyle='--')
    ax11.set_xlim(6,12)
    ax11.set_xlabel('CALI', color='black')
    ax11.tick_params(axis='x', color='black')
    ax11.spines['top'].set_position(('outward',55))
    ax11.legend(['CALI'], loc=(0,1.12))
                
    ax111 = ax[0].twiny()
    #ax111.invert_yaxis()
    ax111.plot(logs.SP, logs.DEPT, color='yellow', linestyle='-')
    ax111.set_xlim(-100,100)
    ax111.set_xlabel('bitsize', color='black')
    ax111.tick_params(axis='x', color='black')
    ax111.spines['top'].set_position(('outward',105))
    ax111.legend(['SP'], loc=(0,1.14))
    
    #track 2
    
    ax02 = ax[1].twiny()
    #ax02.invert_yaxis()
    ax02.semilogx(logs.RT10, logs.DEPT, color='black', linestyle='dotted')
    ax02.set_xlim(1,1000)
    ax02.set_xlabel('R10', color='black')
    ax02.tick_params(axis='x', color='black')
    ax02.spines['top'].set_position(('outward',1))
    ax02.grid(True, which='both')
    ax02.legend(['RT30'], loc=(0,1.1))
    
    ax22 = ax[1].twiny()
    #ax22.invert_yaxis()
    ax22.semilogx(logs.RT30, logs.DEPT, color='black', linestyle='--')
    ax22.set_xlim(1,1000)
    ax22.set_xlabel('RT30', color='black')
    ax22.tick_params(axis='x', color='black')
    ax22.spines['top'].set_position(('outward',55))
    ax22.legend(['RT30'], loc=(0,1.12))
    
    ax222 = ax[1].twiny()
    #ax222.invert_yaxis()
    ax222.semilogx(logs.RT90, logs.DEPT, color='black', linestyle='-')
    ax222.set_xlim(1,1000)
    ax222.set_xlabel('RT90', color='black')
    ax222.tick_params(axis='x', color='black')
    ax222.spines['top'].set_position(('outward',105))
    ax222.legend(['RT90'], loc=(0,1.14))

    
    #track 3
    
    ax03 = ax[2].twiny()
    #ax03.invert_yaxis()
    ax03.plot(logs.RHOB, logs.DEPT, color='red', linestyle='-')
    ax03.set_xlim(2.8,1.8)
    ax03.set_xlabel('RHOB', color='black')
    ax03.tick_params(axis='x', color='black')
    ax03.spines['top'].set_position(('outward',1))
    ax03.legend(['RHOB'], loc=(0,1.1))
    
    ax33 = ax[2].twiny()
    #ax33.invert_yaxis()
    ax33.plot(logs.NPHI, logs.DEPT, color='blue', linestyle='-')
    ax33.set_xlim(-0.06,0.54)
    ax33.set_xlabel('NPHI', color='black')
    ax33.tick_params(axis='x', color='black')
    ax33.spines['top'].set_position(('outward',105))
    ax33.legend(['NPHI'], loc=(0,1.12))
    
#Smoothing the graph    
loglst = list(logs)

logs = logs.copy(deep=True)
window = 17
for i in loglst:
    logs[i] = pd.Series(logs[i]).rolling(window=window, min_periods=1).mean()

#plot the graph    
plot(logs)
