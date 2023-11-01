var assert = require('assert');

$http.post('https://moleculartargets.ccdi.cancer.gov/dge/gene-all-cancer-gtex-diff-exp/plotly/json?ensemblId=ENSG00000149451',
 function (err, response, body) {
  if (err) {
    throw new Error(err);
  }

    // validate the mtp target profile page's headmap table
    console.log('Response:', body);
    console.log('Response:', response.statusCode);

    assert.equal(response.status, 200, 'Status code should be 200');

    assert(Array.isArray(response), 'Response should be an array');
    assert(response.length > 1, 'Array length should be greater than 1');
});

