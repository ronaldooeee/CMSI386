""" Ronald Uy & Edwin Cheung 
	CMSI 386 - Homework #2 """

var sys = require('sys'),
	fs = require('fs');
var filename = process.argv[2];
fs.readFile(filename, 'utf8', function (read_error,content){
	var count = 0;
	content.split('\n').forEach(function(line){
		if(line.replace(/\s*\/\/.*/, "").length>0) count++;
	});
	sys.puts(count);
});