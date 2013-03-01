#!/bin/sh
mkdir -p docs/imgs
sfood auto_version > /tmp/sfood.deps

sfood-graph /tmp/sfood.deps | dot -Tpng -odocs/imgs/dependencies.png
