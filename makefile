default: run_setup

run_setup: setup.py
	@echo Building package
	sudo python3 setup.py build
	@echo Installing package
	sudo python3 setup.py install

clean:
	sudo rm -rf build
	sudo rm -rf dist
	sudo rm -rf src/Cysofa.egg-info