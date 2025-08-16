# I am learning to use Git!

## Git Command Usage

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
Ex:
git commit
git commit -m "feature add: login credentials"
git commit

5. git log
-view the commit history of the current branch
-contains a unique commit hash, branch information, author, date, commit message if available, and continues in reverse order chronologically
 -add the branch_name after "log" to get the commit history of a specific branch
 -add file path after "log" to get the commit history of a specific file





