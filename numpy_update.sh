#!/bin/bash

# A general git update for the numpy_practice.py file with continued practice and demonstration of proper use of NumPy
# python is added to the stagging area and committed with the "NumPy: General Update Message"

git status #see git recognition of changes need to add and commit on current branch
git add "numpy_practice.py" #add file to stage
git commit -m "NumPy: General Practice Update" "numpy_practice.py" #commit changes
git status #confirm changes are committed to branch
