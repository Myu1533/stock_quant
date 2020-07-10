import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5, 7.5, 1000)
y = np.sin(x)

plt.figure(figsize=(12, 8))
plt.plot(x, y, '--g', lw=2, label='sin(x)')

plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.xticks(np.arange(0, 10, 2), ['2015-07-02', '2015-08-02', '2015-09-02', '2015-10-02', '2015-11-02'], rotation=45)
plt.yticks(np.arange(-1, 1.5, 1), [u'最小值', u'零值', u'最大值'])

plt.grid(True, ls=':', color='r', alpha=0.5)

plt.title(u'Functional Programming')

plt.legend(loc='upper right')

plt.annotate('max sell', xy=(np.pi / 2, 1), xytext=(np.pi/2, 1.3), weight='regular', color='g', fontsize=15, arrowprops={'arrowstyle': '->', 'connectionstyle': 'arc3', 'color': 'g'})
plt.annotate('min buy', xy=(np.pi * 3 / 2, -1), xytext=(np.pi * 3/2, -1.3), weight='regular', color='r', fontsize=15, arrowprops={'arrowstyle': '->', 'connectionstyle': 'arc3', 'color': 'r'})

plt.show()