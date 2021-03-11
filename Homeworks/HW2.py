#CV application
#Create 5 dictionaries. Each dictionary should represent a CV.
#Create a CV containing the information of the 5 created people.
#Print the information on CVs created on the screen.

#Question 1
CV1 = {"Ad":"Ali Mert", "Soyad":"Kocaman", "Yaş":19, "Meslek":"Bilgisayar Mühendisi", "Yetenek&Hobi":["C++","Java","Puzzle","Zula"]}
CV2 = {"Ad":"Nagihan", "Soyad":"Ünal", "Yaş":21, "Meslek":"Kimya Mühendisi", "Yetenek&Hobi":["Autocad","R","Voleybol","NLP"]}
CV3 = {"Ad":"Simay Belen", "Soyad":"Köse", "Yaş":21, "Meslek":"Endüstriye Tasarım", "Yetenek&Hobi":["Pafta Hazırlama", "Tasarlama", "Müzik", "Koşu Yapmak"]}
CV4 = {"Ad":"Berna", "Soyad":"Tugrul", "Yaş":21, "Meslek":"Mimar", "Yetenek&Hobi":["Fusion", "Maket Yapı", "Araştırma Yapmak","Tenis"]}
CV5 = {"Ad":"Aysegül", "Soyad":"Çelik", "Yaş":21, "Meslek":"Makine Mühendisi", "Yetenek&Hobi":["Tasarım-Donanım","Autodesk Programları","Baketbol","Pilates"]}

for i,j in CV1.items():
    print(i, ":", j)
    
print("\n")

for i,j in CV2.items():
    print(i, ":", j)
    
print("\n")

for i,j in CV3.items():
    print(i, ":", j)
    
print("\n")

for i,j in CV4.items():
    print(i, ":", j)
    
print("\n")

for i,j in CV5.items():
    print(i, ":", j)
    
print("\n")  
