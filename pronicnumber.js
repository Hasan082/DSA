/**
 * Check if a number is a pronic number.
 *
 * @param {number} n - The number to check.
 * @return {boolean} Whether the number is a pronic number or not.
 * Pronic means 6 = 2*3, 12 = 3*4, 20 = 4*5. 72 = 8*9;
 */
let pronicNumber = function (n) {
    if (n == 1) {
        return true;
    }
    for (let i = 1; i < n; i++) {
        if(i * (i + 1) == n){
            return true;
        }
    }
    return false;
}


for(let j = 1; j <= 100; j++){
    let res = pronicNumber(j);
    if(res == true){
        console.log(j);
    }
}