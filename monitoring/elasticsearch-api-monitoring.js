var assert = require('assert');

$http.post('https://moleculartargets.ccdi.cancer.gov/api/v4/graphql', {
  json: {
    query: 'query getPedCanNav($disease: String!, $geneSymbol: String!) { pedCanNav(disease: $disease, geneSymbol: $geneSymbol) { rows { diseaseFromSourceMappedId targetFromSourceId Gene_symbol Disease SNV CNV Fusion GeneExpression Methylation DifferentialExpression id __typename } __typename } }',
    variables: '{"disease": "acute lymphoblastic leukemia", "geneSymbol": "ache"}'
  }
}, function (err, response, body) {
  if (err) {
    throw new Error(err);
  }

    // validate the mtp target profile page's headmap table
    console.log('Response:', body);
    console.log('Response:', response.statusCode);

    assert.equal(response.status, 200, 'Status code should be 200');

    // Assertion 2: Response is JSON
    assert.equal(response.headers['content-type'], 'application/json; charset=utf-8', 'Response should be JSON');

    //First CNV in pedCanNav.rows is not null
    assert(response.data.pedCanNav.rows[0]['CNV']!=null,'First CNV in pedCanNav.rows is not null');
});

