import math

N  = [150, 165]
mu = [0.299, 0.307]
sigma_square = [0.05, 0.08]

sig2_over_N = lambda x: sigma_square[x]/N[x]

t  = (mu[0]-mu[1])/math.sqrt(sig2_over_N(0) + sig2_over_N(1))

nu = (sig2_over_N(0) + sig2_over_N(1))**2 / (sig2_over_N(0)**2/(N[0]-1) + sig2_over_N(1)**2/(N[1]-1))

print "t  =", t
print "nu =", nu