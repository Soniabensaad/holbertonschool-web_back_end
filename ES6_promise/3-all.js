// 3-all.js

import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const photoResponse = values[0];
      const userResponse = values[1];

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

export default handleProfileSignup;
