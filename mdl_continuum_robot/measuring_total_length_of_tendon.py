import numpy as np
import matplotlib.pyplot as plt

orientation_EE = np.linspace(-np.pi, np.pi, 500)
l0 = 25
d = 25/2
p = 16
num_of_section = 4

theta = orientation_EE / num_of_section

total_length = lambda theta: (2 * l0 + 4 * d * np.cos(theta / 2)) * num_of_section
delta_l = lambda theta: p * np.sin(theta)
l1 = lambda theta: 2 * (d * np.cos(theta / 2) + p * np.sin(theta / 2))
l2 = lambda theta: 2 * (d * np.cos(theta / 2) - p * np.sin(theta / 2))

tendon1 = lambda theta: (l1(theta) + l0) * num_of_section
tendon2 = lambda theta: (l2(theta) + l0) * num_of_section
total_confirm = lambda theta: tendon1(theta) + tendon2(theta)

fig, axs = plt.subplots(2, 3, figsize=(12, 8))

# ----------------------------
# 1) Total length of tendons
# ----------------------------
axs[0, 0].plot(orientation_EE, total_length(theta), color='k', linestyle='-', linewidth=1.5, label='Total Length')
axs[0, 0].grid()
axs[0, 0].set_xlabel('orientation_EE (radians)')
axs[0, 0].set_ylabel('total_length(mm)')
axs[0, 0].set_title('Total Length of Tendons')
axs[0, 0].legend()

# x축을 -π부터 π까지 동일 간격으로 설정
axs[0, 0].set_xticks([-np.pi, -3*np.pi/4, -np.pi/2, -np.pi/4, 
                      0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
axs[0, 0].set_xticklabels([r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$', 
                           r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', 
                           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])

# ----------------------------
# 2) Confirmation of total length
# ----------------------------
axs[0, 1].plot(orientation_EE, total_confirm(theta), color='k', linestyle='-', linewidth=1.5, label='Tendon1 + Tendon2')
axs[0, 1].grid()
axs[0, 1].set_xlabel('orientation_EE (radians)')
axs[0, 1].set_ylabel('(tendon1 + tendon2)(mm)')
axs[0, 1].set_title('Confirmation of Total Length')
axs[0, 1].legend()

axs[0, 1].set_xticks([-np.pi, -3*np.pi/4, -np.pi/2, -np.pi/4, 
                      0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
axs[0, 1].set_xticklabels([r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$', 
                           r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', 
                           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])

# ----------------------------
# 3) Tendon1 and Tendon2 lengths
# ----------------------------
axs[1, 0].plot(orientation_EE, tendon1(theta), label='Tendon1 (Left)', linestyle='-', linewidth=1.5)
axs[1, 0].plot(orientation_EE, tendon2(theta), label='Tendon2 (Right)', linestyle='-', linewidth=1.5)
axs[1, 0].grid()
axs[1, 0].set_xlabel('orientation_EE (radians)')
axs[1, 0].set_ylabel('Tendon Lengths(mm)')
axs[1, 0].set_title('Tendon1 & Tendon2 Lengths')
axs[1, 0].legend()

axs[1, 0].set_xticks([-np.pi, -3*np.pi/4, -np.pi/2, -np.pi/4, 
                      0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
axs[1, 0].set_xticklabels([r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$', 
                           r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', 
                           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])

# ----------------------------
# 4) Tendon components l1 and l2
# ----------------------------
axs[1, 1].plot(orientation_EE, l1(theta), label='l1 (Left)', linestyle='-', linewidth=1.5)
axs[1, 1].plot(orientation_EE, l2(theta), label='l2 (Right)', linestyle='-', linewidth=1.5)
axs[1, 1].grid()
axs[1, 1].set_xlabel('orientation_EE (radians)')
axs[1, 1].set_ylabel('l1 & l2 Length(mm)')
axs[1, 1].set_title('l1 & l2')
axs[1, 1].legend()

axs[1, 1].set_xticks([-np.pi, -3*np.pi/4, -np.pi/2, -np.pi/4, 
                      0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
axs[1, 1].set_xticklabels([r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$', 
                           r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', 
                           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])

# ----------------------------
# 5) Orientation EE plot
# ----------------------------
axs[0, 2].plot(orientation_EE, orientation_EE / 4, linestyle='-', linewidth=1.5, label='Orientation End Effector')
axs[0, 2].grid()
axs[0, 2].set_xlabel('orientation_EE (radians)')
axs[0, 2].set_ylabel('orientation_EE (radians)')
axs[0, 2].set_title('Orientation End Effector')
axs[0, 2].legend()

# x축
axs[0, 2].set_xticks([-np.pi, -3*np.pi/4, -np.pi/2, -np.pi/4, 
                      0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
axs[0, 2].set_xticklabels([r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$', 
                           r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', 
                           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])

# y축도 동일하게 -π부터 π까지 설정 (예시)
axs[0, 2].set_yticks([-np.pi, -3*np.pi/4, -np.pi/2, -np.pi/4, 
                      0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
axs[0, 2].set_yticklabels([r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$', 
                           r'$\frac{-\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', 
                           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])

print("total_length(105 deg) :", total_length(np.pi / 180 * 105 / 4))
print("tendon1(105 deg)      :", tendon1(np.pi / 180 * 105 / 4))
print("tendon2(105 deg)      :", tendon2(np.pi / 180 * 105 / 4))

plt.tight_layout()
plt.show()
