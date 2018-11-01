### This script combines the annual gain rate tiles from different forest types (non-mangrove natural forests, mangroves,
### plantations, into combined tiles. It does the same for cumulative gain over the study period.

import multiprocessing
import utilities
import merge_cumulative_annual_gain_all_forest_types

biomass_tile_list = utilities.tile_list(utilities.biomass_dir)
# biomass_tile_list = ['20S_110E', '30S_110E'] # test tiles
# biomass_tile_list = ['20S_110E'] # test tiles
print biomass_tile_list

# For downloading all tiles in the input folders
download_list = [utilities.cumul_gain_natrl_forest_dir, utilities.cumul_gain_mangrove_dir,
                 utilities.annual_gain_natrl_forest_dir, utilities.annual_gain_mangrove_dir]

for input in download_list:
    utilities.s3_folder_download('{}'.format(input), '.')

# # For copying individual tiles to spot machine for testing
# for tile in biomass_tile_list:
#
#     utilities.s3_file_download('{0}{1}_{2}.tif'.format(utilities.annual_gain_natrl_forest_dir, utilities.pattern_annual_gain_natrl_forest, tile), '.')  # annual gain rate tiles for natural forests
#     utilities.s3_file_download('{0}{1}_{2}.tif'.format(utilities.annual_gain_mangrove_dir, utilities.pattern_annual_gain_mangrove, tile), '.')  # annual gain rate tiles for mangroves
#     utilities.s3_file_download('{0}{1}_{2}.tif'.format(utilities.cumul_gain_natrl_forest_dir, utilities.pattern_cumul_gain_natrl_forest, tile), '.')           # cumulative gain tiles for natural forests
#     utilities.s3_file_download('{0}{1}_{2}.tif'.format(utilities.cumul_gain_mangrove_dir, utilities.pattern_cumul_gain_mangrove, tile), '.')  # cumulative gain tiles for mangroves

count = multiprocessing.cpu_count()
pool = multiprocessing.Pool(count / 4)
pool.map(merge_cumulative_annual_gain_all_forest_types.gain_merge, biomass_tile_list)

# # For single processor use
# for tile in biomass_tile_list:
#
#     cumulative_gain_all_forest_types.cumulative_annual_gain_merge(tile)
