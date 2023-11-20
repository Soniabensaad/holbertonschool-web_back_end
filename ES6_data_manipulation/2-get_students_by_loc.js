const getStudentsByLocation = (students, city) => {
    return students
       .filter(obj => obj.location === city);
}
export default getStudentsByLocation;
