let input_stdin = "";

process.stdin.on('data', data => input_stdin += data);
process.stdin.on('end', () => main());

function main() {
	//Your code goes here
	//Access standard input using the input_stdin variable
	console.log(minCost('problemsolving'))
}

function minCost(s){
	let alphabets = new Array(26).fill(0);

	for (let i = 0; i < s.length; i++){
		alphabets[s[i].charCodeAt(0) - 97] = true;
	}

	let count = 0;
	for (let i = 0; i < 26; i++){
		if (alphabets[i]){
			count++;
		}
	}
	return count;
}
