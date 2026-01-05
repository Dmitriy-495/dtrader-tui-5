.PHONY: venv install run clean

PYTHON=/home/tda/code/dtrader/dtrader-tui-5/.venv/bin/python
PIP=/home/tda/code/dtrader/dtrader-tui-5/.venv/bin/pip

venv:
	python3 -m venv .venv

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
