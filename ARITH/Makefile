# Please install pyinstaller if you don't have it.
# sudo pip install pyinstaller

all:
	pyinstaller --onefile arith.py
	mv dist/arith .
	rm -fr build/
	rm -fr dist/
	rm -fr __pycache__/
	rm *.spec