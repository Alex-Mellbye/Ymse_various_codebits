
# Her er kode for hvordan vi kan matche en DF mot en 'katalog' (teknisk sett annen DF)
# DF'en 'katalog' er allerede laget
# Først lager vi dict_kat som slår sammen (zip) to av variablene i katalog, deretter putter vi den i en dict for å gjøre det til en dictionary
# Deretter bruker vi .map() hvor vi matcher den første variabelen i zip (var1) som nøkkel med en variabel (var) i datasettet, og dermed får ny_var verdien til den andre variabelen i zip (var2)

dict_grov = dict(zip(katalog["var1"], katalog["var2"]))
df["ny_var"] = df["var"].map(dict_grov)



