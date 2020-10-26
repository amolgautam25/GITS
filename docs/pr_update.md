# About gits pr_update
This functionality makes sure that the current branch is able to make a PR without much trouble ( conflict ). 
It makes sure that the current branch has the latest commit off master branch, 
and that the local master has all the commits from the upstream master. 
This helps in reducing merge conflicts.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/harshitpatel96/GITS/blob/master/code/gits_pr_update.py).

# Code Description
## Functions
1. gits_pr_update_func(args):
This function takes **args** object as an input which has an attribute **upstream** to store name of the upstream branch. 
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
To make sure that your changes does not result in any merge conflict, you can use this command in following way:
```
$ gits pr_update
```
If command detects any possible conflicts, it will ask you to fix those on your local machine only. 