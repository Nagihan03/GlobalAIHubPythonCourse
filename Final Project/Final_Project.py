#Write a knowledge competition program.
#It should consist of 10 questions in total.
#Each question will have only one answer.
#Adjust the answers of the questions according to case sensivity.
#Each question should be worth 10 points.
#If User answers 5 or fewer questions, it will be considered unsuccessful.
#If the user answers more than 5 questions correctly, it will be considered successful.

questions = {"Türkiye'nin en büyük yüz ölçümlü şehrinin adı nedir":"konya",
             "Üzümlü kek atom modelinin sahibi kimdir":"thomson",
             "Ülkemizdeki doğalgaz yatağını bulan sondaj gemisinin adı nedir?":"fatih",
             "Atom İçi dolu bir küredir diyen kimyacı kimdir?":"dalton",
             "Milli mücadele döneminde Fransızlarla imzalanan antlaşmanın adı nedir":"ankara",
             "Sıcaklık artarsa basınçta artar diyen ilk bilim insanı kimdir?":"charles",
             "Klor gazını sıvılaştırmayı başaran ilk kimyacı kimdir?":"faraday",
             "Güney Kore hangi yarım kürededir?":"kuzey",
             "Powerpuff çizgi filminin başrolü olan kızlardan mavi renkli olanın adı nedir?":"Bubbles",
             "Çekirdekli atom modelinden bahseden ilk kimyacı kimdir":"rutherford"}

scors = 0

for i,j in questions.items():
    print(i)
    answer = input()
    if (j == answer.lower()):
        print("\nTebrikler! 10 puan kazandınız!\n")
        scors += 10
    else:
        print(f'\nÜzgünüm! Doğru cevap {j.title()} olacaktı.\n')
    
if(scors > 50):
    print(f'\nYarışmayı başarıyla tamamladınız. Toplam {scors} puan kazandınız!')
else:
    print(f'\nYarışmayı başarıyla tamamlayamadınız. Toplam {scors} puan kazandınız!')
