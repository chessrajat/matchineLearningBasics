import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# awards_df = pd.read_csv("https://stats.idre.ucla.edu/stat/data/poisson_sim.csv")
# poission_model = smf.poisson("num_awards ~ math + C(prog)",data=awards_df)
# model_result = poission_model.fit()
# print(model_result.summary())

insurance_data = sm.datasets.get_rdataset("Insurance",package="MASS").data
poission_model = smf.poisson("Claims ~ np.log(Holders)",data=insurance_data)
model_result = poission_model.fit()
print(model_result.resid)