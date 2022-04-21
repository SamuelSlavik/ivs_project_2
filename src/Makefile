

SRC_TETS=$(wildcard tests/*.py)
SRC_FILES=$(wildcard *.py)
MATH_LIB=$(wildcard math_library*.py)
DOC_FILES=# TODO
TEAM_NAMES=# TODO

all: setup

setup: $(SRC_FILES)
	sudo apt-get -y update
	sudo apt-get install python3-pip
	sudo pip3 install pyqt5
#pyinstaller sudo pip3 install pyinstaller

test: $(MATH_LIB)
	python3 -m unittest tests.math_library_tests

run: $(SRC_FILES)
	python3 -m gui

profile: $(SRC_FILES)
#TODO urobiť profiling

documentation:
#TODO urobiť doxygene

clean:
#TODO

zip:
#TODO

install:
#TODO urobiť inštalaciu

uninstall:
#TODO urobiť odinštaláciu
