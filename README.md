# tasks
A collection of Python helper functions for use in ETL pipelines

## setup

```bash
pip install git+https://github.com/codema-dev/tasks
```

## usage

### ploomber yaml

http(s)
```yaml
tasks:
- source: codema_dev_tasks.requests.fetch_file
    name: download_dublin_small_area_boundaries
    params:
      url: https://codema-dev.s3.eu-west-1.amazonaws.com/dublin_small_area_boundaries_in_routing_keys.gpkg
    product: data/external/dublin_small_area_boundaries_in_routing_keys.gpkg
```

s3
```yaml
 - source: download.fetch_s3_file
    name: download_small_areas
    params:
      bucket: codema-dev
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
