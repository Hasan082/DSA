
/**
 * Counts the number of digits in a given number.
 *
 * @param {number} number - The number whose digits are to be counted.
 * @return {number} The number of digits in the given number.
 */
function countDigits(number) {
    // Handle the case when the number is 0 separately
    if (number === 0) {
        return 1;
    }

    // For non-zero numbers, count the digits without using Math.abs
    let count = 0;
    let num = (number < 0) ? -number : number;  // Take the absolute value if the number is negative
    
    // Perform integer division using repeated multiplication
    while (num !== 0) {
        num = (num / 10) | 0;  // Use bitwise OR to perform integer division
        count++;
    }
    
    return count;
}

// Example usage:
let num = -12345;
let digitCount = countDigits(num);
console.log(`Number of digits in ${num}: ${digitCount}`);
