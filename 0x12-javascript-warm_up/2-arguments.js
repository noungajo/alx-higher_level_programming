#!/usr/bin/node

const leng = process.argv.length;

if (leng < 3) {
  console.log("No argument");
} else if (leng === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
