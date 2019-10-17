import matplotlib.pyplot as plt
import numpy as np

lambdax = 0.05
mux = 0.10
dt = 0.01
tend = 50

lambda_inv = 1/lambdax
mu_inv = 1/ mux
step = int(tend / dt)
Lsim = 10000 

time = np.arange(0, tend, dt)
assert len(time) == step

def expo(p):
    return -p*np.log(np.random.rand(1))


slist = np.zeros((Lsim, step))
for j in range(Lsim):
    i = 0
    while i < step:
        interval = int(np.round(expo(lambda_inv)/dt))
        step_n = i + interval
        # print(i, step_n)
        if step_n > step:
            break
        i = step_n
        bt = int(np.round(expo((mu_inv)/dt)))
        step_n = min(i+bt, step)
        slist[j, i:step_n+1] = True
        i = step_n + 1


meanb = slist.mean(axis=0)
plt.plot(time, meanb)
plt.plot(time, 1-meanb)
plt.show()
import ipdb
ipdb.set_trace()
