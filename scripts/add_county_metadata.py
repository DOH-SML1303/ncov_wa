# add_county_metadata.py
# this script is meant to update the location in the metadata file with county references_metadata
# Doing so will enable sequences to appear by county on the map as well as in the Color By - Location feature

import pandas as pd

def read_files(nextstrain_metadata_file, county_metadata_file):
    """read in input files from snakemake"""
    nextstrain_metadata = pd.read_csv(nextstrain_metadata_file)
    county_metadata = pd.read_csv(county_metadata_file)
    return nextstrain_metadata, county_metadata

def rename_col(county_metadata):
    """rename county metadata columns to match nextstrain metadata """
    county_metadata = county_metadata.rename(columns={
        'SEQUENCE_GISAID_STRAIN' : 'strain',
        'COUNTY_NAME': 'location'
        })
    return county_metadata

def convert_to_str(datafames_columns):
    """Convert all values in the specified col"""
        for column in columns:
            df[column] = df[column].astype(str)
        return dfs

def processing_step(nextstrain_metadata, county_metadata):
    """Convert column values to strings, add 'County' to values, and create a location dictionary"""
    convert_to_str([nextstrain_metadata, county_metadata], ['strain', 'location'])
    county_metadata['location'] = county_metadata['location'] + 'County'
    location_dict = county_metadata.set_index('strain')['location'].to_dict()
    return nextstrain_metadata, county_metadata, location_dict

def fill_missing_values(df, columns_defaults):
    """Fills in region, county, and division columns"""

def main(nextstrain_metadata_file, county_metadata_file):
    nextstrain_metadata, county_metadata = read_files(nextstrain_metadata_file, county_metadata_file)
    county_metadata = rename_col(county_metadata)
    nextstrain_metadata, county_metadata, location_dict = processing_step(nextstrain_metadata, county_metadata)
