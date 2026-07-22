export default function appendToEachArrayValue(array, appendString) {
  const final = [];
  for (const idx of array) {
    final.push(appendString + idx);
  }

  return final;
}
