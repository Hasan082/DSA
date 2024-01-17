// Harshad Number
var harshadNumber = function (num) {
    let sum =0, rem = 0, temp;
    temp = num;
    while (num > 0) {
        rem = num % 10; //6
        sum = sum + rem; //6
        num = num / 10;//15.6
    }

    console.log(num);
    console.log(sum);
    if(num%sum===0){
        return true;
    }else{
        return false;

    }


    return sum;
};

let result = harshadNumber(156);
console.log(result);