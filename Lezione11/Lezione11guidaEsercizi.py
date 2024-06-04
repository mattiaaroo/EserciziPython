# Sistema di Prenotazione Cinema

# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
#Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
#Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
# Classi:
# - Film: Rappresenta un film con titolo e durata.
 
# - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

# Metodi:
#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
# - Cinema: Gestisce le operazioni legate alla gestione delle sale.

# Metodi:
#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

# Test case:

#     Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
#     Un cliente sceglie un film e prenota un certo numero di posti.
#     Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

 
 
# Gestione di un magazzino
# Scrivi un programma in Python che gestisca un magazzino. 
#Il programma deve permettere di aggiungere prodotti al magazzino, 
#cercare prodotti per nome e verificare la disponibilità di un prodotto.

# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)
 
# Definisci una classe Magazzino con i seguenti metodi:
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
# Test case:

#     Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
#     Il sistema cerca un prodotto per verificare se esiste nell'inventario.
#     Il sistema verifica la disponibilità dei prodotti in inventario.

