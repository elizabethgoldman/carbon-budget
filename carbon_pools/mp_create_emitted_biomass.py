import create_emitted_biomass
import multiprocessing
import sys
sys.path.append('../')
import constants_and_names as cn
import universal_util as uu

# tile_list = uu.tile_list(cn.natrl_forest_biomass_2000_dir)
tile_list = ['10N_080W', '40N_120E'] # test tiles
print tile_list

# For downloading all tiles in the input folders.
input_files = [
    cn.natrl_forest_biomass_2000_dir,
    cn.mangrove_biomass_2000_dir,
    cn.cumul_gain_AGC_mangrove_dir,
    cn.cumul_gain_AGC_natrl_forest_dir
    ]

# for input in input_files:
#     uu.s3_folder_download('{}'.format(input), '.')

# For copying individual tiles to spot machine for testing.
# The cumulative carbon gain tiles are for adding to the biomass 2000 tiles to get AGC at the time of tree cover loss.
for tile in tile_list:

    uu.s3_file_download('{0}{1}_{2}.tif'.format(cn.natrl_forest_biomass_2000_dir, tile,
                                                            cn.pattern_natrl_forest_biomass_2000), '.')
    uu.s3_file_download('{0}{1}_{2}.tif'.format(cn.mangrove_biomass_raw_dir, tile,
                                                            cn.pattern_mangrove_biomass_emitted), '.')
    uu.s3_file_download('{0}{1}_{2}.tif'.format(cn.cumul_gain_AGC_mangrove_dir,
                                                            cn.pattern_cumul_gain_AGC_mangrove, tile), '.')
    uu.s3_file_download('{0}{1}_{2}.tif'.format(cn.cumul_gain_AGC_natrl_forest_dir,
                                                            cn.pattern_cumul_gain_AGC_natrl_forest, tile), '.')

print "Creating tiles of emitted biomass (biomass 2000 + biomass accumulation)"

count = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=count/3)
pool.map(create_emitted_biomass.create_emitted_biomass, tile_list)
