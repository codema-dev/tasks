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
