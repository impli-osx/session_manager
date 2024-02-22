import requests
import json

# Remplacez ces valeurs par les informations spécifiques à votre configuration OPNsense
OPNSENSE_URL = "https://adresse_de_votre_opnsense"
API_KEY = "votre_clef_api"
API_SECRET = "votre_secret_api"

# Endpoint et données pour la génération du token
endpoint = "/api/captiveportal/voucher/generateVouchers"
data = {
    "provider": "nom_de_votre_provider"
}

# En-tête pour l'authentification
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}:{API_SECRET}"
}

# Effectuer la requête POST pour générer le token
response = requests.post(OPNSENSE_URL + endpoint, headers=headers, data=json.dumps(data))

# Vérifier le code de statut de la réponse
if response.status_code == 200:
    # La requête a réussi, afficher les informations renvoyées par l'API
    token_info = response.json()
    print("Token généré avec succès :")
    print(token_info)
else:
    # La requête a échoué, afficher le code d'erreur
    print("Échec de la génération du token. Code d'erreur :", response.status_code)



## Venant de la doc de OPNsense
# https://docs.opnsense.org/development/how-tos/api.html
# https://docs.opnsense.org/development/api/core/captiveportal.html

import json
import requests

# define endpoint and credentials
api_key = 'w86XNZob/8Oq8aC5hxh2he+vLN00r0kbNarNtdpoQU781fyoeaOBQsBwkXUt'
api_secret = 'puOyw0Ega3xZXeD26XVrJ5WYFepOseySWLM53pJASeTA3'
url = 'https://192.168.1.1/api/core/firmware/status'

# request data
r = requests.get(url,
                 verify='OPNsense.pem',
                 auth=(api_key, api_secret))

if r.status_code == 200:
    response = json.loads(r.text)

    if response['status'] == 'ok':
        print ('OPNsense can be upgraded')
        print ('download size : %s' % response['download_size'])
        print ('number of packages : %s' % response['updates'])
        if response['upgrade_needs_reboot'] == '1':
            print ('REBOOT REQUIRED')
    elif 'status_msg' in response:
        print (response['status_msg'])
else:
    print ('Connection / Authentication issue, response received:')
    print r.text