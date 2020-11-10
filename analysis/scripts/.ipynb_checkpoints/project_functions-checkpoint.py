{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "URL = r\"C:\\Users\\Owen Harris\\Documents\\DATA 301\\Project\\course-project-group_6012\\data\\raw\\UniversitiesDataSet.csv\" #change URL depending on your file setup\n",
    "\n",
    "def load_and_process(URL):\n",
    "    \n",
    "    df = pd.read_csv(URL)\n",
    "    df = df.iloc[200:,].reset_index(drop=True) #removing data from 2012 and 2013 - aka first 200 rows#\n",
    "    score_sum_2014 = df[df['year']==2014]['score'].sum()\n",
    "    score_sum_2015 = df[df['year']==2015]['score'].sum()\n",
    "    df[\"Score - Avg\"] = df[\"score\"] #create new column\n",
    "    for i in range(len(df)): #editing score - avg column\n",
    "        if df.iloc[i,13] == \"2014\":\n",
    "            df.iloc[i,14] = df.iloc[i,12] - (score_sum_2014/1000)\n",
    "        else:\n",
    "            df.iloc[i,14] = df.iloc[i,12] - (score_sum_2015/1000)\n",
    "    def highlight_cols(x): #highlighting important columns\n",
    "        df = x.copy() # copy new df \n",
    "        df.loc[:, :] = 'background-color: white'  # change background to white\n",
    "        df[['world_rank', 'alumni_employment']] = 'background-color: yellow' # change world rank and alumni employment column to yellow\n",
    "        return df  # return new df\n",
    "    display(df.style.apply(highlight_cols, axis = None))\n",
    "    \n",
    "load_and_process(URL) #calling function"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
