import os
import requests
from dotenv import load_dotenv
import json

# On charge la clé depuis le fichier .env
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

def expertise_strat37(message_client):
    url = "https://api.mistral.ai/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": "mistral-small-latest",
        "messages": [
                {"role": "system", "content": "Réponds en JSON avec les clés: 'categorie', 'urgence' (UN CHIFFRE de 1 à 10), 'resume'."},
                {"role": "user", "content": message_client}
        ],
        "response_format": {"type": "json_object"}
     }
    

    # Envoi de la requête à Mistral
    response = requests.post(url, json=data, headers=headers)
    # On récupère le texte JSON envoyé par l'IA
    texte_json = response.json()['choices'][0]['message']['content']
    
    # On transforme ce texte en un "dictionnaire" Python (un objet manipulable)
    donnees_triees = json.loads(texte_json)
    
    return donnees_triees
   
    
    

# --- TEST ---
if __name__=="__main__":
    # on prépare une liste de message
    liste_problemes = [
        "Le site bug sur Iphone 15",
        "On a besoin d'un nouveau logo pour demain",
        "Notre chiffre d'affaires baisse depuis des mois",
        "L'automatisation ne fonctionne pas sur mon pc"
    ]

    print("---DEBUT DE L'ANALYSE AUTOMATISEE---")

    # La boucle 'for' commece ici
    # Pour chaque 'p' contenue dans 'liste_probleme'...
    for p in liste_problemes:
        analyse = expertise_strat37(p)

        # print(f"DEBUG - Score reçu de l'IA : {analyse['urgence']}") # On vérifie ce que l'IA a écrit
        # on transforme l'urgance en nombre entier (int) pour pouvoir comparer
        try:
            score = int(analyse['urgence'])
        except:
            score = 0 # si l'ia écrit "élevée" au lieu d'un chiffre

        print(f"\n MESSAGE : {p}")

        # la condition : Si c'est très urgent
        if score == 10:
            print("!!! ALERTE : DOSSIER PRIORITAIRE !!!")
            print(f"-> ACTION : {analyse['resume']}")
        else:
            print(f"-> STATUS : Analyse classique effectuée ({score}/10)")

        # On envoie le message 'p' à l'IA
        # analyse = expertise_strat37(p)

        # #  On affiche le resultat
        # print(f"\nMESSAGE CLIENT : {p}")
        # print(f"-> CATÉGORIE : {analyse['categorie'].upper()}")
        # print(f"-> URGENCE : {analyse['urgence']}/10")
        # print(f"-> RÉSUMÉ : {analyse['resume']}")
        # print("-" * 40)
        