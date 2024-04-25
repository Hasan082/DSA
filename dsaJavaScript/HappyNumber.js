
/**
 * Determines if a number is a happy number.
 *
 * @param {number} n - The number to check for happiness.
 * @return {boolean} - Returns true if the number is happy, false otherwise.
 * 19
 * sq(1) + sq(9) = 82
 * sq(8) + sq(2) = 68
 * sq(6) + sq(8) = 100
 * sq(1) + sq(0) + sq(0) = 1
 */
var isHappy = function (n) {
    if (n == 1) {
        return true;
    } else if (n === 4) {
        return false
    } else {
        let s = 0;
        let a = n.toString().split('');
        for (let i = 0; i < a.length; i++) {
            s += a[i] * a[i];
        }
        n = s;
    }
    return isHappy(n);
};



// Program to print all Happy numbers between 1 to 100


for (let i = 1; i <= 100; i++) {
    let res = isHappy(i);
    if(res == true){
        console.log(i);//all Happy number
    }
}