var assert = require('assert');

$http.get('https://raw.githubusercontent.com/CBIIT/mtp-config/v2.1/data/pmtl_v3.1.json', function (err, response, body) {
  if (err) {
    throw new Error(err);
  }

    // validate the mtp target profile page's headmap table
    console.log('Response:', body);
    console.log('Response:', response.statusCode);

    assert.equal(response.status, 200, 'Status code should be 200');

    // Assertion 2: Response is JSON
    assert.equal(response.headers['content-type'], 'application/json; charset=utf-8', 'Response should be JSON');
});

