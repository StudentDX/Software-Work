/*
David Xiedeng
Softdev pd 1
K18 -- Come Up For Air
2020-04-19
*/

//passing info from Flask to js
//indirectly uses a meta tag
// inefficent, but no time to change
var fromFlask = document.getElementById('server-info');
// java info
var data = fromFlask.dataset.server;
data = JSON.parse(data);
fromFlask.remove();

// lowest year available in selection is 1880
// var currentYear = 1880;
var graphBottomYear = 1880;
var graphTopYear = 1885;

function createBarData(min, max) {
  // stores number instances in years [min, max]
  // eg 1880 - 1885 > 1880, 81, 82, 83, 84, 85
  // and number of crashes per year
  let filteredDataRange = [];
  for (yearIndex = min; yearIndex <= max; yearIndex += 1) {
    filteredDataRange.push(new Array());
  }
  //data is info from json
  for (let part in data) {
    let yearOf = data[part].year;
    //must be done separately otherwise data[part].year will be undefined
    yearOf = parseInt(yearOf);
    if (yearOf >= min && yearOf <= max) {
      for (tester = min; tester <= max; tester += 1){
        // adds crash entry to year slot in array
        if (tester == yearOf) {
          filteredDataRange[tester - min].push(data[part]);
        }
      }
    }
  }
  return filteredDataRange
}
