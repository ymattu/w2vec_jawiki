# ~/anaconda/bin/python

from gensim.models import word2vec

# コーパス作成
data = word2vec.Text8Corpus('jawiki_abst.txt')

# word2vecで学習
# size      : 出力するベクトルの次元数
# min_count : この数値よりも登場回数が少ない単語は無視する
# window    : 一つの単語に対してこの数値分だけ前後をチェックする
model = word2vec.Word2Vec(data, size=200, min_count=20, window=15)

model.save('jawiki.model')

# 学習後はモデルのロードだけでよい
model = word2vec.Word2Vec.load('jawiki.model')

# コサイン類似度が高い単語
out1 = model.most_similar(positive=['単語'])
for x in out1:
    print(x[0], x[1])


# 単語の足し引き
out2 = model.most_similar(positive=['単語1', '単語2'], negative=['単語3'])
for x in out2:
    print(x[0], x[1])
