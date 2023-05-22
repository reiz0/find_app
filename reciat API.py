from PIL import Image
import pyocr

picture=Image.open(input())

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 対応言語取得
langs = engine.get_available_languages()
print("対応言語:",langs) # ['eng', 'jpn', 'osd']

# 画像の文字を読み込む
txt = engine.image_to_string(picture, lang="jpn") # 修正点：lang="eng" -> lang="jpn"

txt = txt.splitlines()


import re #正規表現を扱う
import time #時間の測定や処理に関する関数を扱う
from datetime import datetime #日付を扱う


l_date = [s for s in txt if re.match('(.*[0-9]{4}(年|/|-).*[0-9]{1,2}(月|/|-).*[0-9]{1,2}(日|).*)', s)]
#数字と年月日、もしくは-、/が並んだ時にl_dateとして抽出
l_func = [s for s in txt if re.match('([^a-zA-Zぁ-んァ-ン\u4E00-\u9FD0]*[ぁ-んァ-ン\u4E00-\u9FD0]+.*[0-9]+[^ぁ-んァ-ン\u4E00-\u9FD0]?$)', s)]
#記号か数字から始まってもいいが、日本語の文字列があり、最後が数字(記号が最後についている場合も含む)で終わる文字列をl-funcとして抽出

ele_date = l_date[0]
l_func.remove(ele_date)

sum_func = [s for s in l_func if re.match('.*(合|計).*', s)]
for i in sum_func:
    if i in l_func:
        l_func.remove(i)

rem_func = [s for s in l_func if re.match('.*(小計|内税|支払|番号|外税|クレジット|釣り|金額|ポイント|残高|期限|取引).*', s)]
#l_funcから小計、内税、支払いなど購買項目に関係のない削除すべきものを抽出
for i in rem_func:
    if i in l_func:
        l_func.remove(i)



main_func = []
main_func.extend(l_func)#main_funcにl_funcの要素を全て追加

main_disc = [s for s in l_func if re.match('.*((割引|値引).*|-[0-9]+.?)', s)]
#l_funcの内容から割引の記述があるものを全て抽出

for i in main_disc:
    if i in main_func:
        main_func.remove(i)


# print(ele_date)#レシートの日付
# print(l_func)#レシートの購買項目と値段、割引のリスト
# print(main_disc)#割引のリスト
# print(main_func)#購買項目と値段


repl_func = []
for i in main_func:
    repl_func.append(re.sub('[^0-9a-zA-Zぁ-んァ-ン\u4E00-\u9FD0]+', '', i) )
    

dob_ele_thing = []
for i in repl_func:
    dob_ele_thing.append(re.findall('[a-zA-Zぁ-んァ-ン\u4E00-\u9FD0].*[a-zA-Zぁ-んァ-ン\u4E00-\u9FD0]', i))
ele_thing = [x for row in dob_ele_thing for x in row]


print(ele_thing)#購買項目のリスト


l_ele_plic = []
for i in l_func:
    # i[::-1]で順番並べ替え
    # findall(...)[0]でマッチしたものの一番初めのものを取り出す
    # 取り出したものを[::-1]で反転させて元に戻す
    l_ele_plic.append(int(re.findall('\d+-|\d+', i[::-1])[0][::-1]))

ele_plic = []
for i in l_ele_plic:
    if i >= 0:
        ele_plic.append(i)
    else:
        ele_plic[-1] += i

print(ele_plic)#割引適用後の実際に支払った値段のリスト