#!/bin/bash
python3 upload_s3.py
python3 dio-live-wordcount-teste.py -r emr s3://<bucket-name>/datalake-dio/data/sherlock.txt --cloud-output-dir=s3://<bucket-name>/<dir-output-name>/ --cloud-tmp-dir=s3://<bucket-name>/<dir-temp-name>/
