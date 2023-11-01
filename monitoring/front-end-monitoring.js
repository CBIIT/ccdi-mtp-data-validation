var assert = require('assert');

$http.post('https://moleculartargets.ccdi.cancer.gov/disease/MONDO_0018997/associations', function (err, response, body) {
  if (err) {
    throw new Error(err);
  }

    // validate the mtp target profile page's headmap table
    console.log('Response:', body);
    console.log('Response:', response.statusCode);

    assert.equal(response.status, 200, 'Status code should be 200');

});

