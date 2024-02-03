export default function handleResponseFromAPI(promise) {
  return promise
  // eslint-disable-next-line
    .then((result) => {
      console.log('Got a response from the API');
      return { status: 200, body: 'success' };
    })
  // eslint-disable-next-line
    .catch((error) => {
      console.error('An error occured');
      return new Error();
    });
}
