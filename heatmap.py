import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch
import seaborn as sns
import pandas as pd

df = pd.read_csv('data.csv')

df['x'] = (df['x']/476)*80
df['y'] = (df['y']/720)*120

fig, ax = plt.subplots(figsize=(4, 6))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='white', stripe=False)
pitch.draw(ax=ax)
plt.gca().invert_yaxis()

kde = sns.kdeplot(
        df['x'],
        df['y'],
        shade = True,
        shade_lowest=False,
        alpha=.7,
        n_levels=20,
        cmap = 'magma'
)



#use a for loop to plot each pass
# for x in range(len(df['x'])):
#     plt.scatter(df['x'][x],df['y'][x],color='green')
        
# plt.xlim(0,120)
# plt.ylim(0,80)

plt.title('Heatmap Table Soccer', color='white', size=20)
plt.show()

