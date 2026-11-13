#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:16:20 2026

@author: meriamberraho
Arbeidskrav 2 PY1010 USN

"""


#%% Pakker

import numpy as np

import matplotlib.pyplot as plt


#%% Oppgave 1

#Koden fra oppgaven
alder = int(input('Hvilket år er du født?'))
#Litt forvirrende at den er kalt alder og ikke fødeår, for det spørres jo om fødeår, ikke alder....
#Definerer 20224 som oppgaven ber om
aar = 2024 

#Lager variabel for 2026, fordi det er dagens år
riktigaar = 2026

#2024 minus fødeår gir automatisk alder
faktiskalder = aar - alder

#Du eller Jeg er passende tenker jeg..
navn = 'Du'
navn2 = 'du'

#Variabel som matcher 2026, selv om oppgaven spørr om 2024. Bare tillegg
rettalder = riktigaar - alder


#Printer tekst som svar til første kode (linje14)
print(f'{navn} er {faktiskalder} år og født i {alder} i utgangen av 2024')

print(f' I 2026 er {navn2} {rettalder} år og ble født i {alder}')


#%% Oppgave 2

antall_elever = int(input('Skriv antall elever:'))

#1 elev spiser 1/4 pizza svs. 4 spiser 1 hel
pizza = antall_elever / 4

#bruke np funksjon for å runde opp til heltall
hele_pizzaer = np.ceil(pizza)

#hele_pizz er float og må bli int for å bli heltall
hele_pizzaer = int(hele_pizzaer)


#Printe tekst svar for input om antall elever
print(f'Hvis {antall_elever} elever er på klassefesten må lærerne kjøpe {hele_pizzaer} pizzaer')



#%%  Oppgave 3

#np er øverst i dokumentet, laster bare øverst
#Lage funksjonen
def grad_til_rad(v_grad):
    v_rad = v_grad * np.pi/180 # regne radianer
    return v_rad #gir svaret

v_grad = float(input('Skriv inn gradtallet:'))

#Bruker funksjonen som ble lagd på gradtallet brukeren skriver inn
v_rad = grad_til_rad(v_grad)

#Printe tekst svar for radianer ved bestemte grader
print(f'Hvis gradtallet er {v_grad}, er radiantallet: {v_rad}')

#%% Oppgave 4

# a) opretter ordboken
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 9.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# b) lager spørsmålet
land = input('Hvilken land lurer du på?')

#definerer variabler print skal bruke for å svare på spørsmålet
hovedstad = data[land][0] #0 fordi det er plasseringen til oslo
innbyggere = data[land][1] #1 fordi det er plasseringen til tot-pop i "Norge"

#Printer ut tekstbesvarelse
print(f'{hovedstad} er hovedstaten i {land} og det er {innbyggere} mill. innbyggere i {land}')


# c) 
#Legge til spørsmålene som trengs og som vil bli variablene som legges til i ordboken
nytt_land = input('Hvilket land vil du legge til? ')
ny_hovedstad = input('Hva er hovedstaden?' )
nye_innbyggere = float(input('Antall innbyggere i millioner? '))


#for å legge til det nye landet i ordboken

data[nytt_land] = [ny_hovedstad, nye_innbyggere]

print(f'Den oppdaterte ordboken ser slik ut: {data}')

#%% Oppgave 5

#Definerer funksjon for å finne areal og ytre omkret
    #jeg skriver formelen brukt basert på teksten i arbeidskravet etter funksjonene #:
def figur(a, b):
    r = a / 2  #a er radiusen til sirkelen, må deles på 2 fordi sirkelen er halv
    hyp = np.sqrt(a**2 + b**2) #standard pytagoras. + fordi vi finner hypotenusen, ikke -
    #regner areal
    trekant_ar = (a * b) / 2 # g * h / 2 areal trekant formelen
    halvsirkel_ar = np.pi*(r**2) / 2 #bruker areal sirkel formelen men deler på 2
    areal = trekant_ar + halvsirkel_ar # plusser arealene til trekant og sirkel (hele figuren)
    #omkrets, ikke areal
    bue = (2 * np.pi*r ) / 2  #omkrets sirkel, men deles på 2 igjen fordi sirkelen er halv
    omkrets = b + hyp + bue #plusser trekanthøyden med buen og så skrå trekanthøyde (hyp) for ytre omkrets av hele figuren
    return areal, omkrets 



a = float(input('Hvis sirkelomkrets a er:')) #float for å respektere desimaler
b = float(input('og trekanthøyde b er:'))
#tilegner A og O de regnede verdiene innsendt a og b får etter de blir "kjørt gjennom funksjonen"/regnet ut er def(inisjon).
A, O = figur(a, b) 

#Printer tekst og begrenser til 2 desimaler med :.2f
print(f'Da er areal {A:.2f}, og ytre omkrets {O:.2f} ')


#%% Oppgave 6

#funksjon f(x) = -x**2 - 5

x = np.linspace(-10, 10, 200)
y = (-x**2)- 5 


plt.plot(x, y) #tilegner plotten verdiene x og y
plt.xlabel("X akse") #skriver ut x aksen
plt.ylabel("Y akse") #skriver ut y aksen
plt.grid() #standard grid
plt.show() #vise plotten




