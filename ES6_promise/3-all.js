import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      if (photoResponse.status === 200 && userResponse.status === 200) {
        console.log(`Body: ${photoResponse.body}`);
        console.log(`First Name: ${userResponse.firstName}`);
        console.log(`Last Name: ${userResponse.lastName}`);
      } else {
        throw new Error('Signup system offline');
      }
    })
    .catch((error) => {
      console.error(error.message);
    });
}
