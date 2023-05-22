import numpy as np
import pandas as pd

if __name__ == "__main__":
    df=pd.DataFrame([[1000,25],[280,120],[900,30]],index=['store1','store2','store3'],columns=['price','num'])

    print(df)
  

    df['total price']=df['price']*df['num']

    print(df)
    
    df1=df.sort_values(by="total price",ascending=False)

    print(df1.head(2))

