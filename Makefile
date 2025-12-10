PYTHON ?= python3

.PHONY: all run test clean web linux win

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

clean:
	rm -rf __pycache__ *.pyc tests/*.actual


