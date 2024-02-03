// 10-car.js
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  set brand(newBrand) {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  set motor(newMotor) {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  set color(newColor) {
    return this._color;
  }

  cloneCar() {
    const newCar = new this.constructor();
    for (const key in this) {
      if (typeof this[key] === 'function') {
        newCar[key] = this[key].bind(newCar);
      } else {
        newCar[key] = this[key];
      }
    }
    return newCar;
  }
}
