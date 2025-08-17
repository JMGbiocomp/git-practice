# I am learning to use Git!

## admin commands

a.  git help
-display help information about git commands
Ex:
git help -a #all commands
git help -c #allo available configuration variables
git help -g #print a list of git concept guides

b.  git config
-can query/set/replace/unset options aka configure
-commands within config:
    -list: list all variables eet in config file and values
    -get: retrieves a value specified
    -set: sets vale for one or more config
    -unset: unset value for one or more config
    -edi: opens an editor to modify the specified config either --system, --global, --local(default), --worktree, or --file <config file>
*see documentation for options and arguements; view config file to evalaute issues and debugt problems

## basic commands

1.  git status
-returns the repositopry status on your current directory
-files are listed as untracked or staged
-current branch is indicated 

2.  git init
-initializes a directory as a git repository

3.  git add <filename>
-adds an untracked file in repository to the staging area or cahnges to files already in the repository
-essentially initializing the file into the repository without committing the file to the project hisotry
*filenames need to be surrounded by quotes
*use "." instead to add all files unstaged
ex:
git add "hello.md"
git add .

4.  git commit 
-commits all the files on the staging area
- the arguemtn "-m" followed by "some commit message here" adds a message to display to the commit history of this commit
-placing a specific file name after commit or at the end of the command will only commit that file and leave everything else staged
*not including a massage will send you to the vim text editor to inlcude a message so alweays just include thje -m "message" in the command
Ex:
git commit
git commit -m "feature add: login credentials"
git commit -m "featue add" <filename>

5.  git log
-view the commit history of the current branch
-contains a unique commit hash, branch information, author, date, commit message if available, and continues in reverse order chronologically
-add the branch_name after "log" to get the commit history of a specific branch
-add file path after "log" to get the commit history of a specific file
-use --after="year-month-day" to view commits on specific date
-use --oneline to see commit hisotry summaries on one line
Ex:
git log
git log branch_name
git log path/to/file
git log --after="2021-09-01"
git log --oneline
git log --author="author name"

6.  git remote
-set up, change and view remote repository
Ex:
git remove -v #view remote connections withj local repository
git remove add https://github.com/JMGbiocomp/git-practice.git
git remote set-url origin https://github.com/JMGbiocomp/git-practice.git

7.  git push
-add local changes to the remote repository
-can require admin to review pushes before accepting them into the remote
Ex:
git push -u origin main #or 'master' depending on the central branches name
git push --all origin #all branches
git push --tags origin #all tags

8.  git pull
-git pull is a combination of both 'git fetch' and 'git merge' in which fetch retrieves the changes and merge to combine your local changes with the history of the remote changes to create a linear history
-allows you to work locally from the changes on the remote or add your local changes to the combined hisotry on the remote
Ex:
git pull #pull changes from default remote (usually origin); check with git remote -v
git pull <remote> <branch>  #example: git pull origin main

9.  git mv
-move or rename files, directories or symlink
Ex:
git mv <oldfilename> <newfilename>
git mv source/file/path destination/file/path

## Branch management

1. git branch
-list, create or delete branches
Ex:
git branch --list #list branches
git branch -d -r origin/b1 origin/b2 origin/b3 #deletes (-d) remote (-r) brachs b1, b2, and b3



2. git checkout
-switch branches or restore working tree files
-commonly used to create branches as well
Ex:
git checkout <branch>
git checkout -b <branch> #new branch
git checkout -m <branch> #merges current branch, working branch and new branchy together

3. git switch


4. git merge


5.  git tag





