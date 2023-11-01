var assert = require('assert');

$http.post('https://moleculartargets.ccdi.cancer.gov/api/v4/graphql', {
  json: {
    query: 'query TargetAssociationsQuery($ensemblId: String!, $index: Int!, $size: Int!, $filter: String, $sortBy: String!, $aggregationFilters: [AggregationFilter!]) { target(ensemblId: $ensemblId) { id associatedDiseases(page: {index: $index, size: $size} orderByScore: $sortBy BFilter: $filter aggregationFilters: $aggregationFilters) { count rows { disease { id name } } } } }',
    variables: '{"ensemblId": "ENSG00000157404", "index": 0, "size": 50, "sortBy": "score", "filter": "", "aggregationFilters": []}'
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

    // Assertion 3: associatedDiseases.count is greater than 1
    assert(response.data.target.associatedDiseases.count > 1, 'associatedDiseases.count should be greater than 1');

    // Assertion 4: First disease in associatedDiseases.rows is not null
    assert(responseBody.data.target.associatedDiseases.rows[0].disease !== null, 'First disease should not be null');
});

