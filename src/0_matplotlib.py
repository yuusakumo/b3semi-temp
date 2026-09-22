import matplotlib.pyplot as plt
import math

# 描画するデータの生成
min_x = 1
max_x = 100
x = [i for i in range(min_x, max_x+1) ]
y1 = [i for i in range(min_x, max_x+1)]                   # y1 = x
y2 = [i*i for i in range(min_x, max_x+1)]                 # y2 = x^2
y3 = [math.exp(i/10) for i in range(min_x, max_x+1)]      # y3 = exp(x/10)

# 描画
n_r = 1    # 行数
n_c = 1    # 列数
fig, axes = plt.subplots(n_r, n_c, tight_layout = True)    # figure オブジェクトの取得

axes.plot(x, y1, '-',  label = 'liner', clip_on=False)      #  (x, y1) の描画
axes.plot(x, y2, '-', label = 'square', clip_on=False)      #  (x, y2) の描画
axes.plot(x, y3, '-', label = 'exponential', clip_on=False) #  (x, y3) の描画

axes.legend()                 #  注釈の作成
axes.set_xlim(min_x, max_x)   #   x 軸の範囲を指定

axes.set_ylabel('$y_1 = x$ or $y_2 = x^2$ or $y_3 = e^{x/10}$')  # y 軸のラベルを描画
axes.set_xlabel('$x$')        #   x 軸のラベルを描画
axes.set_xscale('log')        #   x 軸を対数目盛に変更
axes.set_yscale('log')        #   y 軸を対数目盛に変更

# グラフの保存
fig.savefig("../report/figure/test.png") 
