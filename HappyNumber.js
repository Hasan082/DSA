// A happy number 
var isHappy = function (n) {
    if(n==1){
        return true;
    }else if(n===4){
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