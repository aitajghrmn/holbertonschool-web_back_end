const getStudentsByLocation = (list, city) => {
  const students = list.filter((item) => item.location === city);
  return students;
};

export default getStudentsByLocation;
