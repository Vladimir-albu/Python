import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
over=np.zeros(len(df['id']), dtype=int)
for i in range(len(df['id'])):
  if (df.iloc[i]['weight'] / (df.loc[i]['height']/100)**2) > 25: over[i]=1

df['overweight'] = over

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

for i in range(len(df.index)):
  if df.loc[i,'cholesterol']==1: df.loc[i,'cholesterol']=0
  else: df.loc[i,'cholesterol']=1
      
  if df.loc[i,'gluc']==1: df.loc[i,'gluc']=0
  else: df.loc[i,'gluc']=1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.reset_index().groupby(['variable', 'cardio', 'value']).count()
    df_cat = df_cat.rename(columns={'index':'Total'})

    # Draw the catplot with 'sns.catplot()'

    sns.catplot(data=df_cat, x='variable', y='Total',col='cardio', kind='bar', hue='value')

    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x="variable", y="Total",col="cardio", kind='bar', hue='value').fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat= df[(df['ap_lo']<=df['ap_hi']) & (df['height']>=df['height'].quantile(0.025)) & (df['height']<=df['height'].quantile(0.975)) & (df['weight']>=df['weight'].quantile(0.025)) & (df['weight']<=df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = 1


    # Set up the matplotlib figure
    fig, ax = plt.figure()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
