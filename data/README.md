## DATA
Data used during the DV3 step is held in this directory.  
Manually download data from sources to local machine to run DV3, but do not commit raw or external data to repo.  
Control for this is found within `mtp-data-validation/.gitignore`

### Data sources:
#### External
Open Targets: http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/ 
#### Processed
Processed data can be stored within this repo, but may be generated elsewhere
#### Raw
OpenPedCan CHoP S3 bucket: https://s3.console.aws.amazon.com/s3/buckets/d3b-openaccess-us-east-1-prd-pbta?prefix=open-targets%2F&region=us-east-1#

Directory structure referenced in `verify_data_displayed_in_mtp.ipynb` is listed below.  

```
Last updated 2022-11-15 ZD
.
└── data /
    ├── external/
    │   └── opentargets/platform/
    │       └── {OT Version}/
    │           └── output/etl/json/
    │               ├── associationByOverallDirect/
    │               │   └── [jsonl files]
    │               ├── associationByOverallIndirect/
    │               │   └── [jsonl files]
    │               ├── diseases/
    │               │   └── [jsonl files]
    │               └── targets/
    │                   └── [jsonl files]
    ├── processed/
    │   ├── dv3_priority_tests/
    │   │   ├── diseases.csv
    │   │   ├── evidences.csv
    │   │   └── targets.csv
    │   ├── pcdn
    |   |   └── {OT Version}_{OpenPedCan Version}
    |   |       ├── chopDataNavigationTable.json
    |   |       └── jsonl
    |   |           └── [jsonl files]
    │   │     
    │   └── pmtl_v3.0.json
    └── raw/
        └── OpenPedCan_{version}/
            ├── gene-level-cnv-consensus-annotated-mut-freq.jsonl.gz
            ├── gene-level-snv-consensus-annotated-mut-freq.jsonl.gz
            ├── variant-level-snv-consensus-annotated-mut-freq.jsonl.gz
            ├── putative-oncogene-fused-gene-freq.jsonl.gz
            ├── putative-oncogene-fusion-freq.jsonl.gz
            ├── long_n_tpm_mean_sd_quantile_gene_wise_zscore.jsonl.gz
            └── long_n_tpm_mean_sd_quantile_group_wise_zscore.jsonl.gz
'''