var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, jobData);
var numbList = document.getElementById('jobList');
for(var i = 0; i < jobList.length; i++){	
	var entry = document.createElement('li');
	entry.appendChild(document.createTextNode(jobList[i]));
	numbList.appendChild(entry);
}


