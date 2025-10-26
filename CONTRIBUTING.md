# Contributing to `mybatop`

Thank you for the interest in contributing to mybatop! We welcome all people who want to contribute in healthy and constructive manner in our community.

This document will guide you to help you through the process of contributing to mybatop.

Whether you're a new contributor or a seasoned veteran, we hope these resources help you connect with the community.

## Tips to contribute mybatop

1. new contributors can use `good-first-issues` tag for contributing mybatop.
2. If you are going to contribute mybatop without any issues present, please raise a issue, to assign yourself and work for the contribution to mybatop.
3. Dont do any spam PR, you're PR won't be merged.
4. refer file structure given below, before starting to contribute.

## Steps to contribute mybatop

1. fork the repository to your account.
2. check for issues to contribute to
3. request to assign issue via github issue chat only.
4. After that, refer [Installation from Source](https://mybatop.web.app/docs/install-from-source) for installing mybatop in your laptop.
5. If you working on new feature (i.e., adding classes to report generation) then, create a notebook file (.ipynb)
file before converting to python code for easier analysis.
6. convert .ipynb to .py file using jupyter `nbconvert` command

```bash
jupyter nbconvert --to script <NOTEBOOK.ipynb>
```
7. move converted .py file to pythonscripts folder in src/mybatop/analyze
8. edit or create .sh files with respect to code logic.
9. Write a unit test case in tests/ folder, refer other unit test cases and write code accordingly.
10. Add the featured command to integration testing.
11. Also, make sure to do changes in `test-python.yml`, `integration-testing.yml`, to test changes automatically before merging PR.
12. push your code and make a Pull Request(PR) to `dev` branch with issue number.
13. Please make sure no Merge Conflicts should occur before raising a Pull Request.

## How to make Unit testing

1. Go to `tests/` folder.
2. create a test file with `test-<FEATURE_NAME>.py` as your test file name format.
3. write test cases using Unittest module.
4. put your expected output test files in `test_files/outputs/` folder, and write your test cases accordingly.
5. Run your test cases using below command.
```bash
python3 -m unittest test-<FEATURE_NAME>.py
```
6. Check if all test cases were passed.
7. If all test cases were passed, make sure to add a step in `test-python.yml`.

## Integration testing (Under Development)

1. Go to `integration-testing.yml` under .github/workflows directory.
2. Add a new feature command (i.e., if the command not present in steps in integration-testing.yml), as a new step.
3. Make a PR, if integration-testing works successfully in your repository.

## File Structure

```text
mybatop
├── tests
│   ├── test_userdetails.py
│   ├── test_tech_spec.py
│   ├── test_files
│   │   └── outputs
│   │       ├── no-low-power
│   │       │   ├── xml
│   │       │   │   ├── tech_spec.xml
│   │       │   │   ├── recent_usage.xml
│   │       │   │   ├── cycle_count.xml
│   │       │   │   ├── battery_health.xml
│   │       │   │   ├── battery_activity.xml
│   │       │   │   ├── batcaphis.xml
│   │       │   │   └── Average_capacity.xml
│   │       │   ├── json
│   │       │   │   ├── tech_spec.json
│   │       │   │   ├── recent_usage.json
│   │       │   │   ├── cycle_counts.json
│   │       │   │   ├── battery_health.json
│   │       │   │   ├── battery_activity.json
│   │       │   │   ├── batcaphis.json
│   │       │   │   └── average_capacity.json
│   │       │   ├── html
│   │       │   │   ├── g.html
│   │       │   │   ├── d.html
│   │       │   │   ├── cycle_count.html
│   │       │   │   ├── b.html
│   │       │   │   ├── battery_health.html
│   │       │   │   ├── Average_capacity.html
│   │       │   │   ├── a.html
│   │       │   │   └── a0.html
│   │       │   ├── details.csv
│   │       │   ├── data.csv
│   │       │   ├── csv
│   │       │   │   ├── tech_spec.csv
│   │       │   │   ├── recent_usage.csv
│   │       │   │   ├── cycle_count.csv
│   │       │   │   ├── battery_health.csv
│   │       │   │   ├── battery_activity.csv
│   │       │   │   ├── batcaphis.csv
│   │       │   │   └── Average_capacity.csv
│   │       │   └── batusageact.csv
│   │       └── low-power
│   │           ├── xml
│   │           │   ├── tech_spec.xml
│   │           │   ├── recent_usage.xml
│   │           │   ├── cycle_count.xml
│   │           │   ├── battery_health.xml
│   │           │   ├── battery_activity.xml
│   │           │   ├── batcaphis.xml
│   │           │   └── Average_capacity.xml
│   │           ├── json
│   │           │   ├── tech_spec.json
│   │           │   ├── recent_usage.json
│   │           │   ├── cycle_counts.json
│   │           │   ├── battery_health.json
│   │           │   ├── battery_activity.json
│   │           │   ├── batcaphis.json
│   │           │   └── average_capacity.json
│   │           ├── html
│   │           │   ├── g.html
│   │           │   ├── d.html
│   │           │   ├── cycle_count.html
│   │           │   ├── b.html
│   │           │   ├── battery_health.html
│   │           │   ├── Average_capacity.html
│   │           │   ├── a.html
│   │           │   └── a0.html
│   │           ├── details.csv
│   │           ├── data.csv
│   │           ├── csv
│   │           │   ├── tech_spec.csv
│   │           │   ├── recent_usage.csv
│   │           │   ├── cycle_count.csv
│   │           │   ├── battery_health.csv
│   │           │   ├── battery_activity.csv
│   │           │   ├── batcaphis.csv
│   │           │   └── Average_capacity.csv
│   │           └── batusageact.csv
│   ├── test_dchar.py
│   ├── test_cycle_count.py
│   ├── test_battery_health.py
│   ├── test_battery_activity.py
│   ├── test_batcaphis.py
│   ├── test_analyzers.py
│   ├── __pycache__
│   │   ├── test_analyzers.cpython-313.pyc
│   │   └── __init__.cpython-313.pyc
│   ├── integration_testing
│   │   ├── installation.sh
│   │   ├── inputs
│   │   │   └── uevent
│   │   └── containers
│   │       ├── ubuntu
│   │       ├── fedora
│   │       └── archlinux
│   └── __init__.py
├── src
│   └── mybatop
│       ├── scripts
│       │   ├── runscript
│       │   │   ├── mybatop
│       │   │   └── help.txt
│       │   ├── inserts
│       │   │   ├── insert_suspended.sh
│       │   │   ├── insert_status.sh
│       │   │   ├── insert_lowpower_status.sh
│       │   │   ├── insert_lowpower.sh
│       │   │   └── insert_active.sh
│       │   ├── header.sh
│       │   └── contents
│       │       ├── content_suspended.sh
│       │       ├── content_lowpower.sh
│       │       └── content_active.sh
│       ├── generate_data
│       │   ├── generate_xml.py
│       │   ├── generate_json.py
│       │   └── generate_csv.sh
│       ├── filesystemd
│       │   ├── mybatop-status.service
│       │   ├── mybatop-startup.service
│       │   ├── mybatop-shutdown.service
│       │   └── mybatop-lowpower.service
│       └── analyze
│           ├── tail.txt
│           ├── pythonscripts
│           │   ├── userdetails.py
│           │   ├── tech_spec.py
│           │   ├── dchar.py
│           │   ├── cycle_counts.py
│           │   ├── clean_dataset.py
│           │   ├── battery_health.py
│           │   ├── battery_activity.py
│           │   ├── batcaphis.py
│           │   └── analyzers.py
│           ├── head.txt
│           ├── generate-xml.sh
│           ├── generate-json.sh
│           ├── generate-html.sh
│           ├── generate_classes.sh
│           └── fetchuserdetails.sh
├── README.md
├── logo.svg
├── LICENSE
├── debug
│   ├── useranalyze.ipynb
│   ├── tech_spec.ipynb
│   ├── dchar.ipynb
│   ├── cycle_count.ipynb
│   ├── clean_dataframe.ipynb
│   ├── battery_health.ipynb
│   ├── battery-activity.ipynb
│   ├── batlife-est.ipynb
│   ├── batcaphis.ipynb
│   └── analyzers.ipynb
├── CONTRIBUTING.md
└── build
    ├── mybatop.spec
    ├── Debian
    │   ├── prerm
    │   ├── postrm
    │   ├── postinst
    │   └── control
    └── Arch
        ├── PKGBUILD
        └── mybatop.install
```

- `src` - Source folder where source code is present.
- `tests` - test folder
- `build` - folder for building packages for debian, fedora and archlinux.
- `debug` - list of .ipynb files before adding to production.

### Good luck! for contributing to mybatop.