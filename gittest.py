from git import Repo
import os

#clone current repository from main branch
path = "C:/projects/pipeline"
clone_path = "C:/Users/Martin/Meine Ablage/pipeline"

repo = Repo.init(path)
if not os.path.exists(clone_path):
    repo.clone(os.path.join(path, clone_path), branch="main")
    print("Clone to" + clone_path + " successful")
else:
    print("Clone already exists.")

#show branches
# heads = repo.heads
# for h in heads:
#     print(h)
# print(heads)

print("DONE")