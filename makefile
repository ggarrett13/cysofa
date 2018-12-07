all: setup.py
	@echo Building package
	sudo python3 setup.py build
	@echo Installing package
	sudo python3 setup.py install

build: setup.py
	@echo Building package
	sudo python3 setup.py build

install: setup.py
	@echo Installing package
	sudo python3 setup.py install

clean:
	sudo rm -rf build
	sudo rm -rf dist
	sudo rm -rf src/cysofa.egg-info
	sudo rm -rf src/cysofa/*.so
	sudo rm -rf src/cysofa/cypyx/*.c
	sudo rm -rf *.so