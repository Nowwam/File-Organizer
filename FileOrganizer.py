import os
import shutil

def organiser_fichiers(repertoire):
    
    os.chdir(repertoire)
    
    mapping_dossiers = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Vidéos': ['.mp4', '.avi', '.mov'],
        'Musique': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.tar', '.rar'],
        'Autres': []
    }
    
    for dossier in mapping_dossiers.keys():
        if not os.path.exists(dossier):
            os.makedirs(dossier)

    for nom_fichier in os.listdir(repertoire):
        if os.path.isdir(nom_fichier):
            continue
        
        _, extension = os.path.splitext(nom_fichier)
        
        deplace = False
        for dossier, extensions in mapping_dossiers.items():
            if extension.lower() in extensions:
                shutil.move(nom_fichier, os.path.join(dossier, nom_fichier))
                deplace = True
                print(f'Déplacé : {nom_fichier} vers {dossier}/')
                break
        
        if not deplace:
            shutil.move(nom_fichier, os.path.join('Autres', nom_fichier))
            print(f'Déplacé : {nom_fichier} vers Autres/')

if __name__ == "__main__":
    repertoire_cible = input("Entrez le répertoire à organiser : ")
    organiser_fichiers(repertoire_cible)