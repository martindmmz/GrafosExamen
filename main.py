from grafosConPesos import *

salinacruz = "Salina Cruz"
tehuantepec = "Tehuantepec"
juchitan = "Juchitan"
ixtepec = "Ixtepec"
tonala = "Tonala"
pijijiapan = "Pijijiapan"
huixtla = "Huixtla"
tuxtlagutierrez = "Tuxtla Gutierrez"
comitan = "Comitan"
sancristobal= "San Cristobal"
ocosingo = "Ocosingo"
palenque = "Palenque"
huatulco = "Huatulco"
oaxaca = "Oaxaca"
villahermosa = "Villahermosa"
ciudaddelcarmen = "Ciudad del Carmen"
campeche = "Campeche"
merida = "Merida"
cancun = "Cancun"
playadelcarmen = "Playa del Carmen"
cardenas = "Cardenas"
coatzacoalcos = "Coatzacoalcos"
minatitlan = "Minatitlan"
acayucan = "Acayucan"
cordoba = "Cordoba"
orizaba = "Orizaba"
puebla = "Puebla"
veracruz = "Veracruz"
pozarica = "Poza rica"
tuxpan = "Tuxpan"
tampico = "Tampico"
matamoros = "Matamoros"
tapachula = "Tapachula"
puertoescondido = "Puerto escondido"
chetumal = "Chetumal"
reynosa = "Reynosa"
ixtaltepec = "Ixtaltepec"
cardenas = "Cardenas"
ciudaddemexico = "Ciudad de Mexico"
xalapa = "Xalapa"


grafo = Grafo()
agregar(grafo, salinacruz)
agregar(grafo, tehuantepec)
agregar(grafo, juchitan)
agregar(grafo, ixtepec)
agregar(grafo, tonala)
agregar(grafo, pijijiapan)
agregar(grafo, huixtla)
agregar(grafo, tuxtlagutierrez)
agregar(grafo, comitan)
agregar(grafo, sancristobal)
agregar(grafo, ocosingo)
agregar(grafo, palenque)
agregar(grafo, salinacruz)
agregar(grafo, huatulco)
agregar(grafo, oaxaca)
agregar(grafo, villahermosa)
agregar(grafo, ciudaddelcarmen)
agregar(grafo, campeche)
agregar(grafo, merida)
agregar(grafo, cancun)
agregar(grafo, playadelcarmen)
agregar(grafo, cardenas)
agregar(grafo, coatzacoalcos)
agregar(grafo, minatitlan)
agregar(grafo, acayucan)
agregar(grafo, cordoba)
agregar(grafo, orizaba)
agregar(grafo, puebla)
agregar(grafo, acayucan)
agregar(grafo, veracruz)
agregar(grafo, pozarica)
agregar(grafo, tuxpan)
agregar(grafo, tampico)
agregar(grafo, matamoros)
agregar(grafo, tapachula)
agregar(grafo, puertoescondido)
agregar(grafo, chetumal)
agregar(grafo, reynosa)
agregar(grafo, ixtaltepec)
agregar(grafo, cardenas)
agregar(grafo, ciudaddemexico)
agregar(grafo, xalapa)



relacionar(grafo, salinacruz, tehuantepec, 23)
relacionar(grafo, tehuantepec, oaxaca, 248)
relacionar(grafo, juchitan, tehuantepec, 26)
relacionar(grafo, juchitan, ixtepec, 19)
relacionar(grafo, ixtepec, ixtaltepec, 4)
relacionar(grafo, juchitan, tonala, 172)
relacionar(grafo, tonala, pijijiapan, 76)
relacionar(grafo, pijijiapan, huixtla, 93)
relacionar(grafo, huixtla, tapachula, 42)
relacionar(grafo, tonala, tuxtlagutierrez, 173)
relacionar(grafo, tuxtlagutierrez, villahermosa, 252)
relacionar(grafo, comitan, sancristobal, 88)
relacionar(grafo, sancristobal, ocosingo, 88)
relacionar(grafo, ocosingo, palenque, 103)
relacionar(grafo, palenque, villahermosa, 145)
relacionar(grafo, salinacruz, huatulco, 153)
relacionar(grafo, huatulco, puertoescondido, 106)
relacionar(grafo, oaxaca, puebla, 342)
relacionar(grafo, villahermosa, cardenas, 49)
relacionar(grafo, villahermosa, ciudaddelcarmen, 170)
relacionar(grafo, ciudaddelcarmen, campeche, 206)
relacionar(grafo, campeche, merida, 174)
relacionar(grafo, merida, cancun, 310)
relacionar(grafo, cancun, playadelcarmen, 68)
relacionar(grafo, playadelcarmen, chetumal, 328)
relacionar(grafo, campeche, chetumal, 272)
relacionar(grafo, cardenas, coatzacoalcos, 128)
relacionar(grafo, coatzacoalcos, minatitlan, 22)
relacionar(grafo, minatitlan, acayucan, 52)
relacionar(grafo, acayucan, cordoba, 251)
relacionar(grafo, acayucan, juchitan, 206)
relacionar(grafo, cordoba, orizaba, 26)
relacionar(grafo, orizaba, puebla, 149)
relacionar(grafo, puebla, ciudaddemexico, 124)
relacionar(grafo, acayucan, veracruz, 255)
relacionar(grafo, veracruz, xalapa, 102)
relacionar(grafo, veracruz, pozarica, 249)
relacionar(grafo, pozarica, tuxpan, 52)
relacionar(grafo, tuxpan, tampico, 180)
relacionar(grafo, tampico, matamoros, 508)
relacionar(grafo, matamoros, reynosa, 86)


print "Mejor ruta encontrada:"
print  caminoMinimo(grafo,salinacruz,reynosa)

#calculando los kilometros del reccrrido mediante un ciclo

camino = caminoMinimo(grafo,salinacruz, reynosa)
kilometros = 0
ciudadactual = ""
ciudaddestino = ""

for i in range(0,camino.__len__()-1):
    if i == 0:
        ciudadactual = camino.pop()
        ciudaddestino = camino.pop()
        kilometros = kilometros + peso(grafo,ciudadactual,ciudaddestino)
    else:
        ciudadactual = ciudaddestino
        ciudaddestino = camino.pop()
        kilometros = kilometros + peso(grafo, ciudadactual, ciudaddestino)

print "Kilometros:"
print kilometros