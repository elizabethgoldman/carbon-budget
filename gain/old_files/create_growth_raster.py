import os
import sys
import subprocess

import gain.utilities



def create_growth_raster(tile_age):
    tile_id = tile_age[0]
    age = tile_age[1]

    shapefile = 'growth_rate.shp'
    print tile_id
    ymax, xmin, ymin, xmax = gain.utilities.coords(tile_id)

    output_tif = "{0}_{1}.tif".format(tile_id, age)

    growth = gain.utilities.rasterize_shapefile(xmin, ymax, xmax, ymin, shapefile, output_tif, age)

    #resampled_tif = growth.replace(".tif", "_res.tif")
    #utilities.resample_00025(growth, resampled_tif)

    cmd = ['aws', 's3', 'mv', growth, 's3://gfw-files/sam/carbon_budget/growth_rasters_v2/']
    # print cmd
    subprocess.check_call(cmd)
