import os
# import nuke

#add network path here
network_repo_path = "C:/projects/pipeline"

#Insert artist path to repository and make python packages available
nuke_folder = os.path.dirname(os.path.abspath(__file__))
local_repo_path = os.path.join(nuke_folder, "repo")
nuke.pluginAddPath(os.path.join(nuke_folder, "site_packages"))

import pymongo
from sshtunnel import SSHTunnelForwarder
from git import Repo

repo = Repo.init()

#Initialise and clone repository from network path
# if not os.path.exists(local_repo_path):
#     repo.clone(os.path.join(network_repo_path, local_repo_path), branch="main") 


# origin = repo.remotes.origin
# origin.pull()


remote_address = "127.0.0.1"
port = 27017

#Update repo file from database in virtual machine
virt_machine =  SSHTunnelForwarder("192.168.1.19",
                                    ssh_username="server",
                                    ssh_password="1",
                                    remote_bind_address=(remote_address, port))

virt_machine.start()

user = "server"
password = "1"

client = pymongo.MongoClient(remote_address, virt_machine.local_bind_port)
db = client["vfx"]
# collection = db["software"]
collection = db["cct"]
document = collection.find_one({"name":"nuke"})
# repo.commit(document["hash"])
repo.git.checkout(document["hash"])
virt_machine.stop()