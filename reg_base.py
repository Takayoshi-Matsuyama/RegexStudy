import sys
import re

# Pythonインストール場所の確認
print(sys.exec_prefix)
print(sys.executable)

# 正規表現の確認
print(re.findall(r'abc', 'abcdef'))

# ファイルから読み込んでみる
f = open('sample.txt', 'r', encoding='UTF-8')

for line in f:
    print(line, end='')     # end='' --> 改行なし
    print(re.findall(r'^.', line))
    print(re.findall(r'.$', line))

f.close()
