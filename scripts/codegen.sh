#!/usr/bin/env bash

#set -u
set -e

if [ -n "$PRODUCT" ]; then
  ucloud-model sync --lang python --product "$PRODUCT"
  ucloud-model sdk apis --type public --product "$PRODUCT" --lang python --template "$U_MODEL_HOME"/providers/python/templates/scripts-api.tpl --output scripts/gen-apis.sh
  bash ./scripts/gen-apis.sh
fi

if [ -n "$TEST" ]; then
  IFS=',' read -ra TL <<< "$TEST"
  for i in "${TL[@]}"; do
    ucloud-model sdk test --name "$i" --lang python --template "$U_MODEL_HOME"/providers/python/templates/testing.tpl --output tests/test_services/test_set_"$i".py
  done
fi
