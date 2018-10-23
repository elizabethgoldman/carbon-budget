###

import multiprocessing
import utilities
import tile_statistics
import subprocess

### sudo pip install rasterio --upgrade
### sudo pip install scipy

# mangrove_biomass_tile_list = utilities.tile_list(utilities.mangrove_biomass_dir)
# mangrove_biomass_tile_list = ["00N_000E", "00N_050W", "00N_060W", "00N_010E", "00N_020E", "00N_030E", "00N_040E", "10N_000E", "10N_010E", "10N_010W", "10N_020E", "10N_020W"] # test tiles
mangrove_biomass_tile_list = ['20S_110E'] # test tile
print mangrove_biomass_tile_list

# # For downloading all tiles in the folders
# download_list = [utilities.mangrove_biomass_dir]
#
# for input in download_list:
#     utilities.s3_folder_download('{}'.format(input), '.')

# # For copying individual tiles to spot machine for testing
# for tile in mangrove_biomass_tile_list:
#
#     utilities.s3_file_download('{0}{1}.tif'.format(utilities.loss_dir, tile), '.')      # loss tiles


# # For multiprocessor use
# count = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=count/4)
# pool.map(tile_statistics.create_tile_statistics, biomass_tile_list)

# For single processor use
for tile in mangrove_biomass_tile_list:

    tile_statistics.create_tile_statistics(tile)