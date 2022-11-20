# vfx_pipeline

## Main goals
Get to know pipeline development on my home setup
### 1. MongoDB NoSQL
Learning about managing data with PyMongo
### 2. Make use of apis (nuke, houdini)
- NukeAPI works on pc and mac (serves as artist workstation)
- HoudiniFX works kind of (needs more work)

## 2. Setup Instructions
### Nuke
- Will be updated
### Houdini 19.5
With the help of Houdini Expression Editor nodes can be created during a session and presaved on .py files

1. Windows -> External Python Source Editor
2. Session connected file opens
3. Paste prepared code and test
4. Open a Python Shell on Houdini
5. Call function. Something like hou.session.test()

#### make import hou work
Add this to the settings.json file:
'''
"python.autoComplete.extraPaths": [
    "C:\\Program Files\\Side Effects Software\\Houdini 19.5.303\\python39\\libs"
],
"python.autoComplete.preLoadModules": ["hou"],
"terminal.integrated.env.windows": {
    "PYTHONPATH": "C:\\Program Files\\Side Effects Software\\Houdini 19.5.303\\python39\\libs",
    "PATH": "${env:PATH};C:\\Program Files\\Side Effects Software\\Houdini 19.5.303\\bin"
},
'''
and set the python interpreter to this path:
'''
"C:\Program Files\Side Effects Software\Houdini 19.5.303\bin\hython3.9.exe"
'''

## 3. diary
221120/n Setup with nuke and houdini on my main computer (nuke setup on mac) and learning now how to manage github for versioning with GitPython

## 4. to do
- restructure file structure
- pyside6
- using oop with python, restructure
- houdini: find good way to setup stuff
- mongodb setup db and crud functionality
