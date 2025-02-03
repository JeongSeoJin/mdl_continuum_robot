import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

l0 = 25
d = 25 / 2
p = 16
n = 4

def tl(zeta, psi):
    return 4 * d * (np.cos(zeta / (2 * n)) + np.cos(psi / (2 * n))) * n

def tendon1(zeta, psi):
    return (2 * d * np.cos(zeta/ (2 * n)) + 2 * d * np.cos(psi/(2 * n)) + 2 * p * np.sin(psi/(2 * n))) * n

def tendon2(zeta, psi):
    return (2 * d * np.cos(zeta/ (2 * n)) + 2 * d * np.cos(psi/(2 * n)) - 2 * p * np.sin(psi/(2 * n))) * n

def tendon3(zeta, psi):
    return (2 * d * np.cos(psi/ (2 * n)) + 2 * d * np.cos(zeta/(2 * n)) + 2 * p * np.sin(zeta/(2 * n))) * n

def tendon4(zeta, psi):
    return (2 * d * np.cos(psi/ (2 * n)) + 2 * d * np.cos(zeta/(2 * n)) - 2 * p * np.sin(zeta/(2 * n))) * n

zeta = np.linspace(-np.pi * 105/180, np.pi * 105/180, 500)
psi = np.linspace(-np.pi * 105/180, np.pi * 105/180, 500)
ZETA, PSI = np.meshgrid(zeta, psi)

TL = tl(ZETA, PSI)
TENDON1 = tendon1(ZETA, PSI)
TENDON2 = tendon2(ZETA, PSI)
TENDON3 = tendon3(ZETA, PSI)
TENDON4 = tendon4(ZETA, PSI)

def pi_formatter(x, pos):
    """
    x : 축의 실제 값 (float)
    pos : tick 위치 (사용하지 않음)
    출력 문자열 예: -0.5π, 0π, 1.5π 등
    """
    # π 배수를 계산
    value_in_pi = x / np.pi
    return f"{value_in_pi:.1f}π"

fig = plt.figure(figsize=(15, 10))

# ----- 1번 플롯 (total length) -----
ax1 = fig.add_subplot(2, 3, 1, projection='3d')
surf1 = ax1.plot_surface(ZETA, PSI, TL, cmap='viridis')
ax1.set_title('total length')

# X, Y축을 라디안(pi 단위)으로 표기
ax1.set_xlabel(r'$\zeta$ (rad)')
ax1.set_ylabel(r'$\psi$ (rad)')
ax1.set_zlabel('total length')

ax1.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

# ----- (tendon1) -----
ax2 = fig.add_subplot(2, 3, 2, projection='3d')
surf2 = ax2.plot_surface(ZETA, PSI, TENDON1, cmap='plasma')
ax2.set_title('tendon1')
ax2.set_xlabel(r'$\zeta$ (rad)')
ax2.set_ylabel(r'$\psi$ (rad)')
ax2.set_zlabel('tendon1')

ax2.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax2.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

# ----- (tendon2) -----
ax3 = fig.add_subplot(2, 3, 3, projection='3d')
surf3 = ax3.plot_surface(ZETA, PSI, TENDON2, cmap='plasma')
ax3.set_title('tendon2')
ax3.set_xlabel(r'$\zeta$ (rad)')
ax3.set_ylabel(r'$\psi$ (rad)')
ax3.set_zlabel('tendon2')

ax3.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax3.yaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax3.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))
ax3.yaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

fig.colorbar(surf3, ax=ax3, shrink=0.5, aspect=5)

# ----- (tendon3) -----
ax4 = fig.add_subplot(2, 3, 4, projection='3d')
surf4 = ax4.plot_surface(ZETA, PSI, TENDON3, cmap='plasma')
ax4.set_title('tendon3')
ax4.set_xlabel(r'$\zeta$ (rad)')
ax4.set_ylabel(r'$\psi$ (rad)')
ax4.set_zlabel('tendon3')

ax4.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax4.yaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax4.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))
ax4.yaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

fig.colorbar(surf4, ax=ax4, shrink=0.5, aspect=5)

# ----- (tendon4) -----
ax5 = fig.add_subplot(2, 3, 5, projection='3d')
surf5 = ax5.plot_surface(ZETA, PSI, TENDON4, cmap='plasma')
ax5.set_title('tendon4')
ax5.set_xlabel(r'$\zeta$ (rad)')
ax5.set_ylabel(r'$\psi$ (rad)')
ax5.set_zlabel('tendon4')

ax5.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax5.yaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax5.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))
ax5.yaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

fig.colorbar(surf5, ax=ax5, shrink=0.5, aspect=5)


ax6 = fig.add_subplot(2, 3, 6, projection='3d')
surf6 = ax6.plot_surface(ZETA, PSI, TENDON1 + TENDON2, cmap='viridis')
ax6.set_title('tendon1 + tendon2')
ax6.set_xlabel(r'$\zeta$ (rad)')
ax6.set_ylabel(r'$\psi$ (rad)')
ax6.set_zlabel('tendon1 + tendon2')

ax6.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax6.yaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax6.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))
ax6.yaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

fig.colorbar(surf6, ax=ax6, shrink=0.5, aspect=5)

plt.tight_layout()
plt.show()
