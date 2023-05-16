clean:
	find . -name __pycache__ | xargs rm -r
	find . -name *.egg-info | xargs rm -r
	find . -name .DS_Store | xargs rm -r
	rm -rf build
