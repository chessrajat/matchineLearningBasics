import numpy as np
import patsy
import statsmodels.api as sm


# Y = B0 + B1*X1 + B2*X2 + B3*X1*X2.

# y = np.array([1, 2, 3, 4, 5])
# x1 = np.array([6, 7, 8, 9, 10])
# x2 = np.array([11, 12, 13, 14, 15])
# X = np.vstack([np.ones(5), x1, x2, x1*x2]).T
#
# print(y)
# print(X)

# y = np.array([1, 2, 3, 4, 5])
# x1 = np.array([6, 7, 8, 9, 10])
# x2 = np.array([11, 12, 13, 14, 15])
# data = {'y':y, 'x1':x1, 'x2':x2}
#
# y, X = patsy.dmatrices('y ~ 1 + x1 + x2 + x1*x2', data)
#
# print(y)
# print(X)

# bc_cancer_set = sm.datasets.cancer
# #
# # bc_cancer = bc_cancer_set.load()
# #
# # bc_cancer_data = bc_cancer.data
# # print(bc_cancer_data)
# #
# # print(type(bc_cancer_data))

