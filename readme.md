# 日本語 Wikipedia のデータのダウンロード

このモデルを作った時点でのタイムスタンプは`05-Oct-2016 04:30`である

```fish
cd Desktop/word2vec/

wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-abstract.xml.bz

```

# テキストデータへの変換と Mecab による分かち書き

```fish

gem install wp2txt

# そこそこ時間がかかる
wp2txt --input-file jawiki-latest-pages-articles.xml.bz2

# wp2txt の結果を結合
cat jawiki-latest-pages-articles.xml-* > corpus.txt

# Mecab
mecab -Owakati corpus.txt -o jawiki_abst.txt

# UTF8 に
nkf -w jawiki_abst.txt > jawiki_abst2.txt

```

# Python で解析

使うファイルは `jawiki.py`
