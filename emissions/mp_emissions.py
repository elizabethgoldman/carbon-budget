import multiprocessing
import calc_emissions
import utilities
import tile_peat_dict


def chunks(l, n):
    # Yield successive n-sized chunks from l
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

# Location of the carbon pools
carbon_pool_dir = 's3://gfw2-data/climate/carbon_model/carbon_pools/20180815'

carbon_tile_list = utilities.tile_list('{}/carbon/'.format(carbon_pool_dir))
# carbon_tile_list = ['00N_000E'] # test tile
# carbon_tile_list = ['00N_000E', '30N_080W', '30N_090W', '30N_100W', '40N_090W'] # test tile
print 'Carbon tile list is: ' + str(carbon_tile_list)
print 'Number of carbon tiles is: ' + str(len(carbon_tile_list))

count = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=count / 4)

# How many tiles the spot machine will process at one time
# Set to process half as many tiles at one time as processors it is using
tiles_in_chunk = count / 10

for chunk in chunks(carbon_tile_list, tiles_in_chunk):

    print 'Chunk is: ' + str(chunk)

    with open('status.txt', 'a') as textfile:
        textfile.write(str(chunk) + "\n")

    for tile_id in chunk:
        print '   tile_id is: ' + str(tile_id)

        # download files

        #### MAY NEED TO CHANGE THIS TO REFLECT THE NEW SOIL AND PEAT MASK THAT THAI CREATED
        peat_file = tile_peat_dict.tile_peat_dict(tile_id) # based on tile id, know which peat file to download (hwsd, hist, jukka)

        files = {'carbon_pool': ['bgc', 'carbon', 'deadwood', 'soil', 'litter'], 'data_prep': [peat_file, 'ifl_2000', 'gfw_plantations', 'tsc_model', 'climate_zone'],
                 'fao_ecozone': ['fao_ecozones_bor_tem_tro'], 'burned_area': ['burn_year_with_Hansen_loss']}

        print '      Downloading input tiles'
        utilities.download(files, tile_id, carbon_pool_dir)

        #download hansen tile
        hansen_tile = utilities.wgetloss(tile_id)

        #if idn plant tile downloaded, mask loss with plantations because we know that idn gfw_plantations
        # were established in yr 2000.
        if tile_id in ['00N_090E', '00N_100E', '00N_110E', '00N_120E', '00N_130E', '00N_140E', '10N_090E', '10N_100E', '10N_110E', '10N_120E', '10N_130E', '10N_140E']:
            print "cutting out plantations in Indonesia, Malaysia"
            utilities.mask_loss(tile_id)

    pool.map(calc_emissions.calc_emissions, chunk)
