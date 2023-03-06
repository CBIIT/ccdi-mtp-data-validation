# where the ETL output prefix is located as inside it should find each step output
export PREFIX=
# empty prefix release. If you specify it it will be simply prefixed like "20.11_"...
export INDEX_SETTINGS=
# default ES endpoint

export ES="localhost:9200"


./load_targets.sh
./load_pcdn.sh
./load_diseases.sh
./load_disease_hpo.sh
./load_hpo.sh
./load_drugs.sh
./load_evidences.sh

./load_so.sh
./load_expression.sh
./load_mp.sh
./load_reactome.sh
./load_openfda_faers.sh
./load_interaction.sh
./load_interaction_evidence.sh

./load_evidences_aotf.sh
#echo "INDEX_SETTINGS different"
./load_search.sh
./load_known_drugs.sh
