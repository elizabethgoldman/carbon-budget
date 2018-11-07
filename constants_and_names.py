
##### Constants

# Biomass to carbon ratio
biomass_to_c = 0.5

c_to_co2 = 3.67

# Aboveground to belowground biomass ratios
above_to_below_natrl_forest = 0.26
above_to_below_mangrove = 0.608

##### File names and directories

pattern_emissions_total = 'disturbance_model'
emissions_total_dir = 's3://gfw2-data/climate/carbon_model/output_emissions/20180828/disturbance_model/'

# Spreadsheet with annual gain rates
gain_spreadsheet = 'gain_rate_continent_ecozone_age_20181017.xlsx'

# Woods Hole biomass 2000 version 4 tiles
biomass_dir = 's3://gfw2-data/climate/WHRC_biomass/WHRC_V4/Processed/'

# Lola Fatoyinbo aboveground mangrove biomass tiles
pattern_mangrove_biomass = 'mangrove_agb_t_ha'
mangrove_biomass_dir = 's3://gfw2-data/climate/carbon_model/mangrove_biomass/processed/20181019/'

# Annual Hansen loss tiles (2001-2015)
loss_dir = 's3://gfw2-data/forest_change/hansen_2015/Loss_tiles/'

# Hansen gain tiles (2001-2012)
pattern_gain = 'Hansen_GFC2015_gain'
gain_dir = 's3://gfw2-data/forest_change/tree_cover_gain/gaindata_2012/'

# Tree cover density 2000 tiles
pattern_tcd = 'Hansen_GFC2014_treecover2000'
tcd_dir = 's3://gfw2-data/forest_cover/2000_treecover/'

# Intact forest landscape 2000 tiles
pattern_ifl = 'res_ifl_2000'
ifl_dir = 's3://gfw2-data/climate/carbon_model/other_emissions_inputs/ifl_2000/'

# Processed FAO ecozone shapefile
cont_ecozone_shp = 'fao_ecozones_fra_2000_continents_assigned_dissolved_FINAL_20180906.zip'

# Directory and names for the continent-ecozone tiles, raw and processed
pattern_cont_eco_raw = 'fao_ecozones_continents_raw'
pattern_cont_eco_processed = 'fao_ecozones_continents_processed'
cont_eco_zip = 's3://gfw2-data/climate/carbon_model/fao_ecozones/fao_ecozones_fra_2000_continents_assigned_dissolved_FINAL_20180906.zip'
cont_eco_raw_dir = 's3://gfw2-data/climate/carbon_model/fao_ecozones/ecozone_continent/20181002/raw/'
cont_eco_dir = 's3://gfw2-data/climate/carbon_model/fao_ecozones/ecozone_continent/20181002/processed/'

# Number of gain years for non-mangrove natural forests
pattern_gain_year_count_natrl_forest = 'gain_year_count_natural_forest'
gain_year_count_natrl_forest_dir = 's3://gfw2-data/climate/carbon_model/gain_year_count_natural_forest/20181031/'

# Number of gain years for mangroves
pattern_gain_year_count_mangrove = 'gain_year_count_mangrove'
gain_year_count_mangrove_dir = 's3://gfw2-data/climate/carbon_model/gain_year_count_mangrove/20181031/'

# Forest age category tiles
pattern_age_cat_natrl_forest = 'forest_age_category_natural_forest'
age_cat_natrl_forest_dir = 's3://gfw2-data/climate/carbon_model/forest_age_category_natural_forest/20180921/'


# Annual aboveground biomass gain rate for non-mangrove natural forests
pattern_annual_gain_AGB_natrl_forest = 'annual_gain_rate_AGB_t_ha_natural_forest'
annual_gain_AGB_natrl_forest_dir = 's3://gfw2-data/climate/carbon_model/annual_gain_rate_AGB_natural_forest/20181102/'

# Annual aboveground biomass gain rate for mangroves
pattern_annual_gain_AGB_mangrove = 'annual_gain_rate_AGB_t_ha_mangrove'
annual_gain_AGB_mangrove_dir = 's3://gfw2-data/climate/carbon_model/annual_gain_rate_AGB_mangrove/20181102/'

# Annual belowground biomass gain rate for non-mangrove natural forests
pattern_annual_gain_BGB_natrl_forest = 'annual_gain_rate_BGB_t_ha_natural_forest'
annual_gain_BGB_natrl_forest_dir = 's3://gfw2-data/climate/carbon_model/annual_gain_rate_BGB_natural_forest/20181102/'

# Annual belowground biomass gain rate for mangroves
pattern_annual_gain_BGB_mangrove = 'annual_gain_rate_BGB_t_ha_mangrove'
annual_gain_BGB_mangrove_dir = 's3://gfw2-data/climate/carbon_model/annual_gain_rate_BGB_mangrove/20181102/'


# Cumulative aboveground gain for natural forests
pattern_cumul_gain_AGC_natrl_forest = 'cumul_gain_AGC_t_ha_natural_forest_2001_15'
cumul_gain_AGC_natrl_forest_dir = 's3://gfw2-data/climate/carbon_model/cumulative_gain_AGC_natural_forest/20181104/'

# Cumulative aboveground gain for mangroves
pattern_cumul_gain_AGC_mangrove = 'cumul_gain_AGC_t_ha_mangrove_2001_15'
cumul_gain_AGC_mangrove_dir = 's3://gfw2-data/climate/carbon_model/cumulative_gain_AGC_mangrove/20181102/'

# Cumulative aboveground gain for natural forests
pattern_cumul_gain_BGC_natrl_forest = 'cumul_gain_BGC_t_ha_natural_forest_2001_15'
cumul_gain_BGC_natrl_forest_dir = 's3://gfw2-data/climate/carbon_model/cumulative_gain_BGC_natural_forest/20181104/'

# Cumulative aboveground gain for mangroves
pattern_cumul_gain_BGC_mangrove = 'cumul_gain_BGC_t_ha_mangrove_2001_15'
cumul_gain_BGC_mangrove_dir = 's3://gfw2-data/climate/carbon_model/cumulative_gain_BGC_mangrove/20181102/'


# Annual aboveground gain rate for all forest types
pattern_annual_gain_combo = 'annual_gain_rate_AGB_BGB_t_ha_all_forest_types'
annual_gain_combo_dir = 's3://gfw2-data/climate/carbon_model/annual_gain_rate_all_forest_types/20181105/'

# Cumulative gain for all forest types
pattern_cumul_gain_combo = 'cumul_gain_AGC_BGC_t_ha_all_forest_types_2001_15'
cumul_gain_combo_dir = 's3://gfw2-data/climate/carbon_model/cumulative_gain_all_forest_types/20181105/'

# Net emissions for all forest types and all carbon pools
pattern_net_emis = 'net_emis_t_CO2_ha_all_forest_types_all_drivers_2001_15'
net_emis_dir = 's3://gfw2-data/climate/carbon_model/net_emissions_all_forest_types_all_drivers/20181107/'


# Tile statistics output txt file core name
tile_stats = 'tile_stats'