# where the ETL output prefix is located as inside it should find each step output
export PREFIX="/Users/cheny39/Documents/work/22.09/json"

# default ES endpoint
export ES="localhost:9200"

./load_cancerbiomarker.sh
./load_diseases.sh
./load_disease_hpo.sh
./load_drugs.sh
./load_eco.sh
./load_evidences.sh
./load_evidences_aotf.sh
./load_expression.sh
./load_hpo.sh
./load_interaction.sh
./load_interaction_evidence.sh
./load_mp.sh
./load_openfda_faers.sh
./load_otars.sh
./load_reactome.sh
./load_so.sh
./load_targets.sh
./load_known_drugs.sh
./load_search.sh
