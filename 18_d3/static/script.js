/*
David Xiedeng
Softdev pd 1
K18 -- Come Up For Air
2020-04-19
*/

//passing info from Flask to js
//indirectly uses a meta tag
var fromFlask = document.getElementById('server-info')
// java info
var data = fromFlask.dataset.server
data = JSON.parse(data)
fromFlask.remove()
