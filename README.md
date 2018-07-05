# CV_Introduction
Introduction to Computer Vision with Python.

This repository is a collection of frameworks and methods to get you started with
Computer Vision. It relies mostly on [openCV](https://opencv.org/) for the 
implementation of the methods presented here.

# Setting up your environment

This guide is targeted at Windows users, so please use Google to help you set up
your MacOS or Linux OS if you happen to use those.

1. Install python

Windows user simply should download and install Anaconda from here:
https://www.anaconda.com/download/

To try out if everything went fine, open up the Anaconda Prompt and try
to run Python:

* Open up the Anaconda Prompt by hitting Windowsbutton and typing in "Anaconda
Prompt" or look for the prompt in your startup menu
* In the prompt, type in the following to start up the Python interpreter:

```commandline
python
```

You should get an output like this:
```commandline
Python 3.6.3 |Anaconda custom (64-bit)
```

* Exit the python interpreter by typing following command:

````python
quit()
````

2. Install PyCharm IDE

Download and install [PyCharm](https://www.jetbrains.com/pycharm/) as your IDE.

3. Clone this repository

In PyCharm, navigate to the VCS tab and click on "Checkout from Version Control".
Then go to "GIT" and copy in the following URL:

https://github.com/NatholBMX/CV_Introduction.git

What for the process to finish and open the new project.

4. Create a new virtual environment

Open up your Anaconda Prompt and create a new virtual environment with
following command:

````python
conda create -n cv_introduction python=3.6
````

Try out whether the creation of the environment was successfull with following
command:
````python
activate cv_introduction
````

You should notice that the content of the brackes in the Anaconda Prompt
changed from

````commandline
(base)
````

to

````commandline
(cv_introduction)
````

Deactivating the virtual environment is done with following command:

```commandline
deactivate
```

5. Configure your project interpreter
Set the created virtual environment for your project interpreter by navigating
in PyCharm to "File", "Settings" and
then "Project: CV Introduction". Choose "Project Interpreter".

Click on the gear icon to and add a new project interpreter. 
Choose "Virtual Environment", then "Existing Environment" and enter
the location of your created environment.

You can find the installation location of your Conda executable by starting
the Anaconda Prompt, activating the virtual environment,
starting the python interpreter and executing following commands:

````python
import sys, os
os.path.dirname(sys.executable)
````

Copy the output of this and choose "python.exe" to configure your project interpreter.