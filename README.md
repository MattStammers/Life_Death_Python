# QI-Py

Quickly using open source python scripting to solve real healthcare problems. Target Audience: Anyone

### By Matt Stammers and Michael George - University Hospital Southampton
### 23/04/2022

The purpose of this simple repository is to demonstrate the use of code to solve frontline clinical problems in a way that almost any frontline NHS worker could achieve with a little bit of knowledge. 

#### Intended Audience

The intended audience is frontline clincians (and analysts) learning to code and solve problems perhaps without much programming skill or support within their current trust.

#### Purpose

It should be viewed as an example only in the hope that it will inspire others to try to solve similar problems in their own hospitals. 

#### Scope

There are two frontline clincial problem python examples here:

1) Learning from Death: Mortality and morbidity 10-year survival score calcluation using vvcb's excellent comorbidipy: https://github.com/vvcb/comorbidipy
2) Protecting Life: Saving life by improving the hospitals GI bleed care model and analysing the outcome with python.

#### Installation

The seperate projects share common dependencies as listed in requirements.txt

1. We recommend you start by installing a virtual environment with: 

```python
# For pip environments
python -m venv /path/to/environment

# OR

#For conda environments
conda create venv 'ENV NAME'
```

2. Then activate the environment
```python
#For pip environments
source /path/to/environment/bin/activate

# OR

#For conda environments
conda activate 'ENV NAME'

# In VS Code you can additionally use shift-ctrl-P to select the interpreter
```

3. Then run from the command line
```python
#For pip environments
pip install -r requirements.txt

#TODO - For conda environments
```

4. You will also need to install comorbidipy from https://github.com/vvcb/comorbidipy. Once unzipped please navigate to the central directory and run
```python
python setup.py install
```

5. In a new terminal, navigate to the root of this folder and open in VSCode or other preferred IDE. Alternatively open up the jupyter notebook web interface with the following command:
```python
python -m notebook
```

6. Connect the jupyter notebook to a python kernel associated with your virtual environment:

If using the jupyter notebook web interface, run the following command and then select the newly installed kernel from menu bar: Kernel -> Change kernel
```python
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

If using VSCode the kernel, you can select the kernel that is associated with your virtual environment in the top right of the screen and the above command will be automatically executed.


Then follow the seperate instructions for each script. If it doesn't make sense or you have problems please raise an issue.

### Tricky Parts

##### Ingesting Data

The first tricky part of this is ingesting the data. If you have the data available as .csv or other flat files you can clean this up and use that but we recommend where possible connecting directly to the database or warehouse because it provides far greater flexibility. The examples given feature direct database connections which you might need some help from your local network/BI teams to establish. In all likelihood this is the only part you will need extra help with

##### Encrypting Keys

You should never expose your credentials in any code. I would argue that you should not even expose ports or IP addresses. There are a variety of ways to protect this information - the simplest way for new beginners is to use a keyring and encrypt the keys to your local machine. That way only a hacker with access to your machine can run your code. In windows these credentials are stored by windows credential manager and as most NHS machine hard-drives are encrypted your credentials are then as secure as the machine you are working on. This technique doesn't scale particularly well but it is a good starting point for budding python scripters.

##### Automation

To automate your script for beginners we recommend using windows task scheduler. This stack overflow post details the simplest way to do this by converting it to a .py file first: https://stackoverflow.com/questions/65971461/jupyter-notebook-schedule-automatically. Alternatively you can write a short .bat executable and get task scheduler to run that. 

You can run the notebook directly using runipy but this generates significant un-necessary overhead in a small project like this and is more likely to result in problems.

#### Finally

Good luck. The above might seem a bit daunting but if you follow the process step by step with a little bit of patience you will get there. Feel free to fork or download this repo and do what you will with it. 

##### Disclaimer

Obviously this code is being given away for free and as a result no guarantees can be given that it will work. The authors therefore accept no liability for its use.
