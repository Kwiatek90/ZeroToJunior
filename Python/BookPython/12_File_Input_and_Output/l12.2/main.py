import pathlib 


cwd = pathlib.Path.cwd() 

path = cwd / "Python" / "BookPython"


print(path.is_dir())
    
