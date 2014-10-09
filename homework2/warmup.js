


function change(amount){
	var quarters, nickles, dimes, pennies; 
	if (amount < 0){
		
	}
	else {
		
	}
}
function powersOfTwo(num, f){
	var limit = +process.argv[2]

	for (var x = 1, i = 0; i < limit; i += 1){
		x += x; 
	}
}

function interleave(left, right){
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