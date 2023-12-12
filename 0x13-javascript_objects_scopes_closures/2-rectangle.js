#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // Create an empty object if w or h is not a positive integer
      return class Rectangle{};
    }

    this.width = w;
    this.height = h;
  }
}
