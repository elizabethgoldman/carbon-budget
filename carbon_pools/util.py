import subprocess
import gdal
from gdalconst import GA_ReadOnly


def download(source):
    cmd = ['aws', 's3', 'cp', source, '.']
    subprocess.check_call(cmd)


def upload(src, dest):
    cmd = ['aws', 's3', 'cp', src, dest]
    subprocess.check_call(cmd)


def get_extent(tif):
    data = gdal.Open(tif, GA_ReadOnly)
    geoTransform = data.GetGeoTransform()
    minx = geoTransform[0]
    maxy = geoTransform[3]
    maxx = minx + geoTransform[1] * data.RasterXSize
    miny = maxy + geoTransform[5] * data.RasterYSize
    print [minx, miny, maxx, maxy]

    return minx, miny, maxx, maxy


def resample(in_file, out_file):
    resample = ['gdal_translate', '-co', 'COMPRESS=LZW', '-tr', '.00025', '.00025', in_file, out_file]
    subprocess.check_call(resample)

    return out_file


def clip(in_file, out_file,  xmin, ymin, xmax, ymax, extra_param=None):

    cmd = ['gdalwarp', '-te', str(xmin), str(ymin), str(xmax), str(ymax), '-co', 'COMPRESS=LZW', in_file, out_file]
    if extra_param:
        cmd += extra_param + ['-tap']

    subprocess.check_call(cmd)

    return out_file


def rasterize(in_shape, out_tif, xmin, ymin, xmax, ymax, tr=None, ot=None, recode=None, anodata=None):
    cmd = ['gdal_rasterize', '-co', 'COMPRESS=LZW', '-te', str(xmin), str(ymin), str(xmax), str(ymax),
           '-tr', tr, tr, '-ot', ot, '-a', recode, '-a_nodata',
           anodata, in_shape, out_tif]

    subprocess.check_call(cmd)

    return out_tif


# Lists the tiles in a folder in s3
def tile_list(source):

    ## For an s3 folder in a bucket using AWSCLI
    # Captures the list of the files in the folder
    out = subprocess.Popen(['aws', 's3', 'ls', source], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()

    # Writes the output string to a text file for easier interpretation
    totalCtiles = open("biomass_tiles.txt", "w")
    totalCtiles.write(stdout)
    totalCtiles.close()

    file_list = []

    # Iterates through the text file to get the names of the tiles and appends them to list
    with open("biomass_tiles.txt", 'r') as tile:
        for line in tile:

            num = len(line.strip('\n').split(" "))
            tile_name = line.strip('\n').split(" ")[num - 1]
            tile_short_name = tile_name.replace('_biomass.tif', '')
            file_list.append(tile_short_name)

    file_list = file_list[1:]

    return file_list