all:
	rpmbuild --define="_sourcedir $$(pwd)" -ba extra-keyboards.spec
