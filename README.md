# Pastebin Crawler
It crawles pastebin
## Requirement
- docker installed and configured.
- clone/download this repo.

## Build
run the following in this folder (use sudo if needed)

`docker build -t crawler .`

## Run

`docker run crawler`

## Manual Installation
run the following:

`pip install -r requirements.txt`

## Manual Run
in order to manually run this crawler simply do:

`python main.py`


## Lint
lint via flake8
`flake8`

## Testing
unit tests are made using pytest.
all unit test are at `test/units`
