Ronald Uy & Edwin Cheung <br>
CMSI 386 - Homework #4 <br> 

#####1) 
**GOTO:** <br>
Source:http://en.wikipedia.org/wiki/Goto ; http://en.wikipedia.org/wiki/Rubin_causal_model
Introduction:
It was a common usage before 1960s. However, after the advent of structured programming in around 1960s and 1970s, the usage of GOTO decreased significantly.

**Background:** <br>
GOTO performs one-way transfer of control to another line of code, according to Wikipedia. In contrast a function call normally returns control.
The primary criticism is that code that uses goto statements is harder to understand than alternative constructions. Nowadays, there are many other languages can use label to indicator different structures. We don’t need the GOTO statement too much though many languages support it.

**Conclusion:**<br>
GOTO is still a valuable way to write code. Maybe it plays a more important role in system languages which are the basics of the programming languages. “Somebody has to be the pioneer or ancestor of something. “


#####3) Tail-recursive functions:

######C:
	int minArray(int a[], int n){
		if (n == 1)
			return a[0];
		n--;
		return f(a + (a[0] > a[n]), n);
	}
		
######Javacript: 
	var min = function(array){
		var segment = function(a, b){
			return a.length === 0 ? b : segment(a.slice(1), b < a[0] ? m : a[0])
		}
		return segment(array);
	}

######Ruby:
	def minArray(array)
		def segment(a, b)
			a.empty? ? m : segment(a[1...a.length], [a[0], b].min)
		end
		segment(array)
	end
		
#####4) 
######C Declarations:
	double *a[n];	//array of pointers to doubles
	double (*b)[n]; //pointer to array of doubles
	double (*c[n])(); //array of pointers to functions that return doubles
	double (*d())[n]; //function that returns a pointer to an array of doubles

	//got help from "The Clockwise Spiral Rule" by David Anderson

######Rewritten in Go:
	var a [n]*float64; 
	var b *[n]float64;
	var c [n]*func()float64;
	var d funct()*[n]float64;

	//help from Go's Declaration Syntax page via The Go Blog

######Rewritten in Rust:
	let a: [*mut f64, ..n];
	let b: *mut [f64, ..n];
	let c: [fn() -> f64, ..n];
	fn d() -> *mut [f64, ..n];
	
#####5) Consider the code as a compiler using structural equivalence for types.
	struct A {B* x; int y;};
	struct B {A* x; int y;};
My fear, if I were a compiler, would be similar to a race in NASCAR. The car, symbolizing the code running,  and the driver, the human intellect, would continuously run in a loop until the tires (i.e, the CPU) burned out. 

On the other hand, if I were a super smart compiler with the ability to forsee future cycles, I could just throw an exception instead of trying to run the code. 

#####6) 
######Python:
	def f(): print("left")
	def g(): print("right")
	def h(x,y): pass """found the pass statement on the Python documentation found here: https://docs.python.org/release/2.5.2/ref/pass.html"""
	h(f(),g())

#####7) Consider the following code:
	void foo() {
		int i;
		printf("%d ", i++);
	}
	int main(){
		int j;
		for (j = 1; j <= 10; j++) foo();
	}

My assumption with why this code would continue printing **0 1 2 3 4 5 6 7 8 9** is that each time `foo()` is called, the stack is not being initialized.

#####8) 
	var x = 100;
	function setX(n) {x = n;}
	function printX() {console.log(x);}
	function foo(S, P, n){
		var x;
		if (n === 1 || n === 3) {setX(n);} else{S(n);}
		if (n === 1 || n === 2) {printX(); else {P();}
	}
	setX(0); foo(setX, printX, 1); printX();
	setX(0); foo(setX, printX, 2); printx();
	setX(0); foo(setX, printX, 3); printx();
	setX(0); foo(setX, printX, 4); printx();

Under shallow binding, the program would output **10203040**. This is because with shallow binding, all of the calls to `setX` & `printX` within `foo`, regardless of the parameters passed to `foo`, will used the localized `x`, which is 1, 2, 3, and 4. Then, all of the calls to `printX` within the main section of the program use the global `x`, which is always 0. <br>

With deep binding, the program output is **10x20044**. This result is because w/ deep binding, the direct calls are just normal calls w/ the basic dynamic scoping rules applied. Thus, the direct calls refer to the local `x` and not the global `x`. 

#####9)
	call foo(2)
	print* 2
	stop
	end
	subroutine foo(x)
		x = x + 1
		return
	end

In this program, the compiler allocated some memory to save the value of the literal, `2`, & each time a `2` showed up in the source code, more code was generated so that it could check in that memory address. However, when the code checks for the value in that memory cell, the value has changed. 
#####10)
	x = 1;
	y = [2, 3, 4];
	sub f(a, b) {b++; a = x + 1;}
	f(y[x], x);
	print x, y;

a) Under *pass by value*: 1,2,3,4 <br>
b) Under *pass by value-result*: 2,2,2,4 <br>
c) Under *pass by reference*: 2,2,3,4 <br>
d) Under *pass by name*: 2,2,3,3 <br>