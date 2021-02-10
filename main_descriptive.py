import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

local_path = os.getcwd()

df_raw = pd.read_csv(os.path.join(local_path, r"data/country_vaccinations.csv"))

# The main subject of this study is the total vaccination number so any NaN value is not acceptable

df_clean = df_raw.drop(df_raw[df_raw.total_vaccinations.isna()].index)
df_clean = df_clean.drop(df_clean[df_raw.people_vaccinated.isna()].index)

# Overall loockup to correlation matrix and heatmap

def correlation():
    corr = df_clean.corr()
    heatmap = plt.figure(figsize=(17, 17))
    sns.heatmap(corr, annot=True, square=True)
    heatmap.savefig('temp.png', dpi=heatmap.dpi)

    # We can see in the dataset that the total vaccination number and peopple vaccinated number are very similar and close, showing a high correlate in the total vaccination number
    # correlate matrix. First of all we must be sure that the distributions of this columns are the same

    MW_results = [stats.mannwhitneyu(df_clean.total_vaccinations, df_clean.people_vaccinated, alternative="two-sided"), stats.mannwhitneyu(df_clean.total_vaccinations_per_hundred, df_clean.people_vaccinated_per_hundred, alternative="two-sided")]
    
    # Mann-W

if __name__ == "__main__":
    correlation()
