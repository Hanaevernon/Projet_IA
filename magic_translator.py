import os 
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

def adapter_message(texte_origine, style_voulu):
    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    consigne = (
    f"Tu es un expert en communication. Reformule le texte suivant "
    f"dans le style : {style_voulu}."
    "Réponds uniquement avec les texte reformulé."
)

    data = {
    "model": "mistral-small-latest",
    "messages": [
        {"role": "system", "content": consigne},
        {"role": "user", "content": texte_origine}
    ]
}

    response = requests.post(url, json=data, headers=headers)
    resultat_brut = response.json()
    
    if 'choices' in resultat_brut:
        return resultat_brut['choices'][0]['message']['content']
    else:
        return f"Erreur de l'IA : {resultat_brut}"

if __name__ == "__main__":
    print("---BIENVENUE DANS MAGIC TRANSLATOR---")

    # on demande à l'utilisature d'écrire son texte
    mon_texte = input("Entrez le message à transformer :")

    # on demande le style 
    mon_style = input("En quel style/langue voulez vous le tranformer ?")

    # on appelle la fonction 
    resultat = adapter_message(mon_texte, mon_style)

    print("\n---RESULTAT---")
    print(resultat)
    
 