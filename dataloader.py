from google.cloud import bigquery

def get_traffic_data_by_date(date_string):
    client = bigquery.Client()

    query = f'''
    SELECT *
    from traffic-analysis-418408.taxi_availability.taxi_availability_cluster
    where date(timestamp, "Asia/Singapore") = '{date_string}'
    and cluster <> -1
    order by timestamp asc
    '''

    query_job = client.query(query)
    results = query_job.result()
    df = results.to_dataframe()
    df.timestamp = df.timestamp.dt.tz_convert('Asia/Singapore')
    df["cluster"] = df["cluster"].map(str)
    return df

def get_distinct_available_dates():
    client = bigquery.Client()
    query = f'''
    SELECT distinct date(timestamp, "Asia/Singapore") as dates
    from traffic-analysis-418408.taxi_availability.taxi_availability_cluster
    order by dates asc
    '''
    query_job = client.query(query)
    results = query_job.result()
    return results.to_dataframe()

#print(get_distinct_available_dates())