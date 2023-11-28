// Q1
let x = parseInt(window.prompt("Enter Number 1"))
let y = parseInt(window.prompt("Enter Number 2"))
let z = parseInt(window.prompt("Enter Number 3"))
const ar = [x, y, z]
ar.sort()
console.log("Max Number = " + ar[2])

// Q2
let x2 = parseInt(window.prompt("Enter Number"))
if (x2 % 2 == 0){
    console.log("Even")
}
else{
    console.log("Odd")
}

// Q3
let pass = window.prompt("Enter Password")
if(pass != "hjk7$12"){
    console.log("Try Again")
}
else{
    console.log("Logged in")
}

// Q4
let x3 = parseInt(window.prompt("Enter Number 1"))
let y3 = parseInt(window.prompt("Enter Number 2"))

if(y3 > x3){
    console.log("Number 2 > Number 1")
}
else{
    console.log("Number 1 >= Number 2")
}

// Q5
let rad = parseInt(window.prompt("Enter Radius"))
let volume = rad * rad * 3.14 * 4 / 3
console.log("Area = " + volume)

// Q6
let x4 = parseInt(window.prompt("Enter Number 1"))
let y4 = parseInt(window.prompt("Enter Number 2"))
let prod = x4*y4
console.log("Product = " + prod)

// Q7
let x5 = parseInt(window.prompt("Enter Number 1"))
let y5 = parseInt(window.prompt("Enter Number 2"))
let z5 = parseInt(window.prompt("Enter Number 3"))
let sum = x5 + y5 + z5
console.log("Sum = ", sum)

// Q8
let num = window.prompt("Enter Number").toString()
let last = parseInt(num[num.length - 1])
console.log("Last Digit = " + last)