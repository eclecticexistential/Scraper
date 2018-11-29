require('chromedriver');
const selenium = require('selenium-webdriver');
const driver = new selenium.Builder().forBrowser('chrome').build();

var fs = require('fs'),
	path = require('path'),
	filePath = path.join(__dirname, 'Jobs/sofWeb.csv');
	
fs.readFile(filePath, {encoding: 'utf-8'}, function (err,data){
	var reg = /https.*html/g;
	if(!err){
		driver.get(matches['https://cincinnati.craigslist.org/sof/d/software-engineer-remote/6749997413.html']);
		let textArea = driver.wait(selenium.until.elementLocated(selenium.By.id('postingbody')))
		let replyBtn = driver.wait(selenium.until.elementLocated(selenium.By.className('reply_button js-only')))
		replyBtn.click()
		let neededInfo = driver.wait(selenium.until.elementLocated(selenium.By.className('mailapp')))
		console.log(neededInfo.getText())
	} else{
		console.log(err);
	}
});


