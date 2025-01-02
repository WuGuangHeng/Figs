#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

#%%
# Load csv file
import os
import pandas as pd

dataset = 'LPBA40'

if dataset =='LPBA40':
        outstruct = ['Frontal', 'Parietal','Occipital', 'Temporal', 'Cingulate', 'Putamen', 'Hippocampus'] # LPBA
if dataset =='MindBoggle':
        outstruct = ['Frontal', 'Parietal','Occipital', 'Temporal', 'Cingulate'] # MindBoggle
if dataset =='IXI':
     outstruct = ['R-{:02d}'.format(i) for i in range(1, 18)] # IXI
    #  outstruct = ['Brain-Stem', 'Thalamus', 'Cerebellum-Cortex', 'Cerebral-White-Matter', 'Cerebellum-White-Matter', 
    #               'Putamen', 'VentralDC', 'Pallidum', 'Caudate', 'Lateral-Ventricle', 'Hippocampus',
    #               '3rd-Ventricle', '4th-Ventricle', 'Amygdala', 'Cerebral-Cortex', 'CSF', 'choroid-plexus']
outstruct
#%%
files = ['_SyN_BoxPlot.csv',
         '_VoxelMorph_BoxPlot.csv',
         '_TransMorph_BoxPlot.csv',
         '_TransMatch_BoxPlot.csv',
         '_Im2Grid_BoxPlot.csv',
         '_ModeT_BoxPlot.csv',
         '_MambaMorphFeat_BoxPlot.csv',
         '_VMambaMorphFeat_BoxPlot.csv',
        #  '_RDP_BoxPlot.csv',
         '_MambaFuse_BoxPlot.csv',
        ]
files = [dataset + file for file in files]

all_data = []
for file in files:
    data = pd.read_csv(os.path.join('./'+ dataset, file))
    all_data.append(data.values.T)
all_data[0].shape

#%%
def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    for patch in bp['boxes']:
        patch.set(facecolor = color)
    plt.setp(bp['whiskers'], color='cornflowerblue')
    plt.setp(bp['caps'], color='steelblue')
    plt.setp(bp['medians'], color='dodgerblue')

#%%
flierprops = dict(marker='o', markerfacecolor='cornflowerblue', markersize=2, linestyle='none', markeredgecolor='grey')
meanprops={ "markerfacecolor":"sandybrown", "markeredgecolor":"chocolate"}
fig, ax = plt.subplots(figsize=(20, 12), dpi=300)
spacing_factor = 9
showmeans = False
sep = 0.9
width = 0.65

syn = plt.boxplot(all_data[0].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor-sep/2-4*sep, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
vxm = plt.boxplot(all_data[1].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor-sep/2-3*sep, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
trmo = plt.boxplot(all_data[2].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor-sep/2-2*sep, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
trma = plt.boxplot(all_data[3].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor-sep/2-sep, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
i2g = plt.boxplot(all_data[4].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor-sep/2, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
modet = plt.boxplot(all_data[5].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor+sep/2, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
mabmo = plt.boxplot(all_data[6].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor+sep/2+sep, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
vmabmo = plt.boxplot(all_data[7].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor+sep/2+2*sep, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
# rdp = plt.boxplot(all_data[8].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor+sep/2+3*sep, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops, patch_artist=True)
our = plt.boxplot(all_data[8].T, labels=outstruct, positions=np.array(range(len(outstruct)))*spacing_factor+sep/2+3*sep, widths=width, showmeans=showmeans, flierprops=flierprops, meanprops=meanprops,patch_artist=True)

set_box_color(syn, 'plum') # colors are from http://colorbrewer2.org/
set_box_color(vxm, 'slateblue')
set_box_color(trmo, 'tan')
set_box_color(trma, 'pink')
set_box_color(i2g, 'wheat')
set_box_color(modet, 'olive')
set_box_color(mabmo, 'sandybrown')
set_box_color(vmabmo, 'salmon') 
# set_box_color(rdp, 'teal')
set_box_color(our, 'red')
plt.grid(linestyle='--', linewidth=1)

plt.plot([], c='plum', label='SyN')
plt.plot([], c='slateblue', label='VoxelMorph')
plt.plot([], c='tan', label='TransMorph')
plt.plot([], c='pink', label='TransMatch')
plt.plot([], c='wheat', label='Im2Grid')
plt.plot([], c='olive', label='ModeT')
plt.plot([], c='sandybrown', label='MambaMorph')
plt.plot([], c='salmon', label='VMambaMorph')
# plt.plot([], c='teal', label='RDP')
plt.plot([], c='red', label='Our')

font_manager.fontManager.addfont('./font/TIMES.TTF')  
font = font_manager.FontProperties(family= 'Times New Roman', 
                                   style='normal', size=20)#'Cambria',
leg = ax.legend(prop=font)
for line in leg.get_lines():
    line.set_linewidth(5.0)
minor_ticks = np.arange(-10.8, len(outstruct) * spacing_factor, 0.8)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(np.arange(0, 1.05, 0.2))
ax.set_yticks(np.arange(-0.05, 1.05, 0.05), minor=True)
ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')

plt.xticks(range(0, len(outstruct) * spacing_factor, spacing_factor), outstruct, fontsize=25)
plt.yticks(fontsize=25)
for tick in ax.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.xlim(-5, len(outstruct)*spacing_factor-4.2)
plt.ylim(-0.00, 0.9)
plt.tight_layout()
# plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.2)
plt.show()
# %%