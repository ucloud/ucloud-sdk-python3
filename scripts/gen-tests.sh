#!/usr/bin/env bash

ucloud-model sdk test \
    --lang python3 \
    --template ../ucloud-api-model-v2/apisdk/lang/python/templates/testing.tpl \
    --output tests/test_services/test_set_230.py \
    --name 230
black tests/test_services/test_set_230.py

ucloud-model sdk test \
    --lang python3 \
    --template ../ucloud-api-model-v2/apisdk/lang/python/templates/testing.tpl \
    --output tests/test_services/test_set_2301.py \
    --name 2301
black tests/test_services/test_set_2301.py
