coverage run --source=src/. -m pytest --ignore=tests/integration/ --junitxml=output/tests/unit/test_report.xml
coverage report
coverage xml -o code_coverage.xml