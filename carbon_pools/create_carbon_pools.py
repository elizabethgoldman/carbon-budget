import datetime
import os
import subprocess
import glob
sys.path.append('../')
import constants_and_names
import universal_util

def create_carbon_pools(tile_id):

    start = datetime.datetime.now()

    print 'Writing aboveground carbon, belowground carbon, deadwood, litter, total carbon'
    calc_all_cmd = ['./calc_all.exe', tile_id]
    subprocess.check_call(calc_all_cmd)

    print 'Uploading tiles to s3'
    universal_util.upload_final(constants_and_names.agc_dir, tile_id, constants_and_names.pattern_agc)
    universal_util.upload_final(constants_and_names.bgc_dir, tile_id, constants_and_names.pattern_bgc)
    universal_util.upload_final(constants_and_names.deadwood_dir, tile_id, constants_and_names.pattern_deadwood)
    universal_util.upload_final(constants_and_names.litter_dir, tile_id, constants_and_names.pattern_litter)
    universal_util.upload_final(constants_and_names.soil_C_pool_dir, tile_id, constants_and_names.pattern_soil_pool)
    universal_util.upload_final(constants_and_names.total_C_dir, tile_id, constants_and_names.pattern_total_C)

    print "Deleting intermediate data"
    tiles_to_remove = glob.glob('*{}*'.format(tile_id))
    for tile in tiles_to_remove:
        try:
            os.remove(tile)
        except:
            pass

    print "elapsed time: {}".format(datetime.datetime.now() - start)
