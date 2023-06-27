import matplotlib.pyplot as plt
import numpy as np


# 再帰関数
def recursive_func(x, n):
    if n == 0:
        return 0.4 * x[n]
    else:
        return 0.3 * recursive_func(x, n - 1) + 0.4 * x[n]


# 差分方程式（再帰あり）
def difference_equation_recursive(x):
    N = len(x)
    y = np.zeros(N)

    for n in range(N):
        y[n] = recursive_func(x, n)

    return y


# 確認コード
x = np.zeros(10)
x[0] = 1

y = difference_equation_recursive(x)
np.set_printoptions(suppress=True)

print(y)
# [0.4   0.12   0.036   0.0108    0.00324   0.000972   0.0002916  0.00008748 0.00002624 0.00000787]

plt.stem(y)
plt.show()
