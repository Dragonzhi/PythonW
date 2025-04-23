import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt # type: ignore

# 创建表格
workout_dict = {
    "calories":[420,380,390,390],
    "duration":[50,40,45,45],
    "type":['run','walk','walk','run']
}
workout = pd.DataFrame(workout_dict)
workout.to_excel(filename, index=False)
