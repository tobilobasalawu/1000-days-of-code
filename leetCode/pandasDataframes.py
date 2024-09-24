import pandas as pd

def createDataframe(student_data):
    df = pd.DataFrame(student_data, columns=['student_id','age'])
    df.set_index(['student_id'], inplace=True)
    print(df)

createDataframe([[1,2],[2,11]])