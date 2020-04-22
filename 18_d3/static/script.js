/*
David Xiedeng
Softdev pd 1
K18 -- Come Up For Air
2020-04-19
*/

// passing info from Flask to js
// indirectly uses a meta tag
// inefficent, but no time to change
var fromFlask = document.getElementById('server-info');
// java info
var data = fromFlask.dataset.server;
data = JSON.parse(data);
fromFlask.remove();

function createBarChart(){
  let barData = createBarData(graphBottomYear, graphTopYear);
  //finds slot for bar and empties it
  let barSlot = d3.select('#chart')
    .text("")
    .style("font", "10px sans-serif")
    .style("text-align", "right")
    .style("color", "white");

  // loop through barData to create bars
  for (let i = 0; i < barData.length; i += 1){
    barSlot.append(createBar(barData[i].length));
  }
}

function createBar(length){
  // code from observable hq
  const bar = d3.create("div")
      .data(10)
      .join("div")
      .style("background", "steelblue")
      .style("padding", "3px")
      .style("margin", "1px")
      .style("width", d => `${d * 10}px`)
      .text(d => d);
  return bar.node();
}

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
