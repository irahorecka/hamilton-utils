import os

def admin_rm(path_, file_):    
    try:
        os.remove(os.path.join(path_, file_))
    except PermissionError as e:
        print(e)

        
