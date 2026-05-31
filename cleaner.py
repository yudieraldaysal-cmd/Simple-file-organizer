import os
import shutil
from config import EMPTY_DIR_NAME

def move_empty_folders(root_dir):
    # SE ENTIENDE LO QUE HACE LA FUNCION
    empty_dir = os.path.join(root_dir, EMPTY_DIR_NAME)
    os.makedirs(empty_dir, exist_ok = True)
    
    
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown = False):
        # Do not process the empty_dir itself
        
        if os.path.abspath(dirpath) == os.path.abspath(empty_dir):
            continue
        
        if not filenames and not dirnames:
            try:
                dest = os.path.join(empty_dir, os.path.basename(dirpath))
                
                if os.path.exists(dest):
                    base = os.path.basename(dirpath)
                    counter = 1
                    while os.path.exists(dest):
                        dest = os.path.join(empty_dir, f"{base} ({counter})")
                        counter += 1
                shutil.move(dirpath, dest)
                print(f"Empty folder moved: '{dirpath}' --> '{dest}'")
            
            except Exception as e:
                print(f"Cannot move da folder '{dirpath}': {e}")
                