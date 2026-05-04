import pandas as pd

data={

    "cal":[120,180,220],
    "dur":[90,80,200]
}

name={"car":"bmw","bike":"hero"}

df =pd.Series(name)

new_df=pd.DataFrame(data)



print(df)
print(new_df['cal'])

