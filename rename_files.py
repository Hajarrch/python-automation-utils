import os

def rename_files(folder_path, prefix):
    """
    Renomme tous les fichiers d'un dossier en ajoutant un préfixe.

    Exemple :
    photo.jpg -> prefix_photo.jpg
    """
    if not os.path.isdir(folder_path):
        print("Le dossier n'existe pas.")
        return

    files = os.listdir(folder_path)

    if not files:
        print("Le dossier est vide.")
        return

    for filename in files:
        old_path = os.path.join(folder_path, filename)

        # On ignore les sous-dossiers
        if os.path.isdir(old_path):
            continue

        new_name = f"{prefix}_{filename}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"{filename} -> {new_name}")

    print("Renommage terminé.")


if __name__ == "__main__":
    folder = input("Chemin du dossier : ").strip()
    pref = input("Préfixe à ajouter : ").strip()
    rename_files(folder, pref)
