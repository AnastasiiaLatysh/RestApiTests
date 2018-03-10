#!/usr/bin/env bash
py.test --alluredir $PWD/XMLreport/
allure generate $PWD/XMLreport/ -o $PWD/HTMLreport/ --clean
