# Flere forskjellige måter å anvende IF statements på

# Her bruker vi numpy.where hvor vi først gir betingelsen (notna()=True), deretter de to mulighetene "Har sak_id" og "Mangler sak_id"

df2['teller1'] = np.where(df2['sak_id'].notna() == True, "Har sak_id", "Mangler sak_id")
print('Teller1')
print(df2["teller1"].value_counts())


# Her er det flere betingelser som vi baker inn i en funksjon med .apply(). Fordelen med dette er at vi får
# flere forskjellige utfall. Ulempen er at det er mye kode

def sak_rettskr_avgj(row):
    if row['sak_rettskr_avgj'] == "":
        val = 1
    elif row['sak_rettskr_avgj'] == "0":
        val = 1
    elif row['sak_rettskr_avgj'] == "0000":
        val =1
    else:
        val = 0
    return val

df2['teller2'] = df2.apply(sak_rettskr_avgj, axis=1)
print('Teller2')
print(df2["teller2"].value_counts())

# Under bruken vi en .loc() funksjon med flere betingelser. Dette er mer effektiv kode enn med .apply() funksjon, men tilgjengjeld 
# så får vi kun et utfall. 

df2.loc[(df2['sak_rettskr_avgj'] != '') | (df2['sak_rettskr_avgj'] != '0') | (df2['sak_rettskr_avgj'] != '0000'), 'tellerx'] = 1
print('Tellerx')
print(df2["tellerx"].value_counts())

# Her bruker vi .loc() funksjonen for en betingelse. Litt mer effektiv kode enn numpy.where men også bare et utfall.

df2.loc[(df2['sak_rettskr_avgj'] == ''), 'teller_test'] = 1
print('Teller_test')
print(df2["teller_test"].value_counts())
