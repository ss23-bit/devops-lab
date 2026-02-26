#!/bin/bash
echo "--- DevOps Lap Status ---"
echo "Date: $(date)"
echo "Directory $(pwd)"
echo "File in this folder $(ls | wc -l)"
echo "Memory usage $(free -h)"
echo "-------------------------"