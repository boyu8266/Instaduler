.DEFAULT_GOAL := all

.PHONY: all
all: clean

.PHONY: clean
clean:
	-rm	-rf	./build/
	-rm	-rf	./dist/

.PHONY: install
install:
	pip install -r requirements.txt
	python setup.py install

.PHONY: uninstall
uninstall:
	pip uninstall instaduler -y