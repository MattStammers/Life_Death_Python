# QI-Py

Quickly using open source python scripting to solve real healthcare problems

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
python -m venv 'ENV NAME'

# OR

conda create venv 'ENV NAME'
```

2. Then activate the environment
```python
python activate 'ENV NAME'

# OR

conda activate 'ENV NAME'

# In VS Code you can additionally use shift-ctrl-P to select the interpreter
```

3. Then run from the command line
```python
pip install -r requirements.txt
```

4. Finally run this to launch a kernel and browser locally hosted notebook:
```python
python -m notebook
```

### Tricky Parts

##### Ingesting Data

The first tricky part of this is ingesting the data. If you have the data available as .csv or other flat files you can clean this up and use that but we recommend where possible connecting directly to the database or warehouse because it provides far greater flexibility. The examples given feature direct database connections which you might need some help from your local network/BI teams to establish. In all likelihood this is the only part you will need extra help with

##### Automation

To automate your script for beginners we recommend using windows task scheduler. This stack overflow post details the simplest way to do this by converting it to a .py file first: https://stackoverflow.com/questions/65971461/jupyter-notebook-schedule-automatically. Alternatively you can write a short .bat executable and get task scheduler to run that. 

You can run the notebook directly using runipy but this generates significant un-necessary overhead in a small project like this and is more likely to result in problems.

#### Finally

Good luck. The above might seem a bit daunting but if you follow the process step by step with a little bit of patience you will get there. Feel free to fork or download this repo and do what you will with it. 

##### Disclaimer

Obviously this code is being given away for free and as a result no guarantees can be given that it will work. The authors therefore accept no liability for its use.