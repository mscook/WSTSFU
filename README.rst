WSTSFU
======

.. image:: https://travis-ci.org/mscook/WSTSFU.png?branch=master
        :target: https://travis-ci.org/mscook/WSTSFU
|
.. image:: https://landscape.io/github/mscook/WSTSFU/master/landscape.png
        :target: https://landscape.io/github/mscook/WSTSFU/master
        :alt: Code Health

Work in progress:
    * `WSTSFU documentation`_


WorkSheet To Something Fucking Useful =  WSTSFU. Free clinical metadata
relating to NGS experiments from Excel documents.


Too often the clinical metadata relating to NGS experiments comes in the form  
of a Microsoft Excel spreadsheet. This increasingly frustrates the 
Bioinformatician.

*This tool may be a useful joke*

WSTSFU is a simple wrapper around csvkit.


Requirements
------------

**Python 2.7** (no support for 3 at this stage)
    
Python modules:
    * csvkit
    * envoy


Usage
-----

Something like this::


    $ python WSTSFU.py -h
    
    Usage: WSTSFU.py [-h] [--version] [-e EXCLUDE] [-b] [-s SEQID_HEADER] file strainID_header
                     
         Free clinical metadata relating to NGS experiments from Excel documents
         
        positional arguments:
            file                  Full path to the metadata file
            strainID_header       The header containing the StrainID
             
        optional arguments:
            -h, --help            show this help message and exit
            --version             show program's version number and exit
            -e EXCLUDE, --exclude EXCLUDE Exclude these headers
            -b, --banzai          Generate a pre_analystics file for Banzai
            -s SEQID_HEADER, --seqID_header SEQID_HEADER The header containing the sequencingID [required with -b]
                                                                                               
    Licence: ECL 2.0 by Mitchell Stanton-Cook <m.stantoncook@gmail.com>


Example/Tutorial/Quickstart
---------------------------

Most often the metadata such as isolate data, isolate location, typing 
information etc comes to the Bioinformatician in the form of a Microsoft 
Excel document. WSTSFU takes a Microsoft Excel document and converts it to 
JSON. 

WSTSFU also:
    * renames a given column label to StrainID
    * provides information on the schema that could be loaded into a database

Optionally, WSTSFU can:
    * exclude certain columns from the resultant JSON,
    * generate a pre-analytics file required in the Banzai pipeline (for 
      strain renaming)

The following Quickstart shows you how to achieve each of the tasks described.

**xlsx to JSON:**

Here vial_label is remapped to StrainID::

    python WSTSFU.py ~/Documents/isolates_for_sequencing_032013.xlsx vial_label
    
    Have metadata on 99 strains 

    JSON Schema:
    +-----------------------------+-----------------------------+
    | Key                         | Value (type)                |
    +=============================+=============================+
    | PFGE_type                   | string or None              |
    +-----------------------------+-----------------------------+
    | Sampled                     | string or None              |
    +-----------------------------+-----------------------------+
    | stx2                        | string or None              |
    +-----------------------------+-----------------------------+
    | AHD                         | string or None              |
    +-----------------------------+-----------------------------+
    | Farm                        | string or None              |
    +-----------------------------+-----------------------------+
    | stx2c                       | string or None              |
    +-----------------------------+-----------------------------+
    | Phage Type                  | string or None              |
    +-----------------------------+-----------------------------+
    | StrainID                    | string or None              |
    +-----------------------------+-----------------------------+
    | stx1                        | string or None              |
    +-----------------------------+-----------------------------+
    | year                        | string or None              |
    +-----------------------------+-----------------------------+
    | stx2_old                    | string or None              |
    +-----------------------------+-----------------------------+
    | Ehcount                     | string or None              |
    +-----------------------------+-----------------------------+
    | sequenced_before            | string or None              |
    +-----------------------------+-----------------------------+
    | IPRAVE isolate              | string or None              |
    +-----------------------------+-----------------------------+

    Please find your JSON file at: /home/mscook/Documents/isolates_for_sequencing_032013.xlsx.json


**xlsx to JSON excluding some columns**

Here we exclude columns labelled Farm, AHD, and Ehcount::

    python WSTSFU.py ~/Documents/isolates_for_sequencing_032013.xlsx vial_label -e 'Farm AHD Ehcount'
    Have metadata on 99 strains 

    JSON Schema:
    +-----------------------------+-----------------------------+
    | Key                         | Value (type)                |
    +=============================+=============================+
    | PFGE_type                   | string or None              |
    +-----------------------------+-----------------------------+
    | Sampled                     | string or None              |
    +-----------------------------+-----------------------------+
    | stx2                        | string or None              |
    +-----------------------------+-----------------------------+
    | stx2c                       | string or None              |
    +-----------------------------+-----------------------------+
    | Phage Type                  | string or None              |
    +-----------------------------+-----------------------------+
    | StrainID                    | string or None              |
    +-----------------------------+-----------------------------+
    | stx1                        | string or None              |
    +-----------------------------+-----------------------------+
    | year                        | string or None              |
    +-----------------------------+-----------------------------+
    | stx2_old                    | string or None              |
    +-----------------------------+-----------------------------+
    | sequenced_before            | string or None              |
    +-----------------------------+-----------------------------+
    | IPRAVE isolate              | string or None              |
    +-----------------------------+-----------------------------+

    Please find your JSON file at: /home/mscook/Documents/isolates_for_sequencing_032013.xlsx.json



.. _WSTSFU documentation: http://wstsfu.rtfd.org

