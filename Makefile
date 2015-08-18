clean:
	-@rm -rf .eggs build dist pagestat.egg-info
	-@cat INSTALL.manifest | xargs rm -rf
	-@rm INSTALL.manifest
install: clean
	@python setup.py install --record INSTALL.manifest

test: install
	@python setup.py test