#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sys/stat.h>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <stdint.h>
#include <sstream>
#include <iomanip>
#include <gdal/gdal_priv.h>
#include <gdal/cpl_conv.h>
#include <gdal/ogr_spatialref.h>
using namespace std;
//to compile:  c++ raster_math.cpp -o raster_math -lgdal
// ./dead_wood_c_stock.exe 00N_000E_biomass.tif 00N_000E_res_ecozone.tif 00N_000E_res_srtm.tif 00N_000E_res_srtm.tif test.tif > values.txt

int main(int argc, char* argv[])
{
//passing arguments
if (argc != 6){cout << "Use <program name> <above ground biomass> <biome raster> <elevation raster> <precip raster> <output name>" << endl; return 1;}
string agb_name=argv[1];
string biome_name=argv[2];
string elevation_name=argv[3];
string precip_name=argv[4];
//either parse this var from inputs or send it in
string out_name=argv[5];

//setting variables
int x, y;
int xsize, ysize;
double GeoTransform[6]; double ulx, uly; double pixelsize;

//initialize GDAL for reading
GDALAllRegister();
GDALDataset  *INGDAL; GDALRasterBand  *INBAND;
GDALDataset  *INGDAL2; GDALRasterBand  *INBAND2;
GDALDataset  *INGDAL3; GDALRasterBand  *INBAND3;
GDALDataset  *INGDAL4; GDALRasterBand  *INBAND4;

//open file and get extent and projection
INGDAL = (GDALDataset *) GDALOpen(agb_name.c_str(), GA_ReadOnly ); 
INBAND = INGDAL->GetRasterBand(1);
xsize=INBAND->GetXSize(); 
ysize=INBAND->GetYSize();
INGDAL->GetGeoTransform(GeoTransform);
ulx=GeoTransform[0]; 
uly=GeoTransform[3]; 
pixelsize=GeoTransform[1];
cout << xsize <<", "<< ysize <<", "<< ulx <<", "<< uly << ", "<< pixelsize << endl;

INGDAL2 = (GDALDataset *) GDALOpen(biome_name.c_str(), GA_ReadOnly ); 
INBAND2 = INGDAL2->GetRasterBand(1);
INGDAL3 = (GDALDataset *) GDALOpen(elevation_name.c_str(), GA_ReadOnly ); 
INBAND3 = INGDAL3->GetRasterBand(1);
INGDAL4 = (GDALDataset *) GDALOpen(precip_name.c_str(), GA_ReadOnly ); 
INBAND4 = INGDAL4->GetRasterBand(1);

//initialize GDAL for writing
GDALDriver *OUTDRIVER;
GDALDataset *OUTGDAL;
GDALRasterBand *OUTBAND1;
OGRSpatialReference oSRS;
char *OUTPRJ = NULL;
char **papszOptions = NULL;
papszOptions = CSLSetNameValue( papszOptions, "COMPRESS", "LZW" );
OUTDRIVER = GetGDALDriverManager()->GetDriverByName("GTIFF"); 
if( OUTDRIVER == NULL ) {cout << "no driver" << endl; exit( 1 );};
oSRS.SetWellKnownGeogCS( "WGS84" );
oSRS.exportToWkt( &OUTPRJ );
double adfGeoTransform[6] = { ulx, pixelsize, 0, uly, 0, -1*pixelsize };
OUTGDAL = OUTDRIVER->Create( out_name.c_str(), xsize, ysize, 1, GDT_Float32, papszOptions );
OUTGDAL->SetGeoTransform(adfGeoTransform); OUTGDAL->SetProjection(OUTPRJ); 
OUTBAND1 = OUTGDAL->GetRasterBand(1);
OUTBAND1->SetNoDataValue(-9999);

//read/write data
uint16_t agb_data[xsize];
uint16_t biome_data[xsize];
uint16_t elevation_data[xsize];
uint16_t precip_data[xsize];
float out_data1[xsize];

for(y=0; y<ysize; y++) {
INBAND->RasterIO(GF_Read, 0, y, xsize, 1, agb_data, xsize, 1, GDT_UInt16, 0, 0); 
INBAND2->RasterIO(GF_Read, 0, y, xsize, 1, biome_data, xsize, 1, GDT_UInt16, 0, 0); 
INBAND3->RasterIO(GF_Read, 0, y, xsize, 1, elevation_data, xsize, 1, GDT_UInt16, 0, 0); 
INBAND4->RasterIO(GF_Read, 0, y, xsize, 1, precip_data, xsize, 1, GDT_UInt16, 0, 0); 

for(x=0; x<xsize; x++) {
    // biomass * .5 = carbon. so take carbon * the factor
  if (biome_data[x] = 1 && elevation_data[x] < 2000 && precip_data[x] < 1000) {
    out_data1[x] = agb_data[x] * .01;}
  else if (biome_data[x] = 1 && elevation_data[x] < 2000 && precip_data[x] < 1600 && precip_data[x] > 1000) {
    out_data1[x] = agb_data[x] * .005;}
  else if (biome_data[x] = 1 && elevation_data[x] < 2000 && precip_data[x] > 1600) {
    out_data1[x] = agb_data[x] * .03;}
  else if (biome_data[x] = 1 && elevation_data[x] > 2000) {
    out_data1[x] = agb_data[x] * .035;}
  else if (biome_data[x] = 2) {
    out_data1[x] = agb_data[x] * .04;}
  else {
    out_data1[x] = -9999;}

//closes for x loop
}
OUTBAND1->RasterIO( GF_Write, 0, y, xsize, 1, out_data1, xsize, 1, GDT_Float32, 0, 0 ); 
//closes for y loop
}

//close GDAL
GDALClose(INGDAL);
GDALClose((GDALDatasetH)OUTGDAL);

return 0;
}