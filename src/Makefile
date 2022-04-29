

SRC_TETS=$(wildcard tests/math*.py)
SRC_FILES=$(wildcard *.py)
MATH_LIB=$(wildcard math_library*.py)
PROGRAM_DOC=doc
TEAM_NAMES=xpekny00_xkontr02_xlasmi00_xslavi37
REPO=MCBP_calc/rep
INSTALLER=install

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
    cd ../../ && rm -rf $(PROGRAM_DOC)
    cd ../../ && mkdir -p $(PROGRAM_DOC)
    cp -a tests/math_library_tests.py .
    doxygen $(SRC_TETS) $(SRC_FILES)
    mv html ../../$(PROGRAM_DOC)
    mv latex ../../$(PROGRAM_DOC)
    rm math_library_tests.py


clean:
    cd ../../ && rm -rf $(PROGRAM_DOC)
    cd ../../../ && rm $(TEAM_NAMES).zip


pack: $(SRC_FILES) $(SRC_TETS)
    cd ../../../ && mkdir -p $(TEAM_NAMES)
    cd ../../../$(TEAM_NAMES) && mkdir -p install
    cd ../../../$(TEAM_NAMES) && mkdir -p rep
    cd ../../ && cp -a $(PROGRAM_DOC) ../$(TEAM_NAMES)
    cd ../../../ && cp -a $(REPO) $(TEAM_NAMES)
    cd ../../ && cp -a $(INSTALLER) ../$(TEAM_NAMES)
    cd ../../../ && zip -qr $(TEAM_NAMES).zip $(TEAM_NAMES)
    cd ../../../ && rm -rf $(TEAM_NAMES)
