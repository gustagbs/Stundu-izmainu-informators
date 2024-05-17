# Stundu izmaiņu informātors
#### Apraksts:
Programma “Stundu izmaiņu informātors” ir programma, kas aptrādā datus un izmantojot datubāzes, veido galaproduktu. 
Produkts sastāvēs gan no saskarnes, gan datubāzēm. 
Programmas funckijas nodrošinās vēlamu izvadīto rezultātu. Programmatūras mērķis ir sniegt ērtāk uzskatāmas stundu izmaiņas skolēniem, nemainot ierasato izmaiņu ievades kārtību skolotājiem.

#### Programmas darītais
UI izveidei tika lietota Python iebūvētā bibliotēka Tkinter. Ar Tkinter biblotēkas palīdzbu tiek izveidots uznirstošais logs ar UI. UI nodrošina veiksmīgu izmaiņu ievadi. Ievadītās izmaiņas ir tādā pašā formātā, kādas tās ir atrodamas Valmieras Valsts ģimnāzijas skolas mājaslapā. Saglabājot ievadītās izmaiņas, tās tiek ne tikai saglabātas teksta failā datorā, bet arī SQL datubāzē.
Lai atvieglotu lietotāju saskarnes lietojamību, tika izveidoti divi nolaižamās izvēlnes logi. Dotajos logos jau ir dotas izvēles. Tas likvidē iespēju kļūdīties vadot iekšā skolotāju vārdus un dienas nosaukumu.


Lai nodrošinātu programmas vēlamo funkcionalitāti, autors izvēlējas izveidot speciālu algortimu. Algortima darbība tiek veicināta ar cikliem. Kods algoritmam ir zem funkcijas, kurai tiek padoti vairāki mainīgie: izvēlētās klases stundu saraksts, izmaiņu saraksts, diena, un izvēlētās klases indeks. Algoritma darbība sastāv no 3 galvenajiem cikliem:
- Pamatcikls
- Stundu cikls
- Izmaiņu cikls 
Katrā no šiem cikliem notiek vairākas darbības

#### Pamatcikls sagatavo algoritma darbību:
Sagatavo list ar dotās klases stundu sarakstu attiecīgi izvēlētajā dienā.
#### Stundu cikls:
Iet pa vienam cauri stundu sarakstam attiecīgajai klasei.
Ja attiecīgās stundas skolotājam ir izmaiņas, pāriet uz izmaiņu ciklu.

#### Izmaiņu cikls:
Reizē pa vienai stundai iet cauri gan attiecīgās skolotājas izmaiņām, gan attiecīgās klases stundām.
Ja attiecīgajā stundā, klases stundu sarakstā oriģināli ir stunda pie attiecīgi pārbaudāmās skolotājas, bet izmaiņās šai skolotājai nav stunda pie šobrīd pārbaudāmās klases, šīs skolotājas vārds tiek izņemts no attiecīgās stundas.
Ja izmaiņās attiecīgajai skolotājai ir ierakstīta pārbaudāmā klase, tad attiecīgās stundas vietā tiek pievienots attiecīgās skolotājas vārds.
Ciklam noslēdzoties atgriežas uz stundu ciklu.

Šis algoritms atkārtojas priekš katras klases, kurai stundu saraksti ir ievadīti datubāzē. Algoritma beigās tiek izprintēts labotais stundu saraksts


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
