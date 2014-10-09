""" Ronald Uy & Edwin Cheung 
	CMSI 386 - Homework #2 """


exports.change = function (amount){
	
	var quarters, nickels, dimes, pennies, rest; 
	
	if (amount < 0){
		throw "Amount cannot be Negative";
	}
	else {
		quarters = Math.floor(amount/25);
		rest = amount % 25; 
		dimes = Math.floor(rest/10); 
		rest = amount % 10; 
		nickels = Math.floor(rest/5);
		pennies = nickels % 5; 
	} 
	return [quarters, dimes, nickels, pennies];
}

exports.strip_quotes = function (s){
	return s.replace(None, "\'");
}

exports.scramble = function (s){
	var a = s.split("");
	n = a.length;

	for (var i = n -1; i > 0; i--){
		var j = Math.floor(Math.random() * (i + 1));
		var temp = a[i];
		a[i] = a[j];
		a[j] = temp
	}
	return a.join("");
}

exports.powersOfTwo = function (num, f){
	result = 1;
	while (result <= num){
		f(result);
		result *= 2;		
	}
}

exports.prefixes = function(s, f){

}

exports.interleave = function(left, right){
	var result = []
		L1 = 0;
		R1 = 0;
	while (L1 < left.length && R1 < right.length){
		if (left[L1] < right[R1]){
			result.push(left[L1++]);
		}
		else {
			result.push(right[R1++]);
		}
	}
	return result.concat(left.slice(L1)).concat(right.slice(R1));
}

exports.stutter = function(a){
	return interleave (a, a);
}