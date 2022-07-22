import random

line_a={'あ':'a','い':'i','う':'u','え':'e','お':'o','ア':'a','イ':'i','ウ':'u','エ':'e','オ':'o',
'か':'ka','き':'ki','く':'ku','け':'ke','こ':'ko','カ':'ka','キ':'ki','ク':'ku','ケ':'ke','コ':'ko',
'さ':'sa','し':'si','す':'su','せ':'se','そ':'so','サ':'sa','シ':'si','ス':'su','セ':'se','ソ':'so',
'た':'ta','ち':'ti','つ':'tu','て':'te','と':'to','タ':'ta','チ':'ti','ツ':'tu','テ':'te','ト':'to',
'な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no',
'は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho',
'ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','マ':'ma','ミ':'mi','ム':'mu','メ':'me','モ':'mo',
'や':'ya','ゆ':'yu','よ':'yo','ヤ':'ya','ユ':'yu','ヨ':'yo',
'ら':'ra','り':'ri','る':'ru','れ':'re','ろ':'ro','ラ':'ra','リ':'ri','ル':'ru','レ':'re','ロ':'ro',
'わ':'wa','を':'wo','ワ':'wa','ヲ':'wo'}

def guess_word(line_x):
    for i in range(6):
        ping_jia_ming_list=list(line_x.values())
        ping_jia_ming=random.choice(ping_jia_ming_list)
        print(ping_jia_ming)

guess_word(line_a)