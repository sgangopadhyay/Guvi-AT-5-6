function Suman() {
  return "i live in bangalore";
}

// functions with arguments
function Add(x, y) {
  let sum = x + y;
  return sum;
}

// function with default arguments
function AreaOfCircle(radius, pi = 3.141) {
  let area = 0;
  area = pi * radius * radius;
  return area;
}

let suman = AreaOfCircle(11);

// function statement
let data = function (radius, pi = 3.141) {
  let area = 0;
  area = pi * radius * radius;
  return area;
};

console.log(data(10));

// ARROW FUNCTION
// Javascript - 6

let patna = (x, y) => x + y;

console.log(patna(50, 40));

let area_of_circle = (radius, pi = 3.141) => {
  let area = pi * radius * radius;
  return area;
};

console.log(area_of_circle(20));
