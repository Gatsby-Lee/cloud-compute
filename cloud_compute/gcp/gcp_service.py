"""
:author: Gatsby Lee
:since: 2019-08-13
"""

import googleapiclient.discovery

# gcp_helper > gcloud_api_factory > gcloud_api_playground > google_api_playground


def get_compute_engine_service():
    compute_engine_service = googleapiclient.discovery.build(
        'compute', 'v1', cache_discovery=False)
    return compute_engine_service


__all__ = (
    'get_compute_engine_service',
)
