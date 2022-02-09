
# Variational Recurrent Neural Networks (VRNNs) for Irregular, Asynchronous Clinical Time Series Forecasting
Contains the code to forecast irregular, asynchronous, clinical time series based on VRNNs, which are variational autoencoders extended to
model the sequential data [[1]](#1). In the study, Medical Information Mart for Intensive Care (Version III) (MIMIC III), is utilized as a benchmark data set.
The study validates the concept of utilizing  external domain information to improve the generalization capability (forecasting) of VRNNs.

# Introduction
This code is based on our paper, titled [Exploring Clinical Time Series Forecasting with
Meta-Features in Variational Recurrent Models](https://ieeexplore.ieee.org/abstract/document/92072545) (Ullah, Xu, Wang, Menzel, Sendhoff & Bäck, 2020), and can be used to reproduce the experimental setup and results mentioned in the paper. The code is produced in Python 3.0. The main packages utilized in this code are presented in the next section which deals with technical requirements. 

As stated earlier, we want to improve the generalization capability of VRNNs for time series forecasting. For validating our thesis, we choose a widely-accepted clinical
benchmark data set, which is referred to as MIMIC III. Our aim is to incorporate external domain information, e.g., in this case disease information, to improve the forecasting ability of such models. Based on this external domain information, e.g., disease information about the patients, we can link the time series to each other, i.e., time series of a particular patient in the hospital should be similar to the time series of other patients with similar disease information. Then, when learning the VRNNs, we can also
incorporate the linked time series to each other, which gives rise to better forecasting than vanila VRNN.

To perform the study, we first have to pre-process the MIMIC III data set based on the code provided by [[2]](#2). After this, we have to traverse to the
directory, titled `Preprocess 2.0`. This directory contains three jupyter notebooks, named `prepare_data.ipynb`, `read_data_ihm.ipynb`, and `resample_ts.ipynb` respectively. 
The purpose of each of these notebooks will be explained later. Here, it is important to know that this directory contains the necessary code to preprocess the data.
After that, we can utilize the transformed data set to construct the VRNNs models (vanila as well as extended models based on our idea).
In our study, we evaluate the performance of VRNNs models based on 1-10 step ahead forecasting (hence a total of 10 different learning tasks).
The code for this is provided in three directories, which  are titled `1 Step Ahead Forecasting`, `2-5 Step Ahead`, and `6-10 Step Ahead` respectively. 
Each of these directories contains a total of four notebooks, titled `model.ipynb`, `model - sim.ipynb`, `model - prior.ipynb`, and `model - sim - prior.ipynb` respectively. 
Where `model.ipynb` and `model - prior.ipynb` implement the vanilla VRNNs describe by [[2]](#2), the other two notebooks contain their extensions based on our idea of similarity, i.e., related.

In the following, we describe the technical requirements as well the instructions to run the code in a sequential manner.

# Technical Reuirements
In this code, we make use of four python packages (among others), which are presented below in the table.
In particular, `PyTorch` can be utilized to implement the VRNNs.
The package `SciPy` is utilized to sample from the probability distributions.
Apart from that, `pandas` and `scikit-learn` are utilized for data transformation and wrangling. 
All four required packages can be installed by executing `pip install -r requirements.txt` from the main directory via the command line.
Note that our code is only compatible with `PyTorch` with CPU. 
Additionally, we make use of the external module `mimic3benchmark`, which is separately provided by [[1]](#1).

| Package | Description |
| --- | --- |
| PyTorch | For implementing the VRNNs.  |
| SciPy | For sampling from probability distributions. |
| pandas | For data manipulation and transformation. |
| scikit-learn | Also, for data manipulation and transformation. |

In the following, we describe how to reproduce the experimental setup and results mentioned in our paper.

## 1. Initial Pre-processing of MIMIC III 
The initial pre-processing of MIMIC III data set is based on the code provided by [[1]](#1). For the details on the way their pre-processing works, please refer to their work
and our paper. After the initial pre-processing (based on the methodology of [[1]](#1)) is completed, we have to load the pre-processed data set into memory.
For this purpose, please use the jupyter notebook `read_data_ihm.ipynb` inside the directory `Preprocess 2.0`. Next, re-sample the time series based on the notebook 
`resample_ts.ipynb`. Re-sampling is a crucial step since the original time series is ashychrnous, e.g., not all the temporal features are observed at the same time.
In our study, we re-sample the time series to ensure that we have exactly one entry of all the temporal variables in one hour. After this, we have to prepare the
data set for learning. To this end, we utilize the notebook `prepare_data.ipynb` in the same directory.
At the end of this, the quality of the data is enough such that it can be utilized in learning.

## 2. Constructing the VRNNs, and Forecasting the Time Series
We can construct the VRNNs (extended and vanila) based on their goal, i.e., how many steps ahead must we forecast?
In general, we have 10 different learning tasks, i.e., one-ten steps ahead forecasting.
For the first task, we have the code inside the directory `1 Step Ahead Forecasting`. 
This directory contains four different jupyter notebooks, all of which implement the four models described earlier.
For forecasting 2-5 steps ahead, please refer to the code inside `2-5 Step Ahead` directory, which has the same file structure as the  `1 Step Ahead Forecasting`.
Finally, to perform 6-10 steps ahead forecasting, the code inside `6-10 Step Ahead` can be utilized.

# Citation
## Paper Reference
S. Ullah, Z. Xu, H. Wang, S. Menzel, B. Sendhoff and T. Bäck, "Exploring Clinical Time Series Forecasting with Meta-Features in Variational Recurrent Models," 2020 International Joint Conference on Neural Networks (IJCNN), 2020, pp. 1-9.
## BibTex Reference
`@inproceedings{ullah2020exploring`,\
  `title={Exploring clinical time series forecasting with meta-features in variational recurrent models},`\
  `author={Ullah, Sibghat and Xu, Zhao and Wang, Hao and Menzel, Stefan and Sendhoff, Bernhard and B{\"a}ck, Thomas},`\
  `booktitle={2020 International Joint Conference on Neural Networks (IJCNN)},`\
  `pages={1--9},`\
  `year={2020},`\
  `organization={IEEE}`\
`}`

# Acknowledgements
This research has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement number 766186 (ECOLE).

## References:
<a id="1">[1]</a> 
Chung, Junyoung, et al. "A recurrent latent variable model for sequential data." Advances in neural information processing systems. 2015.

<a id="2">[2]</a> 
Harutyunyan, Hrayr, et al. "Multitask learning and benchmarking with clinical time series data." arXiv preprint arXiv:1703.07771 (2017).
