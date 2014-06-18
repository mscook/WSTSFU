test:
	pip install nose
	nosetests tests

docs:
	pip install sphinx
	python setup.py docs
