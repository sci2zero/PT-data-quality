.PHONY: install validate build test docs clean

install:
	python -m pip install -e .

validate:
	pt-data-quality validate

build:
	pt-data-quality build

test:
	python -m unittest discover -s tests -v

docs:
	mkdocs serve

clean:
	rm -rf generated site
