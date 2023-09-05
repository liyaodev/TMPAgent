# -*- coding: utf-8 -*-

import re
import json
import time
import copy
import requests
from retrying import retry

def retry_if_result_error(result):
    return not result

@retry(retry_on_result=retry_if_result_error, stop_max_attempt_number=3, stop_max_delay=6000, wait_random_min=100, wait_random_max=500)
def post_url(url, body, headers={'Content-Type': 'application/json'}):
    return requests.post(url, json=body, headers=headers).json()
