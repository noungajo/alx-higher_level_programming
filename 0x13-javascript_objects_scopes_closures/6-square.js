#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    const charArray = [];

    for (let i = 0; i < this.width; i++) {
      charArray.push(c.repeat(this.width));
    }

    console.log(charArray.join('\n'));
  }
};
