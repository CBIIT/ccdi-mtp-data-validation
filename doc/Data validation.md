# Data validation

We ingest data come from public open targets and Chop.  We would like to make sure the data presented in our MTP site is what we expected.  The document here summarized the data loading steps and when data validation should happen. 

![](001.png)
# Data from public OT

Public OT has data release in every 2~3 months.  Ideally, we will follow the OT release to integrate with new OT data. Before we combine the CHoP data with public OT data, we need to make sure the data we download from OT’s FTP is what they used in the current release. 
## **DV1**
Data completeness validation 1 aims to make sure the data download from public OT is completed and is the same data files used in current public OT.  That’s critical as later we will add on ChoP’s data, if this step is not right, it will cause data is not presented or incorrect data shown on page. It would be time consuming to find out the root cause. 

1. Make sure data downloaded is completed. 

Public OT provides checksum, We use 

•	To verify MD5 checksums, type:

eg.  md5sum -c md5sums.txt

•	To verify SHA checksums, type the name of the command for the hashing algorithm you want to use. For example, to verify a SHA-256 checksum, use the sha256sum command. To verify a SHA-512 checksum, you would type the following command:

eg.  sha512sum -c sha512sums.txt

1. Make sure data uploaded is completed. 

The data files contain lines of record, each record presented as one document in the database. 

Counting the lines of records gives stats number how many document should be stored in the database. 

Linux can use wc -l to count the line of records. 

1. Make sure data presented on GUI is same as public OT. 

Visual testing cypress with applitools, tools will take screenshot of both local app and public OT, , the tool will do the comparison to find the different.  We could use this tool to validate the data in a large scale .

## **DV2**
Validate the “quality “ of ChoP data. That part are depends on Zack and Cindy’s expertise to manually check if the data from CHoP is what we expected.

## **DV3**
` `Once **DV1** and **DV2** both passed, then we can combine public OT’s data with ChoP. 

Add ChoP data into database. 

Update the codebase (backend) if needed. 

Perform **DV3**

**Dev3** amins to test “ Data loading completeness”, to make sure both ChoP and OT data are loaded corrected and show the right data on the GUI. 

Data analyst will provide the testing criteria and QA can use that as input to the automation script to validate the data on the GUI. 

**Dev3** should be fully automated as we will use it in regression test and integration testing. Ideally, will integrated with our CICD pipeline. 



