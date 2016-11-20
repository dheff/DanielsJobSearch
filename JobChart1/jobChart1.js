var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['August 2014','September 2014','November 2014', 'December 2014','January 2015','February 2015','March 2015','April 2015', 'May 2015', 'June 2015', 'July 2015','August 2015','September 2015','November 2015', 'December 2015','January 2016'],
    datasets: [{
      label: 'Total Jobs Applied For',
      data: [72, 84, 84, 92, 96, 96, 98, 124, 149, 154, 176, 201, 275, 404, 448, 454, 464],
      backgroundColor: "rgba(153,255,51,0.6)"
    }]
  }
});
