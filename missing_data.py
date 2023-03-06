import glob
import json
from opensearchpy import OpenSearch

#es = OpenSearch(hosts=[{'host': "vpc-mtp-opensearch-qa-y4vflq7yz2zwwpwcxii6r75zza.us-east-1.es.amazonaws.com"}],use_ssl=True)
es = OpenSearch(
          hosts=[{'host': "vpc-mtp-opensearch-qa-y4vflq7yz2zwwpwcxii6r75zza.us-east-1.es.amazonaws.com",'port': 443}],
          http_compress=True,
          use_ssl=True,
          verify_certs=False,
          ssl_assert_hostname=False,
          ssl_show_warn=False,
         )

# Data Files path
Miss_Drug_FIle_PATH = '/Users/cheny39/Documents/work/22.04/output/miss_drug/*.json'
Miss_Evidence_Europepmc_FIle_PATH ='/Users/cheny39/Documents/work/22.04/output/miss_evidence/miss_europ/*.json'
Miss_Evidence_Impc_FIle_PATH='/Users/cheny39/Documents/work/22.04/output/miss_evidence/tmp/miss_impc/*.json'
Miss_Evidence_Ot_Genetics_Portal_FIle_PATH='/Users/cheny39/Documents/work/22.04/v_11_18_ot_22_04_chop_11_1/evidence/sourceId=ot_genetics_portal/*.json'
Miss_Evidences_Aotf_FIle_PATH='/Users/cheny39/Documents/work/22.04/output/AOTFElasticsearch/*.json'

count = 0


def hasDoc(index,body):
    global count
    count += 1
    print(count)
    if len(es.search(index=index, body=body)['hits']['hits']) == 0:
        return True
    return False;



def findMissingDrugData(export):
    files = glob.glob(Miss_Drug_FIle_PATH)
    #
    for f in files:
        # Opening JSON file
        file = open(f)
        lines = file.readlines()

        # list
        for line in lines:
            data = json.loads(line)
            if "status" in  data:
                body = {"query": {"bool": {"must": [{"match": {"drugId": data["drugId"]}}, {"match": {"targetId": data["targetId"]}},
                                         {"match": {"diseaseId":  data["diseaseId"]}},{"match": {"phase":  data["phase"]}},{"match": {"status.raw":  data["status"]}}]}}}
            else:
                body = {"query": {
                    "bool": {"must": [{"match": {"drugId": data["drugId"]}}, {"match": {"targetId": data["targetId"]}},
                                      {"match": {"diseaseId": data["diseaseId"]}}, {"match": {"phase": data["phase"]}},
                                      ]}}}

            if hasDoc("known_drugs",body):
                with open(export, "a") as outfile:
                    outfile.write(line)
        file.close()


def findMissingEvidences(path,index,export):
    files = glob.glob(path)
    
    for f in files:
        print(f)
        # Opening JSON file
        file = open(f)
        lines = file.readlines()
        # list
        for line in lines:
            data = json.loads(line)
            body = {"query": {
                    "bool": {"must": [{"match": {"id": data["id"]}}]}}}

            if hasDoc(index, body):
                with open(export, "a") as outfile:
                    outfile.write(line)
        file.close()



def findMissingAotf(path,index,export):
    files = glob.glob(path)
    #
    for f in files:
        # Opening JSON file
        file = open(f)
        lines = file.readlines()
        # list
        for line in lines:
            data = json.loads(line)
            body = {"query": {
                "bool": {"must": [{"match": {"target_id.raw": data["target_id"]}}, {"match": {"disease_id.raw": data["disease_id"]}},
                                  {"match": {"row_id.raw": data["row_id"]}}, {"match": {"datasource_id.raw": data["datasource_id"]}},
                                  {"match": {"datatype_id.raw": data["datatype_id"]}}]}}}

            if hasDoc(index, body):
                with open(export, "a") as outfile:
                    outfile.write(line)
        file.close()


basePath = '/Users/cheny39/Documents/work/22.04/miss'
#findMissingDrugData(basePath+"/drug.json")
print("evidence_datasource_europepmc")
# findMissingEvidences(Miss_Evidence_Europepmc_FIle_PATH,"evidence_datasource_europepmc",basePath+"/europepmc.json")
# print("evidence_datasource_impc")
# findMissingEvidences(Miss_Evidence_Impc_FIle_PATH,"evidence_datasource_impc",basePath+"/impc.json")
print("evidence_datasource_ot_genetics_portal")
findMissingEvidences(Miss_Evidence_Ot_Genetics_Portal_FIle_PATH,"evidence_datasource_ot_genetics_portal",basePath+"/aotf/ot.json")
# print("evidences_aotf")
# findMissingAotf(Miss_Evidences_Aotf_FIle_PATH,"evidences_aotf",basePath+"/aotf.json")
print("down")