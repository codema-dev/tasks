# tasks
A collection of Python helper functions for use in ETL pipelines

## setup

```bash
pip install git+https://github.com/codema-dev/tasks
```

## usage

### ploomber yaml

---

- download via **http(s)** or **s3**

> **note:** s3 searches your environmental variables for your credentials, you must set these in a separate task

```yaml
tasks:
- source: codema_dev_tasks.requests.fetch_file
  name: download_YOUR_FILENAME
  params:
    url: YOUR-URL
  product: YOUR-FILEPATH
```

| host        | use?                                  |
| ----------- | ------------------------------------- |
| **http(s)** | `url: s3://www.WEBSITE.com`           |
| **s3**      | `url: s3://BUCKET-NAME/OBJECT-NAME`   |

---

- file exists?

> i.e. depend on raw data that must be uploaded manually

```yaml
 - source: download.check_file_exists
   name: check_YOUR_FILEPATH_is_uploaded
   params:
     filepath: YOUR-FILEPATH
   product: YOUR-FILEPATH
```
