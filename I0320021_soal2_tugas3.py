#Dictionary
Dict = {"nama" : "Cristin Angel" ,
        "hobi" : ["membaca", "menyanyi", "menulis"],
        "sosial media" : ["instagram : @cristinangl ", "facebook : Christin Angel"," line : angell51"] ,
        "lagu kesukaan " : ["Selidiki Aku", "Terlanjur Mencinta", "Mungkin Harin ini Esok atau Nanti "],
        "makanan favorit" : ["Nasi goreng", "Bakso", "Gado-Gado", "Mie Pangsit",]
        }
print(f'Biodata angel : {Dict}')
print("")

#Mengubah Data hobi dan media sosial
Dict['hobi'][2] = ('Bermain Organ')
Dict['sosial media'][2] = ('WA : 082312793776')

#Menambah satu data hobi
Dict["hobi"].append("Mendengarkan Lagu")

#Menghapus Dua Makanan Favori
del Dict["makanan favorit"][0:2]
print(f'Data setelah diubah : {Dict}')
