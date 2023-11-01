var assert = require('assert');

$http.post('https://moleculartargets.ccdi.cancer.gov/tpm/gene-all-cancer/plotly?ensemblId=ENSG00000149451&yAxisScale=linear&includeTumorDesc=primaryOnly',
 function (err, response, body) {
  if (err) {
    throw new Error(err);
  }
    // validate the mtp target profile page's headmap table
    console.log('Response:', body);
    console.log('Response:', response.statusCode);
    assert.equal(response.status, 200, 'Status code should be 200');
});

