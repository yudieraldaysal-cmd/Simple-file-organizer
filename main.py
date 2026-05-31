import sys
import os
from organizer import organize
from cleaner import move_empty_folders

def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        # Modo interactivo: preguntar carpeta
        print("=== File Organizer ===")
        target = input("Ingresa la ruta de la carpeta a organizar: ").strip()
        if not target:
            print("Error: No ingresaste ninguna ruta.")
            input("Presiona Enter para salir...")
            sys.exit(1)

    if not os.path.isdir(target):
        print(f"Error: '{target}' no es una carpeta válida.")
        if len(sys.argv) != 2:
            input("Presiona Enter para salir...")
        sys.exit(1)

    print(f"\nOrganizando archivos en: {target}\n")
    organize(target)
    move_empty_folders(target)

    if len(sys.argv) != 2:
        input("\nOrganización completada. Presiona Enter para salir...")

if __name__ == '__main__':
    main()