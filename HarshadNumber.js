/**
 * Checks if a number is a Harshad number.
 *
 * @param {number} num - The number to be checked.
 * @return {boolean} True if the number is a Harshad number, false otherwise.
 * The number 18 is a Harshad number because it is divisible by the sum of its digits, which is 1 + 8 = 9.
 * The number 23 is not a Harshad number because it is not divisible by the sum of its digits, which is 2 + 3 = 5.
 */
var harshadNumber = function (num) {
    let sum =0, rem = 0, temp;
    temp = num;
    while (num > 0) {
        rem = num % 10; //6
        sum = sum + rem; //6
        num = num / 10;//15.6
    }

    if(num%sum===0){
        return true;
    }else{
        return false;
    }
};

let result = harshadNumber(156);
console.log(result);