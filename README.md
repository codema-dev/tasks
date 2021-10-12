# tasks

[![PyPI version shields.io](https://img.shields.io/pypi/v/codema-dev-tasks.svg)](https://pypi.python.org/pypi/codema-dev-tasks/)
[![PyPI license](https://img.shields.io/pypi/l/codema-dev-tasks.svg)](https://pypi.python.org/pypi/codema-dev-tasks/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/codema-dev-tasks.svg)](https://pypi.python.org/pypi/codema-dev-tasks/)
[![PyPI status](https://img.shields.io/pypi/status/codema-dev-tasks.svg)](https://pypi.python.org/pypi/codema-dev-tasks/)

A collection of Python helper functions for use in ETL pipelines

## setup

```bash
pip install codema-dev-tasks
```

## usage

### ploomber yaml

---

#### download via **http(s)** or **s3**

```yaml
tasks:
- source: codema_dev_tasks.requests.fetch_file
  name: download_YOUR_FILENAME
  params:
    url: YOUR-URL
  product: YOUR-FILEPATH
```

| host | use? | note |
| --- | --- | --- |
| **http(s)** | `url: s3://www.WEBSITE.com` | -    |
| **s3** | `url: s3://BUCKET-NAME/OBJECT-NAME` | If the data is not public you must save your credentials as environmental variables in a `.env` file |

---

#### load environmental variables

Add a `.env` file with your credentials to your current working directory

```
MY_CREDENTIALS=*****
```

Load the `.env` file within the `fetch_file` task

```yaml
tasks:
  - source: codema_dev_tasks.requests.fetch_file
    params:
      url: YOUR-URL
      dotenv_path: "{{here}}/.env
    product: YOUR-FILEPATH
```
