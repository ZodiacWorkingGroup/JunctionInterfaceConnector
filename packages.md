It is recommended that one runs Junction on an up-to-date Python 3 installation, such as Anaconda (preferably anaconda, as that is what this was built on). Many packages are prefered to be installed to run Junction, but most aren't necessary. 

Required:
* sys -- System stuff, unicode support
* os -- os.system() and filesystem things and such
* socket -- Networking

Recommended:
* Skype4Py ([[https://github.com/FloatingGhost/skype4py]] (you'll need to 2to3 the setup.py, if memory serves and this is the correct one)) -- Skype API
* win32com (windows) -- OS interfaces
* pyhk (windows only) (you'll have to 2to3 it) -- Hotkeys
* pyHooks ([[http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook]]) (windows) -- pyhk dependency
* Tkinter (maybe) -- GUI
* requests -- Web stuff
* http -- For http.server (handling POST)

Possible future use:
* NumPy -- Data analysis
* SciPy -- Science!
* PyBrain -- Neural Networking/Machine Learning

Actions on your part:
* Port foreward port 80
** Get static IP