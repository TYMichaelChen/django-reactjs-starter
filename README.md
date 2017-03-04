# Step 00. Setup Requirements

This setup assumes you are working with a Mac computer. If you are not working on a Mac, the main things that need to be installed are `Python3` and `Pyvenv`

**Install Homebrew/XCode**

First we install Command Line Tools for Xcode. Open a terminal and type:
```
xcode-select --install
```
This should prompt a window that will install the Command Line Tools.

Next, we need to install Homebrew. In your terminal, type:
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Close the terminal and the installations should be finished.

**Install Python 3**

Now that we have Homebrew install, we're going to use Homebrew to install Python3. Open a terminal and type:
```
brew install python3
```
You can now try running `python3 --version` to make sure everything is installed properly.

**Install Virtual Environment**

Now we want to install virtual environment. Virtual environments is a tool that helps you separate different projects by keeping the dependencies separately and thus more manageable. 
```python
pip install virtualenv
```

**Create Virtual Environment**

Now that the virtual environment is installed, we're going to want to create a environment that is initialized to Python 3. So go into your project directory, and in the terminal type:
```python
virtualenv -p python3 envname
source envname/bin/activate
```
You should see in the terminal with (envname) to the left of the terminal prompt.

**Install Django**

Now that we are in our virtual environment.  We should install Django(latest at the time of writing is 1.10.5). First create a `requirements.txt` file in the project directory. In the file add `Django==1.10.5` and return to the terminal and type:
```python
pip install -r requirements.txt
```

If all goes well without error, you are done with Step 0!

Go to [Step 01](https://github.com/MikeTYChen/django-reactjs-starter/tree/step01-django-project)

