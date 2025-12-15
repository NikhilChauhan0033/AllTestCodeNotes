console.log("Hello js");

// let fullName = "Nikhil Chauhan";
// console.log(typeof fullName, fullName);

// const age = 22;
// console.log(typeof age, age);

// const isFollow = true;
// console.log(typeof isFollow, isFollow);

// const marks = 89.9;
// console.log(typeof marks);

// const infoStudent = {
//   fullName: "Nikhil Chauhan",
//   age: 22,
//   CGPA: 8.3,
// };

// infoStudent.age = 23;
// infoStudent["age"] = 23;

// console.log(infoStudent);
// console.log(infoStudent["age"]);
// console.log(infoStudent.fullName);

// let arr = [1, 2, 3, 4, 5, 6];
// console.log(typeof arr);

// let peopleAge = 19;

// if (peopleAge >= 18) {
//   console.log("You Can Vote");
// } else {
//   console.log("You Can't Vote");
// }

// let number = 20
// if (number % 2 == 0){
//     console.log("Even Number")
// }else{
//     console.log("Odd Number")
// }

// let num1 = 18

// if (num1 <= 18){
//     console.log("Junior")
// }else if (num1 >= 60){
//     console.log("Senior")
// }else {
//     console.log("Middle")
// }

// var age1 = 1
// age1 >= 18 ? console.log("Adlut") : console.log("Not adult");

// let num = prompt("Enter A Number To check the number is multiply by 5 or not");
// if(num % 5 === 0){
//     console.log(num + "is multiply by 5")
// }
// else {
//     console.log(num + " is not multiply by 5")
// }
// console.log(num)

// let score = 9;
// if(score <=100 && score>=80){
//     console.log("'A' GRADE")
// }else if(score <=79 && score>=70){
//     console.log("'B' GRADE")
// }else if(score <=69 && score>=60){
//     console.log("'C' GRADE")
// }else if(score <=59 && score>=50){
//     console.log("'D' GRADE")
// }else{
//     console.log("'F' GRADE")
// }

// for(let i = 1; i<=10; i++){
//     console.log("Hello")
// }

// let sum = 0;
// for (let i = 1; i <= 5; i++) {
//   sum = sum + i;
// }
// console.log(sum);

// let multiply = 1;
// for (let i = 1; i <= 3; i++) {
//   multiply = multiply * i;
// }
// console.log(multiply);

// let i = 1;
// while (i <= 10) {
//   console.log(i);
//   i++;
// }

// let j = 1;
// do {
//   console.log(j);
//   j++;
// } while (j <= 10);

// let str1 = "NikhilChauhan";
// for (let varName of str1) {
//   console.log(varName);
// }

// const studentObj = {
//   name: "Nikhil",
//   age: 22,
//   CGPA: 9.5,
// };

// for(let obj in studentObj){
//     console.log("key",obj,"Values",studentObj[obj])
// }

// for (let i = 1; i <= 100; i++) {
//   if (i % 2 == 0) {
//     console.log(i);
//   }
// }

// let gNumber = 10;
// let userNumber = prompt("Enter the number");

// while(userNumber != gNumber){
//     userNumber = prompt("You Enter The Wrong number Guess Again");
// }

// console.log("Congratulation You Guess the right number")

// let str1 = "Nikhil"
// console.log(str1.length)
// console.log(str1[0])
// str2 = str1.toUpperCase()
// console.log(str2)

// let userName = prompt("Enter your Name For Username");
// console.log(`@${userName.trim()}${userName.trim().length}`)

// let arr = [10,20,30,40,60]
// console.log(arr)
// console.log(arr.length)

// for(let i = 0; i<arr.length;i++){
//     console.log(arr[i])
// }

// for(let i of arr){
//     console.log(i)
// }

// for(let i in arr){
//     console.log(arr[i])
// }

// let marksToAvg = [22,33,44,55,66]
// let sum = 0;
// let res;

// for(let j of marksToAvg){
//     sum = sum + j
//     res = sum/marksToAvg.length
// }

// console.log(res);
// let str = "Nikhil";
// let reversed = "";
// for (let i = str.length - 1; i >= 0; i--) {
//     reversed += str[i];
// }
// console.log(reversed); // lihkiN

// let number = [100,200,300,400,500,600,700,800,900]

// for(let j of number){
//     let i = j*20/100
//     // console.log(i)
//     number = j-i
//     console.log(number)
// }

// let foodItems = ["mango","potato","tomato"];
// foodItems.push("milk","chass");
// console.log(foodItems);
// let popitem = foodItems.pop();
// console.log(popitem);
// console.log(foodItems.toString()) //convert array to string

// let companies = ["uber","ola","amazon","flipkart"]

// companies.shift()
// console.log(companies)
// companies.push("meta")
// console.log(companies)
// companies.splice(1,1,"rapido")
// console.log(companies)

// function fun1() {
//   console.log("Learning Function");
// }

// fun1();

// function fun2(msg) {
//   //parameter
//   console.log(msg);
// }

// fun2("hello from nik"); //argument

// function sumCaculate(a, b) {
//   console.log(a + b);
// }

// sumCaculate(10, 20);

// function minusCalculate(x, y) {
//   z = x - y;
//   return z;
// }
// let res = minusCalculate(10,20)
// console.log(res)

// const arrowSum = (a,b) => {
//     return a+b;
// }

// let res1 = arrowSum(13,4);
// console.log("arrowsum " + res1)
// let str = "ae";
// let count = 0;

// function vowel(str) {
//   for (let i = 0; i < str.length; i++) {
//     let j = str[i];
//     if (j === "a" || j === "e" || j === "i" || j === "o" || j === "u") {
//       count++;
//     }
//   }
//   console.log("Total vowels:", count);
// }

// vowel(str);

// let arr = [10,20,30,40,50]
// let arr1 = [];

// arr.forEach((val)=>{
//     res = val*val
//     console.log(res)
//     arr1.push(res)

// })
//     console.log(arr1)

let mode = "light";

function modefun() {
  let body = document.querySelector("body");

  if (mode === "light") {
    body.style.backgroundColor = "black";
    body.style.color = "white";
    mode = "dark"; // ✅ update the mode
  } else {
    body.style.backgroundColor = "white";
    body.style.color = "black";
    mode = "light"; // ✅ update the mode
  }
}

// callback function

// function sum1(a,b){
// console.log(a+b);
// }

// function sumCallBack(a,b,SumCall){
//   SumCall(a,b)
// }

// sumCallBack(10,20,sum1)

function funSum() {
  let para = document.getElementById("para");
  para.innerHTML = "Sum of 2 Numbers";

  let num1 = Number(document.getElementById("num1").value);
  let num2 = Number(document.getElementById("num2").value);

  let result = document.getElementById("result");
  result.innerHTML = `Sum Of 2 Number Is ${num1 + num2}`;
}

const looping = () => {
  for (let i = 1; i <= 10; i++) {
    console.log(i);
  }
};

looping();

let j = 1;
while (j <= 10) {
  console.log(j);
  j++;
}

for (let i = 10; i >= 0; i--) {
  console.log(i);
}

// console.log("1")
// setTimeout(()=>{
//   console.log("2")
//   alert("Hellow from setTimeOut AFter 3 seconds")
// },3000)
// console.log("3")

// like setInterval appears after every interval time is compelete
// console.log("Start");

// setInterval(() => {
//   console.log("Hello every 2 seconds!");
// }, 2000);

// console.log("End");

let box = document.getElementById("box");
let p = document.createElement("p");

p.innerHTML = "cretaed through js";
p.style.color = "pink";
p.style = "color:red , ";

box.appendChild(p);

let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];

let arr3 = [...arr1, ...arr2];
console.log(arr3);

let ob1 = {
  name: "nik",
  mob: "99",
};
let ob2 = { 
  city: "Delhi", 
  age: 21 
};

let ob3 = { ...ob1, ...ob2 };
console.log(ob3);


let objec = {
  myName : "Nikhil",
  email:"nik@gmail.com",
  age : undefined
};

let {myName:nikName, age = 21} = objec
console.log(objec)
console.log(nikName)
console.log(age)
// console.log(myName)


let ar = [11,1,2,3,4,5]

for(let i of ar){
  if(i % 2 !== 0){
    console.log(i)
    break;
  }
}

class StudentInfo{
  name="nikhil";
  age=19;
  mobileNumber = 999999999999
}

let student1 = new StudentInfo()
console.log(student1)

let StudentInfo1 = {
 name:"nikhil",
  age:19,
  mobileNumber : 999999999999
}

console.log(StudentInfo1)

localStorage.setItem("name","nikhil")

var z = localStorage.getItem("name")
console.log(z)

let fruits = ["apple", "banana", "mango"];
localStorage.setItem("fruits", JSON.stringify(fruits));

// retrieve
let storedFruits = JSON.parse(localStorage.getItem("fruits"));
console.log(storedFruits); // ["apple", "banana", "mango"]


let student = { name: "Nikhil", age: 21, email: "nik@gmail.com" };
localStorage.setItem("student", JSON.stringify(student));

// retrieve
let storedStudent = JSON.parse(localStorage.getItem("student"));
console.log(storedStudent); // { name: "Nikhil", age: 21, email: "nik@gmail.com" }


fetch("https://jsonplaceholder.typicode.com/photos")
  .then((response) => response.json())  // parse JSON from the response
  .then((data) => {
    console.log(data);  // THIS is your actual array of objects
  })
  .catch((e) => {
    console.error(e);
  });
