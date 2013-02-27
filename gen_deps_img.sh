#!/bin/sh
mkdir -p docs/imgs
sfood increment_version.py auto_version > /tmp/sfood.deps

sfood-graph /tmp/sfood.deps | dot -Tpng -odocs/imgs/dependencies.png
