"""
This module contains a simple reading dataset

Author: Fabio
Date: 13th of Jan, 2022
"""

import pandas as pd
import logging
import numpy as np


# define log
log=logging.getLogger(__name__)


def read_csv(pth_csv):
    """
        This method read a csv file

        Args:
            pth_csv (str): path of the file

        Output:
            df (pandas Dataframe)
    """
    try:
        log.info('read_csv')

        df=pd.read_csv(pth_csv)

        return df

    except Exception as err:
        log.exception(err)
        raise

def get_descriptive_stat_numeric(df):
    """
    This method outputs the descriptive stats for each numeric column

    Args:
        df (pandas Dataframe)
    
    Outut:
        df_stats (pandas Dataframe): dataframe containing the descriptive stats
    
    """
    try:
        log.info('read_csv')

        df_stats=df.describe(include=np.number)

        return df_stats


    
    except Exception as err:
        log.exception(err)
        raise

def main():
    """
    This is the entrypoint
    """
    try:
        log.info('read_csv')

        df=read_csv('data/iris.csv')

        df_stats=get_descriptive_stat_numeric(df)

        print(df_stats)

    except Exception as err:
        log.exception(err)   


if __name__=='__main__':
    main()