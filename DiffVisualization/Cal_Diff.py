#%%
import matplotlib
# %matplotlib inline
import matplotlib as mpl
from matplotlib import pylab as plt
import matplotlib.colors as mcolors
# matplotlib.use('TkAgg')  # If use this line, the show of image will generate a new window out of jupyter.

import numpy as np
import pylab

import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D

# pylab.rcParams['figure.figsize'] = (27.0, 24.0)
#%%
class MidpointNormalize(mpl.colors.Normalize):
    ## class from the mpl docs:
    # https://matplotlib.org/users/colormapnorms.html

    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        super().__init__(vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))
        # x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        # result = np.interp(value, x, y)
        
        # if clip is None:
        #     clip = self.clip
        # if clip:
        #     result = np.clip(result, 0, 1)
        
        # return np.ma.masked_array(result)

example_filename = './S03/fixed.nii.gz'  # fixed image
img1 = nib.load(example_filename)
# print(img1.header['db_name'])  # 输出头信息

example2_filename = './S03/deformed_VoxelMorph.nii.gz'  # warped image
# example2_filename = './S11.nii.gz'  # moving image
img2 = nib.load(example2_filename)
# print(img2.header['db_name'])  # 输出头信息

width, height, queue = img1.dataobj.shape
# OrthoSlicer3D(img2.dataobj).show()
#%%
# subtract and save the diff image
# img_diff = np.array(img1.dataobj) - np.array(img2.dataobj)
# img_diff = nib.Nifti1Image(img_diff, img1.affine)
# nib.save(img_diff, './S03/diff_our.nii.gz')

#%%
min_error = np.inf
num = 1
for i in range(87, 88, 1): # index 88
#     img_arr1 = img1.dataobj[:, :, i]
#     img_arr2 = img2.dataobj[:, :, i]
    img_arr1 = img1.dataobj[:, :, i]
    img_arr1 = np.fliplr(np.rot90(img_arr1, 3))
    # img_arr1 = img1.dataobj[:, i, :]
    # img_arr1 = np.rot90(img_arr1, 1)
    # normalize the image
    img_arr1 = (img_arr1 - np.min(img_arr1)) / (np.max(img_arr1) - np.min(img_arr1))
    # plt.imshow(img_arr1, cmap='gray')
    # plt.show()
    img_arr2 = img2.dataobj[:, :, i]
    img_arr2 = np.fliplr(np.rot90(img_arr2, 3))
    # img_arr2 = img2.dataobj[:, i, :]
    # img_arr2 = np.rot90(img_arr2, 1)
    # normalize the image
    img_arr2 = (img_arr2 - np.min(img_arr2)) / (np.max(img_arr2) - np.min(img_arr2))
    # plt.imshow(img_arr2, cmap='gray')
    # plt.show()

    img_arr_diff = img_arr1 - img_arr2
    sum_abs_diff = np.sum(np.abs(img_arr_diff))
    # if sum_abs_diff < min_error:
    #     min_error = sum_abs_diff
    #     # min_error_slice = i
    #     print('min_error:', min_error)
    # plt.subplot(5, 6, num)
    print('sum_abs_diff:', sum_abs_diff)
    # plt.title('slice ' + str(i+1) + '/' + str(height))
    plt.imshow(img_arr_diff, cmap='bwr', norm=MidpointNormalize(midpoint=0))
    plt.clim(-0.5,0.5)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.rcParams['font.size'] = 10
    cbar = plt.colorbar(fraction=0.046, pad=0.04)
    # 设置刻度线的样式为透明，这样它们就不会显示出来
    cbar.ax.yaxis.set_tick_params(length = 0.5)  # 设置刻度线长度
    plt.show()
    num += 1
# plt.figure(figsize=(361,315))

# %%
plt.colormaps()