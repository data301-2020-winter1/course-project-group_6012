import pandas as pd 
def load_and_process(URL):
    
    df = pd.read_csv(URL)
    df = df.iloc[200:,].reset_index(drop=True) #removing data from 2012 and 2013 - aka first 200 rows#
    score_sum_2014 = df[df['year']==2014]['score'].sum()
    score_sum_2015 = df[df['year']==2015]['score'].sum()
    df["Score - Avg"] = df["score"] #create new column
    for i in range(len(df)): #editing score - avg column
        if df.iloc[i,13] == "2014":
            df.iloc[i,14] = df.iloc[i,12] - (score_sum_2014/1000)
        else:
            df.iloc[i,14] = df.iloc[i,12] - (score_sum_2015/1000)
    def highlight_cols(x): #highlighting important columns
        df = x.copy() # copy new df 
        df.loc[:, :] = 'background-color: white'  # change background to white
        df[['world_rank', 'alumni_employment']] = 'background-color: yellow' # change world rank and alumni employment column to yellow
        return df  # return new df
    display(df.style.apply(highlight_cols, axis = None))
