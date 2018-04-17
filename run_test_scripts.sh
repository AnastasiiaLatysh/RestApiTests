#!/usr/bin/env bash
# TODO лучше класть в папку ./bin чтоб не засорять структуру проекта. В корне обычно и так очень много всего.
py.test --alluredir $PWD/XMLreport/
allure generate $PWD/XMLreport/ -o $PWD/HTMLreport/ --clean
