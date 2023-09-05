#!/bin/bash

if [ "${1-}" = "up" ]; then
    mkdir -p "${TMPAGENT_DIR:-.}/volumes/vscode-extensions"
    chmod -R 777 "${TMPAGENT_DIR:-.}/volumes"

    docker-compose -f ${TMPAGENT_DIR:-.}/docker-compose-devcontainer.yml up -d
fi

if [ "${1-}" = "down" ]; then
    docker-compose -f ${TMPAGENT_DIR:-.}/docker-compose-devcontainer.yml down
    rm -rf "${TMPAGENT_DIR:-.}/volumes"
fi
