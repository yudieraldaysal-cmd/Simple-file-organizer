import os
import shutil
from tqdm import tqdm
from hasher import get_file_hash
from config import EXT_MAP, UNKNOWN_CATEGORY, EMPTY_DIR_NAME
from logger import setup_logger


def create_progress(total, desc = "Organizer progress"):
    return tqdm(total = total, desc = desc, unit = 'files', dynamic_ncols = True)

def scaan_files(root_dir):
    file_list = []
    # Solo procesar archivos directamente en el directorio raíz
    # No entrar en ninguna subcarpeta
    try:
        for item in os.listdir(root_dir):
            item_path = os.path.join(root_dir, item)
            # Solo agregar archivos, ignorar subcarpetas
            if os.path.isfile(item_path):
                file_list.append(item_path)
    except Exception as e:
        print(f"Error al escanear directorio: {e}")
            
    return file_list

def ask_user_collision(src, dest):
    # Ask the user how to clear da collision
    # Returns 'skip', 'overwrite', 'rename'
    print(f"\n[!] Collision: '{src}'")
    print(f"    It's already in the destiny: '{dest}' with different content.")
    print("\n=========OPTIONS==========""\ns (Skip)""\no (Overwrite)""\nr (Rename)")
    
    while True:
        choice = input("     Choice [s, o, r]: ").lower()
        if choice == "s":
            return 'skip'
        if choice == 'o':
            return 'overwrite'
        if choice == 'r':
            return 'rename'
        else:
            print("      INVALID OPTION")
            
            
def organize(root_dir):
    logger = setup_logger()
    logger.info("Starting in: {root_dir}")
    
    # Getting all da files
    files = scaan_files(root_dir)
    
    # exclude file.log if it's in the same directory
    log_path = os.path.join(root_dir, 'organizer.log')
    files = [f for f in files if os.path.abspath(log_path)]
    
    total = len(files)
    if total == 0:
        logger.info("No files to organize")
        return
    
    progress = create_progress(total)
    
    for src in files:
        progress.update(1)
        
        # Category for extension
        ext = os.path.splitext(src)[1].lower()
        category = EXT_MAP.get(ext, UNKNOWN_CATEGORY)
        
        dest_dir = os.path.join(root_dir, category)
        pp = os.path.join(dest_dir, os.path.basename(src))
        dest = os.path.abspath(pp)
        
        
        # If origen n destiny are the same, skip
        if os.path.abspath(src) == os.path.abspath(dest):
            logger.info("Already organize: {src}, skipping")
            
        # Create dir_folder    
        os.makedirs(dest_dir, exist_ok = True)
        
        if os.path.exists(dest):
            # Compare content
            if os.path.getsize(src) == os.path.getsize(dest):
                hash_src = get_file_hash(src)
                hash_dest = get_file_hash(dest)
                if hash_src == hash_dest:
                    # Same content, skipping
                    logger.info(f"Skipping, same file found: '{src}'")
                    continue
                
                
            action = ask_user_collision(src, dest)
            if action == 'skip':
                logger.info(f"Skipping by user order")
                continue
            
            if action == "overwrite":
                logger.info(f"Overwritting file: '{dest}' with '{src}'")
                if os.path.isdir(dest): # Just in case, for safeness
                    shutil.rmtree(dest)
                    
            if action == "rename":
                base, ext_file = os.path.splitext(os.path.basename(src))
                counter = 1
                new_dest = dest
                while os.path.exists(new_dest):
                    new_name = f"{base} ({counter}){ext_file}"
                    new_dest = os.path.join(dest_dir, new_name)
                    counter += 1
                    dest = new_dest
                    logger.info(f"File renamed into: '{dest}'")
                    
        # Time to move de file
        shutil.move(src, dest)
        logger.info(f"File moved: '{src}' --> '{dest}'")
        
    progress.close()
    logger.info("THE ORGANIZER HAS ENDED THE TASK")
        
        
        
        