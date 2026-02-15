import io
import os
import requests
import pandas as pd
from google.cloud import storage

"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'
# Retrieve the bucketname or use the default value
BUCKET = os.environ.get("GCP_GCS_BUCKET", "week4_taxi_datasets")

dtype = {
    "VendorID": "Int64",
    "lpep_pickup_datetime": "string",
    "lpep_dropoff_datetime": "string",
    "store_and_fwd_flag": "string",
    "RatecodeID": "Int64",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "ehail_fee": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "payment_type": "Int64",
    "trip_type": "Int64",
    "congestion_surcharge": "float64"
}


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    #storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    #storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client(project='dtc-de-course-484501')
    bucket = client.bucket(bucket)
    # Create a blob (file) object within the bucket with the specified path/name
    blob = bucket.blob(object_name)
    # Upload the local file to GCS at the blob location
    blob.upload_from_filename(local_file)


def web_to_gcs(year, service):
    # Create Downloads directory if it doesn't exist
    os.makedirs('Downloads', exist_ok=True)
    
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        base_file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
        file_name = f"Downloads/{base_file_name}"

        # download it using requests via a pandas df
        request_url = f"{init_url}{service}/{base_file_name}"
        # Send HTTP GET request to download the file from the URL
        r = requests.get(request_url)
        # Open a new file & write the downloaded content to it
        open(file_name, 'wb').write(r.content)
        print(f"Local: {file_name}")

        # read it back into a parquet file
        #df = pd.read_csv(file_name, dtype=dtype, compression='gzip')
        
        chunk_size = 1000000  # Adjust based on your RAM
        chunks = []

        for chunk in pd.read_csv(file_name, compression='gzip', chunksize=chunk_size):
            chunks.append(chunk)
            print(f"Read {len(chunks)} chunks...")

        df = pd.concat(chunks, ignore_index=True)
        
        file_name = file_name.replace('.csv.gz', '.parquet')
        df.to_parquet(file_name, engine='pyarrow')
        print(f"Parquet: {file_name}")

        # upload it to gcs 
        upload_to_gcs(BUCKET, f"{service}/{base_file_name.replace('.csv.gz', '.parquet')}", file_name)
        print(f"GCS: {service}/{file_name}")


#web_to_gcs('2019', 'green')
#web_to_gcs('2020', 'green')
#web_to_gcs('2019', 'yellow')
web_to_gcs('2019', 'fhv')