// A happy number 
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