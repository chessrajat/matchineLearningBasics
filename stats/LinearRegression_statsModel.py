import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

ice_cream = sm.datasets.get_rdataset("Icecream","Ecdat")
ice_cream_data = ice_cream.data

# got the data now look at the choosing the model
# linear model consuption with price and temperature

# linear_model1 = smf.ols('cons ~ price + temp',ice_cream_data)
# linear_result1 = linear_model1.fit()
# print(linear_result1.summary())

# analysing the results
# The R-squared value of 0.633 suggests that model is not a proper fit.
# The probability value of coefficient price is high, i.e., 0.141. This accepts the null-hypothesis:
# the value of price coefficient is equal to zero.
# Hence, the variable price does not affect cons variable.

# Now lets recreate the model with different variables

# linear_model2 = smf.ols('cons ~ income + temp', ice_cream_data)
# linear_result2 = linear_model2.fit()
# print(linear_result2.summary())


# linear_model3 = smf.ols('cons ~ -1 + income + temp', ice_cream_data)
# linear_result3 = linear_model3.fit()
# print(linear_result3.summary())

# handson

cars_data = sm.datasets.get_rdataset("mtcars")
cars_data = cars_data.data

linear_model4 = smf.ols("wt ~ mpg",cars_data)
linear_result4 = linear_model4.fit()
# print(linear_result4.rsquared)

# these are patsy formulas
linear_model5 = smf.ols("np.log(wt) ~ np.log(mpg)",cars_data)
linear_result5 = linear_model5.fit()
print(linear_result5.rsquared)