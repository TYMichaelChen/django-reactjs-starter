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

**Virtual Environment with Pyenv**

Now that Python 3 is installed, it should come pre-installed with a virtual environment.
Virtual environments is a tool that helps you separate different projects by keeping the dependencies separately and thus more manageable. We're going to want to create a environment that is initialized to Python 3. So go into your project directory, and in the terminal type:
```python
virtualenv -p python3 envname
```
You should see in the terminal with (envname) to the left of the terminal prompt.

If all goes well without error, you are done with Step 0!

Go to [Step 01](https://github.com/MikeTYChen/django-reactjs-starter/tree/step01-django-project)

