""" Ronald Uy & Edwin Cheung
	CMSI 386 - Homework #2 """

var list = {};
process.stdin.on('data',function (input){
	input.toString().split(/[\s,.\-!]+/).forEach(function(word){
		word = word.toLowerCase();
		if(word!=null&&word!='')
			list[word]=list[word]?list[word]+1:1;
	});
});
process.stdin.on('end', function (){
	Object.keys(list).sort().forEach(function(word,i){
		process.stdout.write(word+''+list[word]+'\n');
	});
});