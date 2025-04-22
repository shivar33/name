import pandas as pd
import numpy as np
exam_data = {'students':["Amy","Ben","Jack","Jill"],'score':[50,86,12,98],'grade':["F","B","F","A"],'passed':["no","yes","no","yes"]}
labels = ["a","b","c","d"]
df = pd.DataFrame(exam_data,index=labels)
print(df)