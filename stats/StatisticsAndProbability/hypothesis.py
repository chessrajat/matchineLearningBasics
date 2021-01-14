from scipy.stats import chi2_contingency
from scipy.stats import chi2
table =[[30, 10], [15, 25], [15, 5]]
stat,p,dof,expected = chi2_contingency(table)
prob = 0.95
critical = chi2.ppf(prob, dof)
if abs(stat) >= critical:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')