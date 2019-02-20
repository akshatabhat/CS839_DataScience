## Webpage for CS839 Project

This repository contains the code, data, and report for the different stages of the Data Science project for CS 839.

**Team:** Akshata Bhat, Pratyush Mahapatra, Felipe Gutierrez Barragan.

**Group ID:** 4.

**Contents:**

1. [Stage 1](#stage1)
2. [Stage 2](#stage2)
3. [Stage 3](#stage3)
4. [Stage 4](#stage4)
5. [Python Environment Setup](#envsetup)

<hr>
<a name="stage1"></a>

### Stage 1: Information Extraction From Text


<hr>
<a name="stage2"></a>

### Stage 2: 

<hr>
<a name="stage3"></a>

### Stage 3: 

<hr>
<a name="stage4"></a>

### Stage 4: 

<hr>
<a name="envsetup"></a>

### Python Environment Setup

Follow the steps in this section to setup an anaconda virtual environment that contains all the required dependencies/libraries to run the code in this repository.

1. **Install miniconda**
2. **Create anaconda environment:** The following command creates an anaconda environment called `dsenv` with python 3.5.

```conda env create -n dsenv python=3.5 ```

3. **Activate environment:** 

```source activate dsenv```

4. **Install libraries:** The code in this repository uses numpy, scipy, pandas, matplotlib, scikit-learn, and ipython (for development). To install all these dependencies run the following command:

```conda install numpy scipy matplotlib ipython pandas scikit-learn```

**Note:** If directly installing the packages with the above commands does not work it is probably because different versions of the libraries were installed. If this happened remove the environment and start over with the following steps.

1. Install miniconda and clone this repository.
2. Navigate to the folder containing this repos.
3. Use the `dsenv.yml` file to create the conda environment by running the following command: `conda env create -f dsenv.yml`. This command will setup the exact same conda environment we are currently using with all library versions being the same.

For more details on how to manage a conda environment take a look at this webpage: [Managing Conda Environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment).

