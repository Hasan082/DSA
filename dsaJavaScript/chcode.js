let x = "abc"; //`ab
let z = [];
for(let i = 0; i < x.length; i++) {
    console.log(x[i]);
    let y = x.charCodeAt(i);
    z.push(String.fromCharCode(y-1));
}

console.log(z)