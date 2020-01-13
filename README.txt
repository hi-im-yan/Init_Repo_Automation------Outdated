What this code do:
This code automate the process of creating project folders and project repositories on github. Run this code and it will automatically create a new repository, create a new folder on your file explorer, open your IDE and make a connection of your folder to the repository (git init, git remote add, etc). And then you are ready to code, commit and push. No need to configurate the boring parts.

1. Requirements:
   1.1 Need Python to be installed.
   1.2 Some sort of git bash need to be installed (vscode console can run it too. Maybe...).

2. Installation:
   2.1 git clone https://github.com/hi-im-yan/Init_Repo_Automation.git
   2.2 cd Init_Repo_Automation
   3.1 pip install -r dependecy.txt (You never know when a new feature can added)

3. Configuration:
   3.1 Go to "create_repo.sh". Change the path of line 3 to the path of your projects folder (this path is the one that will contain your repositories. Don't touch "$1").
   3.2 On the same file. Line 5 change the "hi-im-yan" to your GitHub username.
   3.3 On the same file. Line 10 is optional, the command will create a new branch called "developing". Erase if you want to.
   3.4 On the same file. Line 11 is a command to open your new project on vscode. You can erase the line or you can add your IDE command to open.
   3.5 Go to "new_repo.py". Change the "path" variable to the same path of step 3.1 but take out "$1".
   3.6 On the same file. Insert your GitHub username and password on the related variables.

4. Run:
   4.1 (On Git Bash) sh create_repo.sh <Project_name> (This step is going to depend on your console choice. Search on google how to run .sh files on your console.)
   4.2 That's it.


Pros:
   1. No need to open GitHub
   2. No need to log on GitHub
   3. No need to create repository on GitHub
   4. No need to create a project folder on file explorer
   5. No need to open your IDE
   6. No need to "git init", "git remote add", etc
   7. You just need to open console and run 1 one command line
