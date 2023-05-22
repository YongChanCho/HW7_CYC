import pandas as pd
import numpy as np
if __name__ == '__main__':
    import pandas as pd
    import numpy as np

    data = pd.read_csv('gender2.csv', encoding='ANSI',index_col=0)
    df = pd.DataFrame(data)
    df=df.loc[:,["2022년_계_총인구수","2022년_남_총인구수","2022년_여_총인구수"]]
    df.rename(columns= {"2022년_계_총인구수":"Total", "2022년_남_총인구수":"Male", "2022년_여_총인구수":"Female"}, inplace= True)
    print(df)