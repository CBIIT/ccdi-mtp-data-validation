Data used during the DV3 step is held in this directory. 
Download data to local machine, but do not commit raw or external data to repo.


Data structure for reference:
Last updated 2022-11-02 ZD
.
└── data /
    ├── external/
    │   └── opentargets/platform/
    │       └── 22.04/
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
    │   ├── chopDataNavigationTable_22.09_v10.0.json 
    │   └── pmtl_v3.0.json
    └── raw/
        └── OpenPedCan_v10.0/
            ├── gene-level-cnv-consensus-annotated-mut-freq.jsonl.gz
            ├── gene-level-snv-consensus-annotated-mut-freq.jsonl.gz
            ├── variant-level-snv-consensus-annotated-mut-freq.jsonl.gz
            ├── putative-oncogene-fused-gene-freq.jsonl.gz
            ├── putative-oncogene-fusion-freq.jsonl.gz
            ├── long_n_tpm_mean_sd_quantile_gene_wise_zscore.jsonl.gz
            └── long_n_tpm_mean_sd_quantile_group_wise_zscore.jsonl.gz