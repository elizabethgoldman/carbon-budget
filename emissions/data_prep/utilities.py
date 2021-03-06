import subprocess
import os


def coords(tile_id):
    NS = tile_id.split("_")[0][-1:]
    EW = tile_id.split("_")[1][-1:]

    if NS == 'S':
        ymax =-1*int(tile_id.split("_")[0][:2])
    else:
        ymax = int(str(tile_id.split("_")[0][:2]))
    
    if EW == 'W':
        xmin = -1*int(str(tile_id.split("_")[1][:3]))
    else:
        xmin = int(str(tile_id.split("_")[1][:3]))

    ymin = str(int(ymax) - 10)
    xmax = str(int(xmin) + 10)
    
    return ymax, xmin, ymin, xmax
    
    
def rasterize(shapefile, tile_id):

    print "rasterizing: {}".format(shapefile)
    ymax, xmin, ymin, xmax = coords(tile_id)
    
    d = {'fao_ecozones_bor_tem_tro': 'recode','ifl_2000': 'temp_id','peatland_drainage_proj': 'emisC02ha','gfw_plantations': 'c02emiss'}
    rvalue = d[shapefile]
    
    rasterized_tile = "{0}_res_{1}.tif".format(tile_id, shapefile)
    
    cmd = ['gdal_rasterize', '-co', 'COMPRESS=LZW', '-tr', '0.00025', '0.00025', '-ot',
                         'Byte', '-a', rvalue, '-a_nodata', '0', shapefile + ".shp", rasterized_tile, '-te', str(xmin), str(ymin), str(xmax), str(ymax)]
                      
    subprocess.check_call(cmd)

    return rasterized_tile


def resample_clip(raster, tile_id):
    print "resampling: {}".format(raster)
    
    ymax, xmin, ymin, xmax = coords(tile_id)
    
    input_raster = raster + ".tif"
    clipped_raster = '{0}_res_{1}.tif'.format(tile_id, raster)
    
    if raster == "forest_model":
    
        cmd = ['gdalwarp', '-co', 'COMPRESS=LZW', '-ot', 'Byte', '-tr', '.00025', '.00025', '-tap', '-te', str(xmin), str(ymin), str(xmax), str(ymax), input_raster, clipped_raster, ]
       
        subprocess.check_call(cmd)
 
    elif raster == 'cifor_peat_mask':
        # cifor raster is large resolution. so, clip to a larger extent than tile, then clip down to tile size
        xmin = str(int(xmin) -.1)
        ymax = str(int(ymax) + .1)
        xmax = str(int(xmax) + .1)
        ymin = str(int(ymin) -.1)
        
        cmd = ['gdalwarp', '-tr', '.00025', '.00025',  '-co', 'COMPRESS=LZW', '-tap', input_raster, clipped_raster, '-te', str(xmin), str(ymin), str(xmax), str(ymax)]        
        
        subprocess.check_call(cmd)

    else:
        cmd = ['gdalwarp', '-tr', '.00025', '.00025',  '-co', 'COMPRESS=LZW', '-tap', input_raster, clipped_raster, '-te', str(xmin), str(ymin), str(xmax), str(ymax)]

        subprocess.check_call(cmd) 

    return clipped_raster
