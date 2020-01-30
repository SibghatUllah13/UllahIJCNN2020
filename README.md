
# VRNNs-for-Clinical-Time-Series-Forecasting

## Introduction
This repository contains the implementations of Variational Recurrent Neural Networks[[1]](#1) for Clinical Time Series Forecasting on MIMIC III.  


### Detail

#### 0 - Preprocessing
- [Read](https://github.com/SibghatUllah13/VRNNs-for-Clinical-Time-Series-Forecasting/blob/master/Preprocess%202.0/read_data_ihm.ipynb) in-hospital-mortality data extracted from [[2]](#2).
- [Re-Sample](https://github.com/SibghatUllah13/VRNNs-for-Clinical-Time-Series-Forecasting/blob/master/Preprocess%202.0/resample_ts.ipynb) the Time Series.
- [Prepare](https://github.com/SibghatUllah13/VRNNs-for-Clinical-Time-Series-Forecasting/blob/master/Preprocess%202.0/prepare_data.ipynb) Data for Learning Task.

#### 1 Step Ahead Forecasting

- Run all the files in the [folder](https://github.com/SibghatUllah13/VRNNs-for-Clinical-Time-Series-Forecasting/tree/master/1%20Step%20Ahead%20Forecasting)

#### 2-5 Step Ahead Forecasting

- Run all the files in the [folder](https://github.com/SibghatUllah13/VRNNs-for-Clinical-Time-Series-Forecasting/tree/master/2-5%20Step%20Ahead)

#### 6-10 Step Ahead Forecasting

- Run all the files in the [folder](https://github.com/SibghatUllah13/VRNNs-for-Clinical-Time-Series-Forecasting/tree/master/6-10%20Step%20Ahead)

## Requiremnts
For this project to run you need:
* Python 3.7.3
* Pytorch 1.3.0+cpu
* Numpy 1.16.2
* Matplotlib
* Pandas 0.24.2
* Scikit-learn 0.20.3 

## References:
<a id="1">[1]</a> 
Chung, Junyoung, et al. "A recurrent latent variable model for sequential data." Advances in neural information processing systems. 2015.

<a id="2">[2]</a> 
Harutyunyan, Hrayr, et al. "Multitask learning and benchmarking with clinical time series data." arXiv preprint arXiv:1703.07771 (2017).
