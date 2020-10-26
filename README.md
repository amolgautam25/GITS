
# GITS 
### GIT Simplified

![GitHub](https://img.shields.io/github/license/amolgautam25/GITS)
[![Build Status](https://travis-ci.com/amolgautam25/GITS.svg?branch=master)](https://travis-ci.com/amolgautam25/GITS)
![GitHub](https://img.shields.io/badge/language-python-blue.svg)
![GitHub](https://img.shields.io/badge/language-shell-orange.svg)
![YouTube Video Views](https://img.shields.io/youtube/views/cMcftHMtIZ4?style=social)

[![DOI](https://zenodo.org/badge/295480790.svg)](https://zenodo.org/badge/latestdoi/295480790)

![GitHub issues](https://img.shields.io/github/issues/amolgautam25/GITS)
![GitHub closed issues](https://img.shields.io/github/issues-closed/amolgautam25/GITS)

![GitHub pull requests](https://img.shields.io/github/issues-pr/amolgautam25/GITS)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/amolgautam25/GITS)

[![](https://img.youtube.com/vi/cMcftHMtIZ4/0.jpg)](https://youtu.be/cMcftHMtIZ4 "GITS demo")


### Supported functionality

#### gits pr_update
This functionality makes sure that the current branch is able to make a PR without much trouble ( conflict ). It makes sure that the current branch has the latest commit off master branch, and that the local master has all the commits from the upstream master. This helps in reducing merge conflicts

#### gits profile
This functionality allows the user to change the git account quickly with a single command. There are situations when a developer has a personal github account and a enterprise github account as well. Changing between these accounts is a little complicated. This functionality aims to simplify it.

#### gits rebase 
This is a highly simplified version of git rebase command. This interactive command asks for the branch that you want to rebase and automatically rebases it off master. This is the most common scenario. The original GIT rebase command is a little un-intuitive and there is always a confusion , about the source branch and the destination branch.  

#### gits reset
'Reset' intuitively means a HARD reset. This functionality does a HARD reset on your branch, and makes it even with the remote branch. This aims to simplify the confusion between HARD and the SOFT reset.  

#### gits set
This functionality sets the parent branch. 

#### gits upstream
This functionality changes the upstream with a single command. No need to manually remove the existing upstream, and adding a new upstream. This command will automatically change the upstream for the git repo. If there is any existing upstream , it will be overwritten.

#### gits super reset
Have you ever run into a situation, where you had to clone the repository again ? Yes, this functionality is exactly for that scenario. It will remove the current repository. It will clone it again, and add all the 'remote' to this freshly cloned repository. 

#### gits add 
Function that adds files as passed to the gits add command. Performs operation as similar to git add command

#### gits commit
It is a highly simplified version of git commit command. We are actively working on this functionality such that a commit would fail if the unit tests does not pass. We can specify the tests that need to pass before the commit can actually happen. 

#### gits create_branch
This automatically checks out a new branch from local master , after pulling all the changes from the remote master to local master. The idea behind this is that this new branch should have all the latest commits before a developer starts working on them.

#### gits all-branch
This command lists all the branches on both local and remote repositories.


#### gits remote-branch
This command lists all the branches on remote repository.


#### gits init
This command initializes the local repository.

#### gits logging
This logs all the commands executed by the user, and also stores the output of each command

#### gits push
This pushes all the local changes of origin to the branch specified. 

Note: More functionality are being added to this project. Please refer to the 'issues' tab for more information. In case you want to contribute to this project , please refer to 'Contributing.md' file.


### pydoc implementation
We have tried to write as much documentation as possible. You can use pydoc to go through the documentation. 
For example if you want to go through all the documentation for all files in code/ directory, do the following: 

`cd code`<br>
`python3 -m pydoc -b `

This will open up a browser and you can see all the files. You can click on a particular file to access the documentation associated with that file.

This repository is made for CSC 510 Software Engineering Course at NC State University.

Group 17 Team Members: 

Amol Gautam  
Sneha Kumar  
Sreeraksha Mavinhally Sreekantha  
Srujana Rachakonda  
Tanay Agarwal
