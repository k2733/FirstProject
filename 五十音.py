import time
import random
line=input("【亲爱的旅行者，请问您要复习哪一行？\n或输入all开启整体复习。】\n请输入：")
print()
 
def guess_word(line_x):
    for i in range(30):
        ping_jia_ming_list=list(line_x.keys())
        ping_jia_ming=random.choice(ping_jia_ming_list)
        print(ping_jia_ming)
        luo_ma_yin=input()
        print
        if luo_ma_yin=='quit':
            break
        while luo_ma_yin!=line_x[ping_jia_ming]:
            print('【错误！再试一遍：】')
            luo_ma_yin=input()
        else:
            print('【正确！下一个：】')
            print()
        time.sleep(0.5)
    print("【明天记得也要来背单词O(∩_∩)O!】")
    
def dict_combine(dic1,dic2):
    for k in dic2.keys():
        dic1[k]=dic2[k]
 
line_a={'あ':'a','い':'i','う':'u','え':'e','お':'o','ア':'a','イ':'i','ウ':'u','エ':'e','オ':'o'}
line_ka={'か':'ka','き':'ki','く':'ku','け':'ke','こ':'ko','カ':'ka','キ':'ki','ク':'ku','ケ':'ke','コ':'ko'}
line_sa={'さ':'sa','し':'si','す':'su','せ':'se','そ':'so','サ':'sa','シ':'si','ス':'su','セ':'se','ソ':'so'}
line_ta={'た':'ta','ち':'ti','つ':'tu','て':'te','と':'to','タ':'ta','チ':'ti','ツ':'tu','テ':'te','ト':'to'}
line_na={'な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no'}
line_ha={'は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho'}
line_ma={'ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','マ':'ma','ミ':'mi','ム':'mu','メ':'me','モ':'mo'}
line_ja={'や':'ja','ゆ':'ju','よ':'jo','ヤ':'ja','ユ':'ju','ヨ':'jo'}
line_ra={'ら':'ra','り':'ri','る':'ru','れ':'re','ろ':'ro','ラ':'ra','リ':'ri','ル':'ru','レ':'re','ロ':'ro'}
line_wa={'わ':'wa','を':'wo','ワ':'wa','ヲ':'wo'}
 
line_all={}
dict_combine(line_all,line_a)
dict_combine(line_all,line_ka)
dict_combine(line_all,line_sa)
dict_combine(line_all,line_ta)
dict_combine(line_all,line_na)
dict_combine(line_all,line_ha)
dict_combine(line_all,line_ma)
#dict_combine(line_all,line_ja)
#dict_combine(line_all,line_ra)
#dict_combine(line_all,line_wa)
 
if line=="a":
    guess_word(line_a)
elif line=='ka':
    guess_word(line_ka)
elif line=='sa':
    guess_word(line_sa)
elif line=='ta':
    guess_word(line_ta)
elif line=='na':
    guess_word(line_na)
elif line=='ha':
    guess_word(line_ha)
elif line=='ma':
    guess_word(line_ma)
elif line=='ja':
    guess_word(line_ja)
elif line=='ma':
    guess_word(line_ra)
elif line=='wa':
    guess_word(line_wa)
elif line=='all':
    guess_word(line_all)
elif line=='quit':
    print("【明天记得也要来背单词O(∩_∩)O!】")
