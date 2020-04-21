/*
David Xiedeng
Softdev pd 1
K18 -- Come Up For Air
2020-04-19
*/

//passing info from Flask to js
//indirectly uses a meta tag
var fromFlask = document.getElementById('server-info');
// java info
var data = fromFlask.dataset.server;
data = JSON.parse(data);
fromFlask.remove();

//lowest year in selection is 1880
var currentYear = 1880;

// selecting meteorites by year
// throws undefined error at the end but array is still built
function filterByYear(year) {
  filteredData = [];
  for (let part in data) {
    // console.log(data[entry].year)
    let temp = data[part]
    // console.log(temp.substring(0,4))
    // console.log(temp, temp == 1990)
    if (year == parseInt(temp.year.substring(0,4))) {
      filteredData.push(temp);
    }
    //console.log(filteredData.length, filteredData)
  }
  return filteredData;
}
