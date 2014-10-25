'''
Created on 23-Oct-2014

@author: Rahul

@summary: CSV serializer to save the required data onto disk in the CSV format.
'''
from __future__ import absolute_import
import csv
import datetime


def write(output_file, fields, rows):
    '''
        Writes the date into csv format.
        Rows will be a collection of dicts containing the data.
    '''
    with open(output_file, 'ab') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # Add the CSV file heading.
        writer.writerow({k: k for k in fields})
        # Save all the rows
        writer.writerows(rows)
