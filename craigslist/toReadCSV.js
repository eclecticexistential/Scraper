require('chromedriver');
const selenium = require('selenium-webdriver');
const driver = new selenium.Builder().forBrowser('chrome').build();

var fs = require('fs'),
	path = require('path'),
	filePath = path.join(__dirname, 'Jobs/sofWeb.csv');
	
fs.readFile(filePath, {encoding: 'utf-8'}, function (err,data){
	var reg = /https.*html/g;
	if(!err){
		let matches = data.match(reg)
		let email = /[a-zA-Z0-9]*@.*com/g;
		for(i=0;i<matches.length;i++){
			driver.get(matches[1]);
			let area = driver.wait(selenium.until.elementLocated(selenium.By.id('postingbody')))
			area.getText().then(function(text){
				let attached = text.match(email)
				console.log(attached)
			})
			break
		}
	} else{
		console.log(err);
	}
});
