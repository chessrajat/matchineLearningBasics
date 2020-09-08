import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import anova

icecream = sm.datasets.get_rdataset("Icecream","Ecdat").data

#model
model1 = smf.ols("cons ~ temp",icecream).fit()
# print(anova.anova_lm(model1))





