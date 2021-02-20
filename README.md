# ModelPlotter
Script for the web app to plot the suspension response in KAGRA

## Environment

## Matlab_engine
Install matlab_engine package from matlabroot.

Under the cds workstation environment, the matlabroot was /kagra/apps/matlab.2019a.tools according to the return message from matlab root in Matlab2019a. After comfirmation the root directory, you can install the matlab engine in your python einvironment by following the command;

```
cd /kagra/apps/matlab.2019a.tools/extern/engines/python/
python setup.py install --prefix='/home/controls/miniconda3/envs/vis_modelplotter'
```


