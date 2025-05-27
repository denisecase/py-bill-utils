# py-bill-utils

[![Uses Zig](https://img.shields.io/badge/Uses-Zig-ec912d?logo=zig&logoColor=white&style=flat-square)](https://ziglang.org)

> Python project for analyzing U.S. legislative bills. Incorporates high-performance Zig utils for speedy processing.

## Zig-Enhanced Python Project

This project integrates Zig executables for quickly analyzing U.S. legislative bills. 
This project uses six Zig CLI tools:

| Tool                | Description                                           |
|---------------------|-------------------------------------------------------|
| `clean_bill`        | Cleans bill text (removes line numbers, whitespace)   |
| `extract_amendments`| Extracts amendments                                   |
| `extract_headings`  | Extracts section headers (`TITLE`, `SEC.`)            |
| `extract_money`     | Extracts funding amounts (e.g., `$5,000,000`)         |
| `filter_keywords`   | Filters lines by keyword (listed in keywords.txt)     |
| `split_sections`    | Splits full bill into files by section    

## Add Bill Data

Research bills:

- [Congress.gov](https://www.congress.gov/)
  - [2025-hconres0014](https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/14)

Create a data/billname folder (e.g. data/2025-hconres0014/) and using the website, add:
  - bill.txt - paste the TXT version of the bill
  - amendments.csv - paste this from the Congress.gov site
  - keywords.txt - list keywords for that bill (and amendments)

## Development: Python Workflow

See [pro-analytics-01](https://github.com/denisecase/pro-analytics-01/) for recommended workflow for a professional Python project.

## Development: Python Dependencies

Create virtual environment (modify if not using Windows PowerShell):

```shell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt --timeout 100
```

## Development: Zig Dependencies

List required Zig executables in `requirements-zig.txt`. Install them into `zig-out` with:

```shell
py zig-install-requirements.py
```

## Generate Bill Output Files

Copy these two files from [zig-bill-utils](https://github.com/denisecase/zig-bill-utils):
- zig-bill-utils-run.ps1
- zig-version.txt


Run pipeline on each `data/billname` folder in this repo:

```pwsh
./zig-bill-utils-run.ps1
```


## License

MIT License © 2025 Denise Case
