# About gits init
This function allows user to transform current directory into a Git repository.

# Location of Code
The code that implements this gits functionality is located [here](https://github.com/harshitpatel96/GITS/blob/master/code/gits_init.py)

# Code Description
## Functions
1. gits_init(args):
This function takes optional arguments as an input. Those arguments are **bare** which is a boolean attribute and **template** which takes path to template file as input. If **bare** is set to true, then an empty git repository would be initialized but the working directory would be omitted. Whereas, if **template** argument is used, then the directory is initialized with the provided template repository.

# How to run it? (Small Example)
There are three different ways to initialize the repository.
1) Simple git initialization
```
$ gits init
```
2) Using bare flag
```
$ gits init --bare
```
3) Using templates
```
$ gits init --template pathtotemplate
```

After using any of these commands your directory would have a version control system.
