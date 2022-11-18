# vfx_pipeline

### 1. MongoDB NoSQL
Learning about managing data with PyMongo

### 2. Make use of apis (nuke, houdini)



### make import hou work
Add this to the settings.json file:

"python.autoComplete.extraPaths": [
    "C:\\Program Files\\Side Effects Software\\Houdini 19.5.303\\python39\\libs"
],
"python.autoComplete.preLoadModules": ["hou"],
"terminal.integrated.env.windows": {
    "PYTHONPATH": "C:\\Program Files\\Side Effects Software\\Houdini 19.5.303\\python39\\libs",
    "PATH": "${env:PATH};C:\\Program Files\\Side Effects Software\\Houdini 19.5.303\\bin"
},

and set the python interpreter to this path:
"C:\Program Files\Side Effects Software\Houdini 19.5.303\bin\hython3.9.exe"


### todo:
pyside6 and use other computer to have a real pipeline