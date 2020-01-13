from github import Github
import os
import sys

path = "C:/Users/yanaj/Projetos/"

un = "" #Insert GitHub UserName
pw = "" #Insert GitHub PassWord

projectName = str(sys.argv[1])

def create():
    projectName = str(sys.argv[1])
    os.makedirs(path + str(projectName))
    print("\nProject " + projectName + " folder created on path " + path)
    account = Github(un, pw).get_user()
    account.create_repo(projectName)
    print("Repository " + projectName + " added to GitHub")
    print("")

create()