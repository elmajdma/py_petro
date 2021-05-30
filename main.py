import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lasio

import os

#basepath=os.listdir("C:/Users/lenovo/pycharmProjects/py_petro/")
file_path="C:/Users/lenovo/pycharmProjects/py_petro/test.las"
las = lasio.read(file_path)
#print(las.well)

# for item in las.well:
#     print(f"{item.descr} ({item.mnemonic}): {item.value}")
#
# for count, curve in enumerate(las.curves):
#     print(f"Curve: {curve.mnemonic}, Units: {curve.unit}, Description: {curve.descr}")
# print(f"There are a total of: {count+1} curves present within this file")

well_data=las.df()
print(well_data.head())

# #Set up the plot axes
# ax1 = plt.subplot2grid((1,5), (0,0), rowspan=1, colspan = 1)
# ax2 = plt.subplot2grid((1,5), (0,1), rowspan=1, colspan = 1)
# ax3 = plt.subplot2grid((1,5), (0,2), rowspan=1, colspan = 1)
# ax4 = plt.subplot2grid((1,5), (0,3), rowspan=1, colspan = 1)
# ax5 = plt.subplot2grid((1,5), (0,4), rowspan=1, colspan = 1)

well_nan = well_data.notnull()
# columns = well_nan.columns
# axes = [ax1, ax2, ax3, ax4, ax5]
# for i, ax in enumerate(axes):
#     ax.plot(well_nan.iloc[:,i], well_nan.index, lw=0)
#     ax.set_ylim(11500, 11000)
#     ax.set_xlim(0, 1)
#     ax.set_title(columns[i])
#     ax.set_facecolor('r')
#     ax.fill_betweenx(well_nan.index, 0, well_nan.iloc[:,i], facecolor='g')
#     # Remove tick labels from each subplot
#     if i > 0:
#         plt.setp(ax.get_yticklabels(), visible = False)
#     plt.setp(ax.get_xticklabels(), visible = False)
# ax1.set_ylabel('Depth', fontsize=14)
# plt.subplots_adjust(wspace=0)
# plt.show()

# fig, ax = plt.subplots(figsize=(15, 10))
# # Set up the plot axes
# ax1 = plt.subplot2grid((1, 6), (0, 0), rowspan=1, colspan=1)
# ax2 = plt.subplot2grid((1, 6), (0, 1), rowspan=1, colspan=1, sharey=ax1)
# ax3 = plt.subplot2grid((1, 6), (0, 2), rowspan=1, colspan=1, sharey=ax1)
# ax4 = plt.subplot2grid((1, 6), (0, 3), rowspan=1, colspan=1, sharey=ax1)
# ax5 = ax3.twiny()  # Twins the y-axis for the density track with the neutron track
# ax6 = plt.subplot2grid((1, 6), (0, 4), rowspan=1, colspan=1, sharey=ax1)
# ax7 = ax2.twiny()
# # As our curve scales will be detached from the top of the track,
# # this code adds the top border back in without dealing with splines
# ax10 = ax1.twiny()
# ax10.xaxis.set_visible(False)
# ax11 = ax2.twiny()
# ax11.xaxis.set_visible(False)
# ax12 = ax3.twiny()
# ax12.xaxis.set_visible(False)
# ax13 = ax4.twiny()
# ax13.xaxis.set_visible(False)
# ax14 = ax6.twiny()
# ax14.xaxis.set_visible(False)
# # Gamma Ray track
# ax1.plot(well_data["GR"], well_data.index, color="green", linewidth=0.75)
# ax1.set_xlabel("GR")
# ax1.xaxis.label.set_color("green")
# ax1.set_xlim(0, 200)
# ax1.set_ylabel("Depth (MDft)")
# ax1.tick_params(axis='x', colors="green")
# ax1.spines["top"].set_edgecolor("green")
# ax1.title.set_color('green')
# ax1.set_xticks(np.arange(0, 200, 20))
#
# # Resistivity track
# ax2.plot(well_data["LLD"], well_data.index, color="red", linewidth=0.5)
# ax2.set_xlabel("LLD")
# ax2.set_xlim(0.2, 2000)
# ax2.xaxis.label.set_color("red")
# ax2.tick_params(axis='x', colors="red")
# ax2.spines["top"].set_edgecolor("red")
# ax2.set_xticks([0.1, 1, 10, 100, 1000])
# ax2.semilogx()
#
# # Resistivity track - Curve 2
# ax7.plot(well_data["LLS"], well_data.index, color="b", linewidth=0.5)
# ax7.set_xlabel("LLS")
# ax7.set_xlim(0.2, 2000)
# ax7.xaxis.label.set_color("b")
# ax7.spines["top"].set_position(("axes", 1.08))
# ax7.spines["top"].set_visible(True)
# ax7.tick_params(axis='x', colors="b")
# ax7.spines["top"].set_edgecolor("b")
# ax7.set_xticks([0.1, 1, 10, 100, 1000])
# ax7.semilogx()
#
# # Density track
# ax3.plot(well_data["RHOB"], well_data.index, color="red", linewidth=0.5)
# ax3.set_xlabel("RHOB")
# ax3.set_xlim(1.95, 2.95)
# ax3.xaxis.label.set_color("red")
# ax3.tick_params(axis='x', colors="red")
# ax3.spines["top"].set_edgecolor("red")
# ax3.set_xticks([1.95, 2.15, 2.35, 2.55, 2.75, 2.95])
#
# # Neutron track placed ontop of density track
# ax5.plot(well_data["NPHI"], well_data.index, color="blue", linewidth=0.5)
# ax5.set_xlabel('NPHI')
# ax5.xaxis.label.set_color("blue")
# ax5.set_xlim(0.45, -0.15)
# # ax5.set_ylim(4150, 3500)
# ax5.tick_params(axis='x', colors="blue")
# ax5.spines["top"].set_position(("axes", 1.08))
# # ax5.spines["top"].set_visible(True)
# ax5.spines["top"].set_edgecolor("blue")
# ax5.set_xticks([0.45, 0.33, 0.21, 0.15, 0.09, -0.03, -0.15])
#
# # Common functions for setting up the plot can be extracted into
# # a for loop. This saves repeating code.
# for ax in [ax1, ax2, ax3, ax4, ax6]:
#     ax.set_ylim(11450, 11050)
#
#     ax.grid(which='major', color='lightgrey', linestyle='-')
#     ax.xaxis.set_ticks_position("top")
#     ax.xaxis.set_label_position("top")
#     ax.spines["top"].set_position(("axes", 1.02))
#
# for ax in [ax2, ax3, ax4, ax6]:
#     plt.setp(ax.get_yticklabels(), visible=False)
#
# plt.tight_layout()
# fig.subplots_adjust(wspace=0)
# plt.show()

#fig, axs = plt.subplots(2, 2, figsize=(7,7))
fig2, ax_cross = plt.subplots(figsize=(10,10))
well_data.plot(kind='scatter', x='NPHI', y='RHOB',
            ax=ax_cross, c='GR', cmap='jet', vmin=0, vmax=150)
ax_cross.set_xlim(0,0.6)
ax_cross.set_ylim(2.7,2)
ax_cross.set_title('Test')
ax_cross.grid(True)
ax_cross.set_axisbelow(True)
plt.tight_layout()
plt.show()