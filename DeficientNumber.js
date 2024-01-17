let deficientNumber = function (n) {
    let sum = 0;
    for (let i = 0; i <= n; i++) {
        if (n % i === 0) {
            sum += i;
        }
    }
 
    if (sum < 2 * n) {
        return true
    } else {
        return false
    }

}

let x = deficientNumber(18);
console.log(x);

for(let i = 1; i < 100; i++){
    let res = deficientNumber(i);
    if(res){
        console.log(i);
    }
}
