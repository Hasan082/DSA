// Program to determine whether a given number is a Disarium number

/**
 * Calculates the sum of the power of the digits in a given number.
 *
 * @param {number} n - The number for which the sum of the power of its digits needs to be calculated.
 * @return {boolean} Returns true if the sum of the power of the digits is equal to the original number, otherwise returns false.
 */
var calculateSumOfPowerDigits = function(n) {
    let dtos = n.toString();
    let ln = dtos.length;
    let sum = 0;

    for (let i = 0; i < ln; i++) {
        let digit = parseInt(dtos[i]);
        let power = i + 1;
        let poweredDigit = 1;

        for (let j = 0; j < power; j++) {
            poweredDigit *= digit;
        }

        sum += poweredDigit;
    }
    if(n===sum){
        console.log(sum);
        return true;
    }else {
        return false;
    }
};

let result = calculateSumOfPowerDigits(15);
console.log(result); // Output: 175 (1^1 + 7^2 + 5^3)

for (let i = 1; i <= 200; i++){
    calculateSumOfPowerDigits(i);
}