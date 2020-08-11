import numpy as np
import pandas as pd

d = pd.date_range('11-Sep-2017', '17-Sep-2017', freq='2D')
a = len(d[d.isin(pd.to_datetime(['12-09-2017', '15-09-2017']))])
print(pd.bdate_range('11-Sep-2017', '17-Sep-2017', freq='2D'))
print(pd.period_range('11-Sep-2017', '17-Sep-2017', freq='M'))
print(pd.date_range('11-Sep-2017', '17-Sep-2017', freq='2D'))
