#!/bin/bash


echo INPUT = $INPUT
echo INDEX_NAME = $INDEX_NAME

INDEX=$INDEX_NAME


number_of_doc=$(find $INPUT  -name *.json |xargs   wc -l  | awk '{sum+=$1}END{print sum}' )
echo $number_of_doc
echo $ES/$INDEX_NAME"/_count" 


curl_es=$(curl  --silent $ES/$INDEX_NAME"/_count")

echo $curl_es 

IFS=', ' read -r -a array <<< $curl_es

number_of_doc_es=$(echo "${array:9}")  

if [ "$number_of_doc" -eq "$number_of_doc_es" ]
  then
  echo "[GREEN]   $INDEX is GOOD."
else
  echo "[ERROR]   $INDEX's number does not match."
fi   


