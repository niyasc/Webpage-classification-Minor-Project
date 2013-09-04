import sys
sys.path.insert(0, './lib') #set library location
from web import *;

def main():
	address="http://jmi.ac.in"
	webclass=web()
	content=webclass.getContent(address)
	print("Whole content");
	print(content)
	text=webclass.getPureText(content)
	print("Pure text")
	print(text)

if __name__ == "__main__":
	sys.exit(main())

