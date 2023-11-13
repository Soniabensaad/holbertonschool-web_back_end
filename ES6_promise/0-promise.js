// Only make Promise
function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    /* eslint-disable */
    if (true) {
      resolve(); // Corrected typo here
    } else {
      reject();
    }
    /* eslint-disable */
  });
}
export default getResponseFromAPI();
