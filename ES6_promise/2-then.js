export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    promise
      .then((result) => {
        console.log(result.data);
        resolve(result);
      })
      .catch((error) => {
        console.error(error);
        reject(error);
      });
  });
}
