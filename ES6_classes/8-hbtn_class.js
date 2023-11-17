class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') {
      return this.size;
    } if (hint === 'string') {
      return this.location;
    }

    return null;
  }
}

export default HolbertonClass;
