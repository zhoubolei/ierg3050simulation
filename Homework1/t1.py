import matplotlib.pyplot as plt
import numpy as np

lambdax = 0.05
mux = 0.10
dt = 0.01
tend = 50

lambda_dt = lambdax * dt
mu_dt = mux * dt
step = int(tend / dt)
Lsim = 1000

time = np.arange(0, tend, dt)
assert len(time) == step

def bo_generator(p):
    return np.random.rand(1) < (p)


slist = np.zeros((Lsim, step))
for j in range(Lsim):
    state = False
    for i in range(step):
        if state or bo_generator(lambda_dt):
            slist[j][i] = 1
            state =  not bo_generator(mu_dt)
meanb = slist.mean(axis=0)
plt.plot(time, meanb)
plt.plot(time, 1-meanb)
plt.show()
