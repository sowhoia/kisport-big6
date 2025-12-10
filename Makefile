PYTHON ?= python3

.PHONY: all run test clean web plan9 boot linux win

all: run

run:
	$(PYTHON) big6.py

linux:
	$(PYTHON) big6.py

win:
	$(PYTHON) big6.py

test:
	$(PYTHON) test_big6.py

web:
	@echo "Starting web version with Pyodide..."
	$(PYTHON) -m http.server 8000

plan9:
	$(PYTHON) big6_plan9.py

boot:
	$(PYTHON) big6_boot.py

clean:
	rm -rf __pycache__ *.pyc tests/*.actual

