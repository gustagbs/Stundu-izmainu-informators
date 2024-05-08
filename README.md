# Stundu izmaiņu informātors
#### Apraksts:
Programma “Stundu izmaiņu informātors” ir programma, kas aptrādā datus un izmantojot datubāzes, veido galaproduktu. 
Produkts sastāvēs gan no saskarnes, gan datubāzēm. 
Programmas funckijas nodrošinās vēlamu izvadīto rezultātu. Programmatūras mērķis ir sniegt ērtāk uzskatāmas stundu izmaiņas skolēniem, nemainot ierasato izmaiņu ievades kārtību skolotājiem.

Programmas darītais
-PROGRAMMAS LIETOTĀJU SASKARNE

-STUNDU SARAKSTU IZVEIDE (BUS VELAK UN SPECIFIKACIJA ARI ES APSOLU)
##### Apakšnodaļa pēc funkcionalitātes
Ko dara programmā šī funkcija
#### Instalēšana:
Visas pip instalējamās bibliotēkas, pa vienai katrā rindā

-tikinter

-sqlite3

-csv

-tabulate
#### Lietošana:
-  Augšupielādēt failus - izmainas_code.py, user_interface_code.py, saraksti.db un salikt tos vienā mapē.

- Šo mapi atvērt, kādā kodu redaktora, kā piemēram Visual Studio Code.

- Obligāti iepriekš nolādēt visas augstāk norādītās bibliotēkas

- Palaižot failu izmainu_code.py atvērsies logs ar lietotāju saskarni. 

- Šajā logā iespējams ievadīt stundu izmaiņas. (IZMAIŅĀM JABŪT PAREIZĀ FORMĀTĀ => izvēloties skolotāju, katrā stundā jānorāda vai nu klase, vai zīme "-" (stundas nav)) Programma nav paredzēta uzķert ievades kļūdas, tāpēc tās darbība ir atkarīga no lietotāja precizitātes. Ja skolotājai ir vairāk par 1 stundu vienā laukā, tad klases atdala ar : bez atstarpes. ( Piem: 12a:12b)

- Apakšējā labajā stūri vēl ir jāizvēlas kurai dienai ir ievadītas izmaiņas. 

- Kad viss ir pareizi savadīts, jāuzspiež poga "saglabāt" un fails jasaglabā kaut kur datorā. Tad saskarne ir jāaizver ciet.

- Pēc šī tiks izvadīti laboti stundu saraksti klasēm.
TĀKĀ PROGRAMMAS DARBĪBA IR ATKARĪGA NO STUNDU SARAKSTU DATUBĀZES(KURAS SKOLAI NAV!), UN AUTORAM BIJA SLINKUMS VADĪT NESKAITĀMI DAUDZ SARAKSTUS, PROGRAMMA NEVAR IZVEIDOT SARAKSTUS VISĀM KLASĒM.
Ja nu gadījuma interesē reāli piemēri var izveidot saraksti.db datubāze klašu stundu sarakstus. Pēc parauga var saprast kā sataisīt sarakstu. Nosaukumam tabulai jābūt _xy x-cipars y-burts. Man nebija visam laiks
#### Licence:
Apache 2.0
