let input_stdin = "";

process.stdin.on('data', data => input_stdin += data);
process.stdin.on('end', () => main());

function main() {
	//Your code goes here
	//Access standard input using the input_stdin variable
	console.log(romanToDecimal('MCMIV'))
}

function value(r){
	if (r == 'I')
		return 1;
	if (r == 'V')
		return 5;
	if (r == 'X')
		return 10;
	if (r == 'L')
		return 50;
	if (r == 'C')
		return 100;
	if (r == 'D')
		return 500;
	if (r == 'M')
		return 1000;
	return -1;
}

function romanToDecimal(str){
	var res = 0;
	for (let i =0; i < str.length; i++) {
		var s1 = value(str.charAt(i));
		if (i+1 < str.length){
			var s2 = value(str.charAt(i+1));
			if (s1 >= s2){
				res = res + s1;
			} else {
				res = res + s2 - s1;
				i++;
			}
		} else {
			res = res + s1;
		}
	}
	return res;
}
