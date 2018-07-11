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


6. Install the packages needed for this introduction project

You can simply install all required packages from PyCharm by opening 
"requirements.txt" and clicking on "Install requirements".

For installing all requirements without an idea, run:

````python
pip install -r requirements.txt
````

This will install most of the requirements needed. There are two
modules which require special treatment.

* Dlib: Download the 
[Python Bindings for Dlib](https://files.pythonhosted.org/packages/97/08/0d2b53b3845d562d01108e482ae45596a0d13bf58c63172df954ff0b53ef/dlib-19.14.0.tar.gz#sha256=88470836cb649b380f6f9eca054f08a94b115ee2845b1eccbf8a410efb2e3dc1)
and extract them into your preferred folder.
* Install the wheel with Python:
````python
pip install dlib-file.whl
````
* Install face_recognition by running following script:
````python
pip install face_recognition
````

Manual installation:
* Install openCV Python for Windows: 
[openCV Python](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html)
* Install Tensorflow for Windows: 
[Tensorflow Installation For Windows](https://www.tensorflow.org/install/install_windows).
If you happen to have Admin rights, install it for GPU.
* Install Keras for Windows:
[Keras Installation](https://keras.io/#installation)


7. Test your installation

The folder "tests" contains different scripts for testing your installation.

* Test openCV: run "simple_webcam.py"
* Test Tensorflow: run "simple_tensorflow.py"
* Test Keras: run "simple_keras.py"
* Test face_recognition: run "simple_face_recognition.py"