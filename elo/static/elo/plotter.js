



function plotter(datax,datay,divName){

  var data = [
  {
    x: datax,
    y: datay,
    type: 'scatter'
  }
  ];
  var layout = {
    autosize: false,
    width: 400,
    height: 400,
    margin: {
      l: 50,
      r: 50,
      b: 50,
      t: 50,
      pad: 4
    }
  }

  Plotly.newPlot(divName, data, layout);
}
