var twitter = require('twitter-text')
var inp = document.getElementById('myinput');
var chars = document.getElementById('chars');

inp.onkeyup = function() {
  chars.innerHTML = twitter.txt.getTweetLength(inp.value);
}