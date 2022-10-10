print('\n\n\nWelkom bij de voetbal quizzzzz')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=3
 
if antwoord.lower()=='ja':

    print('\n\nMooi. Dan gaat de voetbal Quiz beginnen!!\nGeef bij iedere vraag als antwoord de goede naam.\n\n')

    antwoord=input('Vraag 1: Heeft het Nederlands elftal in 2010 het wk gewonnen? ')
    if antwoord.lower()=='nee' or antwoord.lower()=='ja':
        punten += 1
        print('goed!')
    else:
        print('fout!')
 
    antwoord=input('Vraag 2: van wie heeft Nederland verloren in 2010 in de finale? ')
    if antwoord.lower()=='spanje':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 3: hoeveelste is Nederland geworden bij het WK in 2014? ')
    if antwoord.lower()=='halve finale':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('vraag 4: Wie heeft er gewonnen met penaltys in 2014 Nederland tegen Argentinie?')
    if antwoord.lower()=='argentinie':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('vraag 5: Wanneer speelt Nederland het volgende WK?')
    if antwoord.lower()=='21 november 2022':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('vraag 6: Tegen wie speelt nederland het 1e WK?')
    if antwoord.lower()=='senegal':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('vraag 7: hoeveel heeft Nederland gespeeld tegen belgie op vrijdag 25-09-2022?')
    if antwoord.lower()=='1-0':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('vraag 8: hoeveel is ajax-napoli geworden op 4 oktober 2022 voor de champions league?')
    if antwoord.lower()=='1-6':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('vraag 9: Wk 2010, hoeveel was het geworden tussen Nederland-brazilie?')
    if antwoord.lower()=='2-1':
        punten += 1
        print('goed')
    else:
        print('fout')

    if antwoord.lower()=='Wesley sneijder':
        punten += 1
        print('goed')
    else:
        print('fout')




    print('\n\nBedankt voor het spelen van de voetbal Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 6: print('Goed bezig!')
    else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')

elif antwoord.lower()=='nee':
    print('NIET ZO VEEL NADENKEN EN GEWOON DOEN KLEINE SPELER.\nPFFFFF!')
else:
    print('Dit antwoord ken ik niet!')