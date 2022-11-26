import os
import nuke

#add network path here
network_repo_path = "ADD_PATH_HERE"

#Insert artist path to repository and make python packages available
nuke_folder = os.path.dirname(os.path.abspath(__file__))
local_repo_path = os.path.join(nuke_folder, "repo")
nuke.pluginAddPath(os.path.join(nuke_folder, "site-packages"))

import pymongo
import git
# import sshtunnel
# from sshtunnel import SSHTunnelForwarder

#Initialise and clone repository from network path
repo = git.Repo.init(network_repo_path)

if not os.path.exists(local_repo_path):
    repo.clone(os.path.join(network_repo_path, local_repo_path), branch="main") 
    origin = repo.remotes.origin
    origin.pull()


clone_repo = git.Repo.init(local_repo_path)
# remote_address = "127.0.0.1"
# port = 27017
# user = "server"
# password = "1"

#Virtual machine does not work sadly. Error opening a module
#Update repo file from database in virtual machine
# virt_machine =  sshtunnel.SSHTunnelForwarder("192.168.1.19",
#                                     ssh_username=user,
#                                     ssh_password=password,
#                                     remote_bind_address=(remote_address, port))

# virt_machine.start()

# client = pymongo.MongoClient(remote_address, virt_machine.local_bind_port)
# db = client["vfx"]
# collection = db["cct"]
# document = collection.find_one({"name":"nuke"})

# virt_machine.stop()

clone_repo.git.checkout("ADD_HASH")

nuke.pluginAddPath("repo")

nuke.message('Hello World!')