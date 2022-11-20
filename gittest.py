from git import Repo
import os

#clone current repository from main branch for artist computer
path = "C:/projects/pipeline"
cloned_path = "C:/Users/Martin/Meine Ablage/pipeline"

repo = Repo.init(path)
if not os.path.exists(cloned_path):
    repo.clone(os.path.join(path, cloned_path), branch="main") 
    print("Clone to" + cloned_path + " successful")
else:
    print("Clone already exists.")

#update cloned main files
cloned_repo = Repo.init(cloned_path)
o = cloned_repo.remotes.origin
o.pull()

#show branches
# heads = repo.heads
# for h in heads:
#     print(h)
# print(heads)

print("DONE")