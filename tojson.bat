@echo off

if [%1]==[] (
    echo Yaml file is required
    exit 1
) else (
    if exist %CD%\%1 (
        python %~dp0ymltojson.py %CD%\%1
    ) else (
        echo not exist
    )
)

