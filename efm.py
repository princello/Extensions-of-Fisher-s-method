import numpy as np
from scipy.stats import chi2

class model:
	def __init__(self, pvalues, weights, pccs):
		self.pvalues = pvalues
		self.weights = weights
		self.pccs = pccs

	def depwei(self):
		pcc = np.array(self.pccs)
		wei = np.array(self.weights)
		n = len(wei)

		p_tilde = pcc*(1+(1-pcc*pcc)/(2*n-1.0))
		cov = 3.263119*p_tilde + 0.709866 * p_tilde**2 + 0.026589 * p_tilde**3 -(0.709866/n) * np.square(1 - p_tilde**2)

		# initial r_hat
		r_hat = 1.0*sum(wei**2)/sum(wei)

		# residual r_hat
		for k in range(n):
			for l in range(k):
				r_hat += 1.0*cov[k][l]*wei[k]*wei[l]/(2*sum(wei))

		v_hat = 2*sum(wei)/r_hat

		x = np.sum(np.log(np.array(self.pvalues)) * wei * -2)

		return (1- chi2.cdf(x, v_hat,scale=r_hat))

	def dep(self):
		pcc = np.array(self.pccs)
		n = len(pcc)
		wei = np.ones(n)

		p_tilde = pcc*(1+(1-pcc*pcc)/(2*n-1.0))
		cov = 3.263119*p_tilde + 0.709866 * p_tilde**2 + 0.026589 * p_tilde**3 -(0.709866/n) * np.square(1 - p_tilde**2)

		# initial r_hat
		r_hat = 1.0*sum(wei**2)/sum(wei)

		# residual r_hat
		for k in range(n):
			for l in range(k):
				r_hat += 1.0*cov[k][l]*wei[k]*wei[l]/(2*sum(wei))

		v_hat = 2*sum(wei)/r_hat

		x = np.sum(np.log(np.array(self.pvalues)) * wei * -2)

		return (1- chi2.cdf(x, v_hat,scale=r_hat))

	def wei(self):
		wei = np.array(self.weights)
		n = len(wei)

		r_hat = 1.0*sum(wei**2)/sum(wei)

		v_hat = 2*sum(wei)/r_hat

		x = np.sum(np.log(np.array(self.pvalues)) * wei * -2)

		return (1- chi2.cdf(x, v_hat,scale=r_hat))

	def org(self):
		n = len(self.pvalues)

		r_hat = 1.0

		v_hat = 2*n/r_hat

		x = np.sum(np.log(np.array(self.pvalues)) * -2)

		return (1- chi2.cdf(x, v_hat,scale=r_hat))
