const getStudentsByLocation = (students, city) => students
  .filter((obj) => obj.location === city);
export default getStudentsByLocation;
