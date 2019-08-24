Cloud Compute
=============

Simple API creating Google ComputeEngine or AWS EC2


SSH Connect to Instance
=======================

SSH Connect with gcloud
-----------------------

ref: https://cloud.google.com/compute/docs/instances/connecting-to-instance

.. code-block:: bash

    # gcloud compute ssh --project [PROJECT_ID] --zone [ZONE] [INSTANCE_NAME]
    gcloud compute ssh

SSH Connect with OS Login
-------------------------

ref:

* https://cloud.google.com/compute/docs/instances/connecting-advanced
* https://cloud.google.com/compute/docs/instances/managing-instance-access


Set enable-oslogin as key, TRUE as value

* Project-wide: Compute Engine > Metadata
* Instance: Add metadata either while creating or running instance



SSH Connect from Browser
--------------------

ref: https://cloud.google.com/compute/docs/ssh-in-browser


Source IP addresses for browser-based SSH sessions are dynamically allocated by GCP Console
and can vary from session to session.

For the feature to work, you must allow connections either from any IP address
or from Google's IP address range which you can retrieve using `public SPF records <https://support.google.com/a/answer/60764>`_


.. code-block:: bash

    nslookup -q=TXT _netblocks.google.com 8.8.8.8
    nslookup -q=TXT _netblocks2.google.com 8.8.8.8
    nslookup -q=TXT _netblocks3.google.com 8.8.8.8


Troubleshooting
================

Unable to Launch Instance
-------------------------

The user does not have access to service account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* service account needs new Role: `Service Account > Servic Account User`



References
==========

Disks
-----

* https://cloud.google.com/compute/docs/disks/
* https://cloud.google.com/compute/docs/disks/performance

OS Images
---------

Images with/without Shielded VM support

* https://cloud.google.com/compute/docs/images
* https://cloud.google.com/container-optimized-os/docs/release-notes

Google Python API Client References
-----------------------------------

* https://cloud.google.com/compute/docs/api/libraries
* https://github.com/googleapis/google-api-python-client
* https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/compute/api
* https://cloud.google.com/compute/docs/instances/create-start-instance
* https://cloud.google.com/compute/docs/reference/rest/v1/instances/insert


libcloud References
-------------------

* https://libcloud.apache.org/
* https://libcloud.readthedocs.io/en/latest/compute/drivers/gce.html
* http://libcloud.apache.org/blog/2014/02/18/libcloud-0-14-and-google-cloud-platform.html
* https://github.com/apache/libcloud/blob/trunk/demos/gce_demo.py


Google API Discovery Service
----------------------------

* https://developers.google.com/discovery/
* https://developers.google.com/apis-explorer/#p/
