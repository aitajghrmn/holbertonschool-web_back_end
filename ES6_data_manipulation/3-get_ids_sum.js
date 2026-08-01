const getStudentIdsSum = (list) => {
  const sum = list.reduce((total, next) => total + next.id, 0);
  return sum;
};

export default getStudentIdsSum;
