export default function handleResponseFromAPI(promise) {
  return Promise
      .then(() => ({
        status: 200,
        body: 'success',
      }))
      .catch(() => Error())
      .finally(() => console.log('Got a response from the API'));
}
