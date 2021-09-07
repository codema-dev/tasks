# tasks
A collection of Python helper functions for use in ETL pipelines

## setup

```bash
pip install git+https://github.com/codema-dev/tasks
```

## usage

### ploomber yaml

download via http(s) or s3
> for s3 try `url: s3://codema-dev/dublin_small_area_boundaries_in_routing_keys.gpkg`
> **note:** s3 searches your environmental variables for your credentials, you must set these in a separate task
```yaml
tasks:
- source: codema_dev_tasks.requests.fetch_file
  name: download_dublin_small_area_boundaries
  params:
    url: https://codema-dev.s3.eu-west-1.amazonaws.com/dublin_small_area_boundaries_in_routing_keys.gpkg
  product: data/external/dublin_small_area_boundaries_in_routing_keys.gpkg
```

file exists?
> i.e. depend on raw data that must be uploaded manually
```yaml
 - source: download.check_file_exists
   name: check_urban_atlas_is_uploaded
   params:
     filepath: data/raw/Urban Atlas
   product: data/raw/Urban Atlas
```
