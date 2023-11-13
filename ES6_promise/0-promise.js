// Only make Promise
function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        if (true) {
            resolve(); // Corrected typo here
        } else {
            reject();
        }
    });
}

export default getResponseFromAPI();
