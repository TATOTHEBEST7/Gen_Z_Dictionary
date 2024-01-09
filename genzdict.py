parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

gen_z_dizionario = {
    "LOL": "Laugh Out Loud - Ridere forte",
    "TBH": "To Be Honest - Per essere onesti",
    "YOLO": "You Only Live Once - Si vive solo una volta",
    "SQUAD": "Squadra in inglese; Un gruppo di amici molto unito",
    "CRINGE": "qualcosa di imbarazzante",
    "SHEESH": "[DEPRECATO] disapprovazione leggera",
    "CREEPY": "spaventoso, inquietante",
}

spiegazione = gen_z_dizionario.get(parola)

if parola in gen_z_dizionario.keys():
    print(gen_z_dizionario.get(parola))
    
else: 
    print("mi dispiace, non ho ancora aggiunto questa parola al dizionario, oppure hai sbagliato sintassi :)")