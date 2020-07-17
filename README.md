# LogPrint
Logging the python `print()` function

## Intro
Just a basic script to log every print() function call to a file in the working directory of 
the entry file.

## Usage
On each module simply import the new print function.

	from log_print import print 

This only overrides the print function in the module importing the function. Other modules are unaffected and will not be logged if `print()` is called

## Example
Basic module called `testfile1` will be imported into out main program:

	print("1hello")
	
	class Test():
	    print("2hello")
	    def func(self):
	        print("3hello")
	    print("4hello")

This module doesn't import the new print function, no logging will occur from print() usage inside this module.

When we run Python, we will only see logging from the main module:

	Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] 
	on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from log_print import print
	>>> print("MAIN HELLO")
	MAIN HELLO
	>>> from new.testfile1 import Test
	1hello
	2hello
	4hello
	>>> Test().func()
	3hello
	>>>

Outputted to log file:

	MAIN HELLO

Now import the new print function:

	from log_print import print
	
	
	print("1hello")
	
	class Test():
	    print("2hello")
	    def func(self):
	        print("3hello")
	    print("4hello")

After importing new print function into testfile1:

	Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] 
	on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from log_print import print
	>>> print("MAIN HELLO AGAIN")
	MAIN HELLO AGAIN
	>>> from new.testfile1 import Test
	1hello
	2hello
	4hello
	>>> Test().func()
	3hello
	>>>

Outputted to log file:

	MAIN HELLO AGAIN
	
	1hello
	
	2hello
	
	4hello
	
	3hello

