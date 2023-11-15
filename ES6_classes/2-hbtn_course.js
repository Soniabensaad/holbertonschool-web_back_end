export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // get name
  get name() {
    return this._name;
  }

  // set name
  set name(newName) {
    this._name = newName;
  }

  get length() {
    return this._length;
  }

  // set length
  set length(newLength) {
    this._length = newLength;
  }

  get students() {
    return this._students;
  }

  // set students
  set students(newStudents) {
    this._students = newStudents;
  }

  // toString method for better representation
  toString() {
    return `${this.name}, ${this.length}, ${this.students}`;
  }
}
