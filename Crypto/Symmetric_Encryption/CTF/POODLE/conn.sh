#!/bin/bash

socat tcp-listen:1234,fork,reuseaddr EXEC:"python ./server.py"
