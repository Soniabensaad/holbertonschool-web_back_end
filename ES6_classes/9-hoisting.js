export class HolbertonClass {
  constructor(year, location) {
    this.year = year; // Updated variable names
    this.location = location;
  }

  getYear() {
    return this.year;
  }

  getLocation() {
    return this.location;
  }
}

const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this.firstName = firstName; // Updated variable names
    this.lastName = lastName;
    this.holbertonClass = holbertonClass;
  }

  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }

  getHolbertonClass() {
    return this.holbertonClass;
  }

  getFullStudentDescription() {
    return `${this.firstName} ${this.lastName} - ${this.holbertonClass.year} - ${this.holbertonClass.location}`;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

const listOfStudents = [student1, student2, student3, student4, student5];

export default listOfStudents;
