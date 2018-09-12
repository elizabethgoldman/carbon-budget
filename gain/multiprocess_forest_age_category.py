###

import multiprocessing
import utilities
import forest_age_category

### Need to update rasterio package on spot machine before running
### sudo pip install rasterio --update

# Loss, gain, and tree cover density, intact forest landscape, biomass tiles, and continent-ecozone
# All of these are needed for the forest age decision tree
loss = 's3://gfw2-data/forest_change/hansen_2015/Loss_tiles/'
gain = 's3://gfw2-data/forest_change/tree_cover_gain/gaindata_2012/'
tcd = 's3://gfw2-data/forest_cover/2000_treecover/'
ifl = 's3://gfw2-data/climate/carbon_model/other_emissions_inputs/ifl_2000/'
biomass = 's3://gfw2-data/climate/WHRC_biomass/WHRC_V4/Processed/'
cont_eco = 's3://gfw2-data/climate/carbon_model/fao_ecozones/ecozone/20180912/'


# biomass_tile_list = utilities.tile_list(biomass)
# biomass_tile_list = ["00N_000E", "00N_050W", "00N_060W", "00N_010E", "00N_020E", "00N_030E", "00N_040E", "10N_000E", "10N_010E", "10N_010W", "10N_020E", "10N_020W"] # test tiles
biomass_tile_list = ['00N_050W'] # test tile
print biomass_tile_list

# download_list = [loss, gain, tcd, ifl, biomass, cont_eco]
#
# # For downloading all tiles in the folders
# for input in download_list:
#     utilities.s3_folder_download('{}'.format(input), '.')

# # For copying individual tiles to s3 for testing
# for tile in biomass_tile_list:
#
#     utilities.s3_file_download('{0}{1}.tif'.format(loss, tile), '.')                                # loss tiles
#     utilities.s3_file_download('{0}Hansen_GFC2015_gain_{1}.tif'.format(gain, tile), '.')            # gain tiles
#     utilities.s3_file_download('{0}Hansen_GFC2014_treecover2000_{1}.tif'.format(tcd, tile), '.')    # tcd 2000
#     utilities.s3_file_download('{0}{1}_res_ifl_2000.tif'.format(ifl, tile), '.')                    # ifl 2000
#     utilities.s3_file_download('{0}{1}_biomass.tif'.format(biomass, tile), '.')                     # biomass 2000
#     utilities.s3_file_download('{0}fao_ecozones_{1}.tif'.format(cont_eco, tile), '.')               # continents and FAO ecozones 2000

# count = multiprocessing.cpu_count()
# pool = multiprocessing.Pool(processes=count/4)
# pool.map(forest_age_category.forest_age_category, biomass_tile_list)

# For single processor use
for tile in biomass_tile_list:

    forest_age_category.forest_age_category(tile)
