 

SRC_TETS=$(wildcard tests/*.py)
SRC_FILES=$(wildcard *.py)
MATH_LIB=$(wildcard math_library*.py)
PROGRAM_DOC=Program_documentation
TEAM_NAMES=xpekny00_xkontr02_xlasmi00_xslavi37
REPO=ivs_project_2

all: setup

setup: $(SRC_FILES)
	sudo apt-get -y update
	sudo apt-get install python3-pip
	sudo pip3 install pyqt5


test: $(MATH_LIB)
	python3 -m unittest tests.math_library_tests


run: $(SRC_FILES)
	cd .. && python3 -m src.gui


profile: $(SRC_FILES)
	python3 -m profiling


doc: Doxyfile $(SRC_FILES) $(SRC_FILES)
	cd .. && rm -rf $(PROGRAM_DOC)
	cd .. && mkdir -p $(PROGRAM_DOC)
	doxygen $(SRC_TETS) $(SRC_FILES)
	mv html ../$(PROGRAM_DOC)
	mv latex ../$(PROGRAM_DOC)
    

clean:
	cd .. && rm -rf $(PROGRAM_DOC)
	cd ../../ && rm $(TEAM_NAMES).zip


pack:
	cd ../../ && mkdir -p $(TEAM_NAMES)
	cd .. && cp -a $(PROGRAM_DOC) ../$(TEAM_NAMES)
	cd ../../ && cp -a $(REPO) $(TEAM_NAMES)
	cd ../../ && zip -qr $(TEAM_NAMES).zip $(TEAM_NAMES)
	cd ../../ && rm -rf $(TEAM_NAMES)
