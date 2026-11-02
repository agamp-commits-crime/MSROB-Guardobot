#!/usr/bin/env bash
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

export GZ_SIM_RESOURCE_PATH="$PROJECT_DIR/models:$PROJECT_DIR/models/exhibits${GZ_SIM_RESOURCE_PATH:+:$GZ_SIM_RESOURCE_PATH}"

gz sim -r "$PROJECT_DIR/worlds/museum_world.sdf"
