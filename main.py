#skapa filer om dom ej finns
def kontroll_av_filer():
    lista_av_filnamn = ["books.txt", "users.txt", "loans.txt"]
    for filnamn in lista_av_filnamn:
        with open (filnamn, "a", encoding="utf-8"): 
            pass


#meny
def visa_meny():
    print("==============================")
    print("        LIBRARY SYSTEM")
    print("==============================")
    print()
    print("1. Lista böcker")
    print("2. Lägg till bok")
    print("3. Ta bort bok")
    print("4. Registrera användare")
    print("5. Låna bok")
    print("6. Lämna tillbaka bok")
    print("7. Sök bok")
    print("8. Visa statistik")
    print("9. Exportera rapport")
    print("10. Ta bort användare")
    print("0. Avsluta")
    print()


#1 Lista böcker
# Visar alla böcker och om de går att låna.
def lista_bocker():
    with open ("books.txt", "r") as bokfil:
         bokrader = bokfil.readlines()
        
    # Här samlar vi bokinformationen innan den skrivs ut.
    bocker = []

    for bokrad in bokrader:
        bok_falt = bokrad.strip().split(";")

        bok_id = bok_falt[0]
        titel = bok_falt[1]
        fornamn = bok_falt[2]
        efternamn = bok_falt[3]
        utlanad = bok_falt[4]

        bocker.append([titel, bok_id, fornamn, efternamn, utlanad])

    # Sorterar listan efter titel, som ligger först i varje post
    bocker.sort()
    print("ID Titel Författare Status")
    print()
    for bok in bocker:
        titel = bok[0]
        bok_id = bok[1]
        fornamn = bok[2]
        efternamn = bok[3]
        utlanad = bok[4]

        # 0 betyder tillgänglig och 1 betyder utlånad.
        if utlanad == "0":
            status = "Tillgänglig"
        else:
            status = "Utlånad"
        forfattare = fornamn + " " + efternamn
        print(f"{bok_id} {titel} {forfattare} {status}")
        

#2 Lägg till bok
# Frågar efter uppgifter för en ny bok.
def lagg_till_bok():
    titel = input("Titel: ")
    fornamn = input("Författarens förnamn: ")
    efternamn = input("Författarens efternamn: ")

    with open("books.txt", "r") as bokfil:
        bokrader = bokfil.readlines()
    
    # Letar efter det högsta befintliga bok-IDt
    hogsta_bok_id = 0
    for bokrad in bokrader:
        bok_id = int(bokrad.split(";")[0])
        if bok_id > hogsta_bok_id:
            hogsta_bok_id = bok_id

    # Den nya boken får nästa ID efter det högsta
    nytt_bok_id = hogsta_bok_id + 1

    # Lägger till boken sist i filen utan att ta bort de gamla.
    with open("books.txt", "a") as bokfil:
        bokfil.write(f"{nytt_bok_id};{titel};{fornamn};{efternamn};0\n")

    print("Boken har lagts till.")
    print()
    print("ID:", nytt_bok_id)


#3 Ta bort bok
# Tar bort en bok om den finns och inte är utlånad.
def ta_bort_bok():
    bok_id = input("Bok-ID: ")

    with open("books.txt", "r") as bokfil:
        bokrader = bokfil.readlines()


    for bokrad in bokrader:
        bok_falt = bokrad.strip().split(";")
        
        # Jämför användarens val med bok-ID:t i filen
        if bok_falt[0] == bok_id:
            utlanad = bok_falt[4]

            # Utlånade böcker får inte tas bort.
            if utlanad == "1":
                print("Boken är utlånad och kan inte tas bort.")
                return

            else:
                # Tar bort den valda raden ur listan med böcker.
                bokrader.remove(bokrad)
                # Skriver om bokfilen med de rader som finns kvar.
                with open("books.txt", "w") as bokfil:
                    bokfil.writelines(bokrader)
                
                print("Boken har tagits bort.")
                return
    print("Boken finns inte.")

   
#4 Registrera användare
# Registrerar en ny användare i users.txt.
def registrera_anvandare():
    fornamn = input("Förnamn: ")
    efternamn = input("Efternamn: ")

    with open("users.txt", "r") as userfil:
        userrader = userfil.readlines()
    
    # Letar fram högsta användar-ID:t i filen.
    hogsta_user_id = 0
    for userrad in userrader:
        user_id = int(userrad.split(";")[0])
        if user_id > hogsta_user_id:
            hogsta_user_id = user_id
    
    # Nya användaren får ett nytt ID och börjar med noll lån.
    nytt_user_id = hogsta_user_id + 1

    with open("users.txt", "a") as userfil:
        userfil.write(f"{nytt_user_id};{fornamn};{efternamn};0\n")
    
    print("Användaren har registrerats.")
    print()
    print("ID:", nytt_user_id)


#5 Låna bok
# Lånar ut en bok och uppdaterar de tre textfilerna.
def lanabok():
    bok_id = input("Bok-ID: ")
    user_id = input("Användar-ID: ") 

    with open("books.txt", "r") as bokfil:
        bokrader = bokfil.readlines()   
    
    # Utgår från att bok-ID:t inte har hittats ännu.
    bok_hittad = False
    for bokrad in bokrader:
        bok_falt = bokrad.strip().split(";")
        if bok_falt[0] == bok_id:
            bok_hittad = True
            if bok_falt[4] == "1":
                print("Boken är redan utlånad.")
                return
            
    # Avbryter om bok-ID:t inte fanns i books.txt.
    if not bok_hittad:
        print("Boken finns inte.")
        return

    with open("users.txt", "r") as userfil:
        userrader = userfil.readlines()
    
    for userrad in userrader:
        user_falt = userrad.strip().split(";")
        if user_falt[0] == user_id:
            antal_utlanade_bocker = int(user_falt[3])
            if antal_utlanade_bocker >= 5:
                print("Användaren har redan maximalt antal lån.")
                return

    # Bygger upp filinnehållet med bokens nya status.
    nya_bokrader = []
    for bokrad in bokrader:
        bok_falt = bokrad.strip().split(";")
        if bok_falt[0] == bok_id:
            bok_falt[4] = "1"
            bokrad = f"{bok_falt[0]};{bok_falt[1]};{bok_falt[2]};{bok_falt[3]};{bok_falt[4]}\n"
            
        nya_bokrader.append(bokrad)

    with open("books.txt", "w") as bokfil:
        bokfil.writelines(nya_bokrader)
    
    # Bygger upp användarfilen med uppdaterat låneantal
    nya_userrader = []

    for userrad in userrader:
        user_falt = userrad.strip().split(";")
        if user_falt[0] == user_id:
            antal_utlanade_bocker = int(user_falt[3]) + 1
            userrad = f"{user_falt[0]};{user_falt[1]};{user_falt[2]};{antal_utlanade_bocker}\n"
        
        nya_userrader.append(userrad)

    with open("users.txt", "w") as userfil:
        userfil.writelines(nya_userrader)

    with open("loans.txt", "r") as lanfil:
        loanrader = lanfil.readlines()
  

    # Hittar nästa låne-ID genom att leta efter det högsta.
    hogsta_loan_id = 0
    for loanrad in loanrader:
        if loanrad.strip() != "":
            lan_id = int(loanrad.split(";")[0])
            if lan_id > hogsta_loan_id:
                hogsta_loan_id = lan_id

    nytt_loan_id = hogsta_loan_id + 1

    # Sparar det nya lånet i loans.txt.
    with open("loans.txt", "a") as lanfil:
        lanfil.write(f"{nytt_loan_id};{bok_id};{user_id}\n")
    
    print("Boken har lånats ut.")


#6 Lämna tillbaka bok
# Lämnar tillbaka en bok och ändrar uppgifterna i filerna.
def lamna_tillbaka_bok():
    bok_id = input("Bok-ID: ")

    with open("loans.txt", "r") as lanfil:
        loanrader = lanfil.readlines()
    

    # Samlar lånen som ska vara kvar efter återlämningen.
    nya_loanrader = []
    bok_hittad = False
    user_id = ""
    for loanrad in loanrader:
        if loanrad.strip() != "":
            # Letar efter lånet som hör till den valda boken
            loan_falt = loanrad.strip().split(";")
            if loan_falt[1] == bok_id:
                bok_hittad = True
                user_id = loan_falt[2]
            else:
                nya_loanrader.append(loanrad)
    # Om inget aktivt lån hittas avbryts återlämningen
    if not bok_hittad:
        print("Boken är inte utlånad.")
        return

    with open("books.txt", "r") as bokfil:
        bokrader = bokfil.readlines()
    

    nya_bokrader = []
    for bokrad in bokrader:
        bok_falt = bokrad.strip().split(";")
        if bok_falt[0] == bok_id:
            # Markerar att boken är tillgänglig igen.
            bok_falt[4] = "0"
            bokrad = f"{bok_falt[0]};{bok_falt[1]};{bok_falt[2]};{bok_falt[3]};{bok_falt[4]}\n"
        nya_bokrader.append(bokrad)

    with open("books.txt", "w") as bokfil:
        bokfil.writelines(nya_bokrader)
    
   
    with open("users.txt", "r") as userfil:
        userrader = userfil.readlines()
    nya_userrader = []
    for userrad in userrader:
        user_falt = userrad.strip().split(";")
        if user_falt[0] == user_id:
            # Minskar låntagarens antal aktiva lån med ett.
            antal_utlanade_bocker = int(user_falt[3]) - 1
            userrad = f"{user_falt[0]};{user_falt[1]};{user_falt[2]};{antal_utlanade_bocker}\n"
        nya_userrader.append(userrad)

    with open("users.txt", "w") as userfil:
        userfil.writelines(nya_userrader)
    

    if not bok_hittad:
        print("Boken är inte utlånad.")
        return

    # Sparar lånelistan utan det återlämnade lånet
    with open("loans.txt", "w") as lanfil:
        lanfil.writelines(nya_loanrader)
    

    print("Boken har återlämnats.")


#7 Sök bok
# Söker efter böcker med hjälp av titel eller författarnamn.
def sok_bok():
    sokterm = input("Sökterm: ")

    with open("books.txt", "r") as bokfil:
        bokrader = bokfil.readlines()
    # Ingen träff har hittats innan sökningen börjar.
    hittad = False
    for bokrad in bokrader:
        bok_falt = bokrad.strip().split(";")
        titel = bok_falt[1]
        fornamn = bok_falt[2]
        efternamn = bok_falt[3]

        # lower() gör att stora och små bokstäver behandlas lika
        if sokterm.lower() in titel.lower() or sokterm.lower() in fornamn.lower() or sokterm.lower() in efternamn.lower():
         if not hittad:
            print("ID Titel")
            print()

         print(bok_falt[0], titel)
         # Kommer ihåg att minst en bok matchade sökningen.
         hittad = True        
    # Visar ett meddelande om sökningen inte gav någon träff.
    if hittad == False:
        print("Inga böcker hittades.")


#8 Visa statistik
# Räknar samman uppgifter från böcker, användare och lån
def visa_statistik(exportfil=None):
    with open("books.txt", "r") as bokfil:
        bokrader = bokfil.readlines()
    
    with open("users.txt", "r") as userfil:
        userrader = userfil.readlines()
    
    with open("loans.txt", "r") as lanfil:
        lanrader = lanfil.readlines()
    

    # len() räknar hur många bokrader som finns i listan.
    totala_bocker = len(bokrader)
    totala_anvandare = len(userrader)
    # Räknar de lånerader som inte är tomma.
    totala_lan = 0
    for lanrad in lanrader:
        if lanrad.strip() !="":
            totala_lan = totala_lan + 1

    # Startar räknarna för tillgängliga och utlånade böcker.
    tillgangliga_bocker = 0
    utlanade_bocker = 0

    for bokrad in bokrader:
        bok_falt = bokrad.strip().split(";")
        if bok_falt[4] == "0":
            tillgangliga_bocker = tillgangliga_bocker + 1
        else:
            utlanade_bocker = utlanade_bocker + 1

    # Letar efter den användare som har flest lån.
    flest_lan = 0
    
    for userrad in userrader:
        user_falt = userrad.strip().split(";")
        antal_lan = int(user_falt[3])

        if antal_lan > flest_lan:
            flest_lan = antal_lan
    
    # Samlar alla författarnamn från bokfilen.
    forfattare_lista = []

    for bokrad in bokrader:
        bok_falt = bokrad.strip().split(";")
        forfattare = bok_falt [2] + " " + bok_falt[3]
        forfattare_lista.append(forfattare)

    # Räknar hur många böcker den vanligaste författaren har.
    flest_bocker = 0
    for forfattare in forfattare_lista:
        antal_bocker = forfattare_lista.count(forfattare)

        if antal_bocker > flest_bocker:
            flest_bocker = antal_bocker

    print(file=exportfil)
    print(f"Antal böcker: {totala_bocker}", file=exportfil)
    print(file=exportfil)
    print(f"Antal användare: {totala_anvandare}", file=exportfil)
    print(file=exportfil)
    print(f"Antal aktiva lån: {totala_lan}", file=exportfil)
    print(file=exportfil)
    print(f"Tillgängliga böcker: {tillgangliga_bocker}", file=exportfil)
    print(file=exportfil)
    print(f"Utlånade böcker: {utlanade_bocker}", file=exportfil)
    print(file=exportfil)

    # Skriver ut alla användare som delar på flest lån
    print("Användare med flest lån:", file=exportfil)
    print(file=exportfil)
    for userrad in userrader:
        user_falt = userrad.strip().split(";")

        if int(user_falt[3]) == flest_lan:
            print(f"{user_falt[1]} {user_falt[2]} ({flest_lan})", file=exportfil)
    
    print(file=exportfil)
    print("Författare med flest böcker:", file=exportfil)
    print(file=exportfil)
    # Håller reda på vilka författare som redan skrivits ut
    utskrivna_forfattare = []
    for forfattare in forfattare_lista:
        antal_bocker = forfattare_lista.count(forfattare)

        # Skriver bara ut författare på förstaplats som inte visats ännu.
        if antal_bocker == flest_bocker and forfattare not in utskrivna_forfattare:
            print(f"{forfattare} ({antal_bocker})", file=exportfil)
            utskrivna_forfattare.append(forfattare)

    
#9 Exportera rapport
def exportera_rapport():
    with open("report.txt", "w", encoding="utf-8") as rapportfil:
        visa_statistik(rapportfil)
    print("Rapporten exporterad till report.txt")
   

#10 Ta bort användare
# Tar bort en användare så länge den inte har aktiva lån.
def ta_bort_anvandare():
    user_id = input("Användar-ID: ")

    with open("users.txt", "r") as userfil:
        userrader = userfil.readlines()
    
    with open("loans.txt", "r") as lanfil:
        lanrader = lanfil.readlines()
    har_aktiva_lan = False
    for lanrad in lanrader:
        if lanrad.strip() != "":
            lan_falt = lanrad.strip().split(";")
            if lan_falt[2] == user_id:
                har_aktiva_lan = True
    
    for userrad in userrader:
        user_falt = userrad.strip().split(";")
        
        if user_falt[0] == user_id:
            antal_utlanade_bocker = int(user_falt[3])

            # Användare med aktiva lån får inte raderas.
            if antal_utlanade_bocker > 0 or har_aktiva_lan:
                print("Användaren har aktiva lån och kan inte tas bort.")
                return

            else:
                # Tar bort användarens rad ur listan
                userrader.remove(userrad)
                with open("users.txt", "w") as userfil:
                    userfil.writelines(userrader)
                
                print("Användaren har tagits bort.")
                return
    print("Användaren finns inte.")


kontroll_av_filer()

# Meny val
# Menyn upprepas tills användaren väljer 0.
while True:
    visa_meny()
    # Läser in menyvalet som text.
    val = input("Val: ")
    
    if val not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("Ogiltigt val. Ange en siffra mellan 0 och 10.")

    if val == "1":
        lista_bocker()
        input("Tryck Enter för att återgå till menyn…")
    if val == "2":
        lagg_till_bok()
        input("Tryck Enter för att återgå till menyn…")
    if val == "3":
        ta_bort_bok()
        input("Tryck Enter för att återgå till menyn…")

    if val == "4":
        registrera_anvandare()
        input("Tryck Enter för att återgå till menyn…")

    if val == "5":
        lanabok()
        input("Tryck Enter för att återgå till menyn…")

    if val == "6":
        lamna_tillbaka_bok()
        input("Tryck Enter för att återgå till menyn…")

    if val == "7":
        sok_bok()
        input("Tryck Enter för att återgå till menyn…") 

    if val == "8":
        visa_statistik()
        input("Tryck Enter för att återgå till menyn…") 

    if val == "9":
        exportera_rapport()
        input("Tryck Enter för att återgå till menyn…") 

    if val == "10":
        ta_bort_anvandare()
        input("Tryck Enter för att återgå till menyn…")

    # Avslutar loopen och därmed programmet
    if val == "0":
        break