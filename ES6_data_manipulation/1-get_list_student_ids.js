const getListStudents = () => [
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];
  
  const getListStudentIds = (students) => {
    if (!Array.isArray(students)) {
      return [];
    }
    return students.map(obj => obj.id);
  };
  
  export default getListStudentIds;
  