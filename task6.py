# import os

# os.makedirs('Example', exist_ok=True)

# os.makedirs('Example/subdirect', exist_ok=True)

# sekil = r'C:\Users\PC\Downloads\stol.jpg'

# sekil_at = 'Example/subdirect/stol.jpg'
# if os.path.exists(sekil):
#     os.rename(sekil, sekil_at)
# else:
#     print(f"Şəkil faylı tapılmadı: {sekil}")

# text = 'Example/subdirect/file.txt'
# with open(text, 'w', encoding='utf-8') as f:
#     f.write('re;sgnkjfodiuafbniuorh')

# for txt in os.listdir('Example/subdirect'):
#     if txt.endswith('.txt'):
#         faylyeri = os.path.join('Example/subdirect', txt)
#         faylgon = os.path.join('Example', txt)
#         os.rename(faylyeri, faylgon)



# Alqoritmik task

# Bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. Biz isə onların 
# topladığı xallara görə neçənci yeri tutduğunu print etməliyik. Misal üçün bizə xallar
#  verilib. xallar = [5,3,4,2,1].
# Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. 
# yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
# Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş 
# sıraya uyğun sıralanacaq və nəticə  düzgün olmayacaq. (taskı daha da asanlaşdırmaq 
# üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)
# Verilmiş xallara uyğun tutduğu yerləri gətirən bir funksiya yazın.


def tutulanyer(xallar):
    sirali_xallar = sorted(enumerate(xallar), key=lambda x: x[1], reverse=True)
    
    yerler = [''] * len(xallar)
    for yer, (indeks, xal) in enumerate(sirali_xallar, start=1):
        yerler[indeks] = "{}-ci yer".format(yer) 
    return yerler

xallar = [5, 2,1,4,3]
yerler = tutulanyer(xallar)
print(yerler)
