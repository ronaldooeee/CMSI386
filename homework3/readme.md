##CMSI 386 - Homework #3##
Ronald Uy & Edwin Cheung <br>
<br>
#####1) (a = 3) >= m >= ! & 4 * ~ 6 || y %= 7 ^ 6 & p
 
![alt text](https://github.com/ronaldooeee/CMSI386/blob/master/homework3/Abstract%20Syntax%20Tree.JPG)
		

#####2) 
	function f(){
		return
			{x: 5}
	}
The code above is expected to return the object {x: 5}, but the script actually returns *undefined* because Javascript inserts a semicolon after **return**. If the function were written in Python, the program would have terminated if the **return** were followed by a newLine. 

	var b = 8
	var a = b + b
	(4 + 5).toString(16)

People might expect to change a number to a string. However, the code doesn't have a semicolon and there are only 2 declarations. What it actually does is initialize b, then initialize a to b+b(4+5).toString(16), resulting in a TypeError. Python for example, would end the statement after the *b+b* declaration. 

	var place = "mundo"
	["Hola", "Ciao"].forEach(function (command) {
		alert(command + ", " + place)
	})

The first line of this code is assigning the string "mundo" to the variable place. The rest of the code is expected to display "Hola, mundo" & "Ciao, mundo". However, the result is a TypeError because Javascript tries to evaluate "mundo"["Hola", "Ciao"].forEach(function (command) & returns undefined, which makes it impossible to call the method forEach of undefined. Python would have ended the declaration statement after the newline. 
	
	var sayHello = function () {
		alert("Hello")
	}
	
	(function () {
		alert("Goodbye")
	}())

People might expect to alert "Hello" after calling sayHello & after they called sayHello, they add another function which will alert "Goodbye". However, when sayHello is called, the result is a function that alerts "Hello" which is evaluated first & alerts "Goodbye" which produces undefined. 

#####3) Give an example of a program in C that would not work correctly if local variables were not allocated in static storage as opposed to the stack For the purposes of this question, local variables do not include parameters.

	void f(int x) {
		int a = 1;
		int b;
		
		if (x < 0){
			a = 2;
			return 0; 
		}
		else {
			b = f(-x);
			return a + b;
		}
	} 

#####4) Given:
	var x = 100;
	function setX(n) {x=n;}
	function printX() {console.log(x);}
	function first() {setX(1); printX();}
	function second() {var x; setX(2); printX();}
	setX(0);
	first();
	printX();
	second();
	printX();

Using static scoping, this program will output the number 1122 because when **setX()** is executed the second time, it changes the global variable x to 2, which leads to the last **printX()** to print out 2. <br>

With dynamic scoping, the output will be 1121. This is because when **setX()** is executed the second time, following dynamic scoping rules, it changes the local x to 2 instead of the global x, thereby leaving the global x unchanged. 

#####5) Translate the following expression into (a) postfix and (b) prefix notation, in both cases *without using parenthesis*:
	(-b + sqrt(4 x a x c))/ (2 x a)
	
	int a, b, c, d = 1, 1, 1, 1
	def f(b): 
		c = 2; 
		return 1
	print a-f(b)-c*d

a) Postfix: the script above (using slightly modified code from problem 6), would print -2 if f(b) was evaluated before c*d.

b) Prefix: The script above would print out -1 if c*d was evaluated before f(b). 


#####6) The exression **a-f(b)-c*d** can produce different values depending on how a compiler decides to order, or even parallelize operations. Give a small program in the language of your choice (or even one of your own decide) that would produce different values for this expression for different evaluation orders. As you learned in class, "different evaluation orders" *does not mean* that the compiler can violate the precedence and associativity rules of the language. It simply means operands can be evaluated in any order before an operation is applied. 

	int a, b, c, d = 1, 1, 1, 1 
	
	def f(b):
		return b
	print a-f(b)-c*d

The above expression will be evaluated left to right, returning -13. <br>
or 
	int a, b, c, d = 1, 2, 3, 4
	a = b + c
	a = 5 
	c = a + d 
	c = 0
	a-f(b)-c*d

will return -33. Through some procedures, we can have different results with different evaluation order and the evaluation order remains the same for the operands (function evaluation first, * has a higher priority that -). 

#####7) Write the interleave function from the three previous assignments in C++, using C-style arrays. 
	
	#include "stdafx.h"
	#include <iostream>
	#include <array>
	using namespace std; 

	int* interleave(int firstArray[], int arrayLength1, int secondArray[], int arraylength2){
		int length = arrayLength1 + arrayLength2; 
		int thirdArray[length]; 
		int index = 0;
		
		for (int i = 0; i < length; i++){
			if (arrayLength1 > i){
				thirdArray[index] = firstArray[i];
				index++;
			}
			if (arrayLength2 > i){
				thirdArray[index] = secondArray[i];
				index++;
			}
		return thirdArray; 
		}
	

#####8) Write the interleave function from the previous three assignments in C++, using C++ vectors (from the Standard Library). 
		
	template<class T>
	
	vector<T>interleave(vector<T>, length1, vector<T>, length2){
		vector<T> result = []; 
		int size1 = size1.size();
		int size2 = size2.size();
		int total = size1 + size2;

	for (int i = 0; i < total; i++){
		if (i < size1){
			result.push_back(length1[i]); //found push_back off of Google
		}
		if (i < size2){
			result.push_back(length2[i]);
		}
		return result; 
	}
	
#####9) a) How efficient is **same_fringe** when the trees differ in their first few leaves? 

The function **same_fringe** is horrible in efficiency when it comes to computing trees that are very large because it computes the entire fringe of two very large trees that actually show that they are not the same early on in the comparison. 

#####9) b) Write an efficient (lazy) version of **same_fringe** in Python. 

	from itertools import izip_longest

	def fringe(tree):
		for node1 in tree: 
			if isinstance(node1, tuple):
				for node2 in fringe(node1):
					yield node2
			else:
				yield node1
	
	def same_fringe(tree1, tree2):
		return all(node1 == node2 for node1, node2 in izip_longest(fringe(tree), fringe(tree2)))
			
#####9) c) Write an efficient (lazy) version of **same_fringe** in Javascript.

#####10) One of the freshmen had trouble remembering the conditional operator in C++ so she tried to wrap it inside of a function with a readable, so she wrote: 
	template <class T>T if_then_else(bool, x, T y, T z){
		return x ? y : z;
	}
##### Why is this wrong? Would a macro have helped? Why? Show the macro. 

The reason this is wrong is because the function arguments are evaluated before the actual call & the conditional operator only evaluates the condition and only of the two arms, not both. 