"""
Use AWSume in Jupyter.
"""

import os
from typing import Optional

from awsume.awsumepy import awsume


def jawsume(profile_name: str, mfa_token: Optional[str] = None) -> None:
    """
    Use AWSume in Jupyter.
    """
    if mfa_token is None:
        mfa_token = input()

    session = awsume(profile_name, mfa_token=mfa_token)
    credentials = session.awsume_credentials

    os.environ["AWS_ACCESS_KEY_ID"] = credentials.get("AccessKeyId")
    os.environ["AWS_SECRET_ACCESS_KEY"] = credentials.get("SecretAccessKey")
    os.environ["AWS_SESSION_TOKEN"] = credentials.get("SessionToken")
    os.environ["AWS_REGION"] = credentials.get("Region")
    os.environ["AWSUME_PROFILE"] = profile_name
    os.environ["AWSUME_EXPIRATION"] = (
        credentials["Expiration"].strftime("%Y-%m-%dT%H:%M:%S")
        if "Expiration" in credentials
        else None
    )
