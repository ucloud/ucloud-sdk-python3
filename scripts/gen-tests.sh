#!/usr/bin/env bash

ucloud-model sdk test \
    --lang python3 \
    --template ../ucloud-api-model-v2/apisdk/lang/python/templates/testing.tpl \
    --output tests/test_services/test_set_220.py \
    --name 220
black tests/test_services/test_set_220.py
