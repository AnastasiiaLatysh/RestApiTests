[SOURCE_DIRECTORY] = ../RestApiTests

1. To run test scripts please use next command in terminal in source directory:
py.test --alluredir [$directory-to-save-results]

2. To generate HTML report use next command in terminal:
allure generate [$directory-with-results/] -o [$directory-where-u-want-indexhtmlreport-to-be-generated/]

[$directory-with-results/] - is a directory where xml report was generated after executed command #1

[$directory-where-u-want-indexhtmlreport-to-be-generated/] - is a directory where you want to store HTML report

3. You can use bash script to run test scripts and generate HTML report. 
You need to execute following command in terminal in source directory.
Reports will be generated in 
[$source directory/XMLreport] for xml report
and 
[$source directory/HTMLreport] for html report.
Command:
sh run_test_scripts.sh
