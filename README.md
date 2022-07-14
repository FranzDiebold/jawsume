# JAWSume

[![PyPi](https://img.shields.io/pypi/v/jawsume)](https://pypi.org/project/jawsume/)
[![CI/CD](https://github.com/FranzDiebold/jawsume/actions/workflows/ci.yml/badge.svg)](https://github.com/FranzDiebold/jawsume/actions/workflows/ci.yml)

Use [AWSume](https://awsu.me/) in [Jupyter](https://jupyter.org/) to access [AWS](https://aws.amazon.com/) resources.

## Installation

```bash
$ pip install jawsume
```

## Usage

```python
from jawsume import jawsume

jawsume("<profile-name>")
```

You will be prompted for the MFA token.

Just like [AWSume](https://awsu.me/), this will set the following environment variables:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`
- `AWS_REGION`
- `AWSUME_PROFILE`
- `AWSUME_EXPIRATION`

### Non-interactive mode

You can also directly pass the MFA code:

```python
jawsume("<profile-name>", "<mfa-token>")
```

### What can I do then?

You can then for instance read [Apache Parquet](https://parquet.apache.org/) files from [Amazon S3](https://aws.amazon.com/s3/).

```python
import pandas as pd

df = pd.read_parquet("s3://<bucket-name>/<path-name>.parquet/")
```
